from jinja2 import Environment, FileSystemLoader
import csv, argparse, os
from datetime import datetime
import uuid

parser = argparse.ArgumentParser(description='Convert csv files to Symfony migrations')
parser.add_argument('-i','--input', help='CSV file path', required=True)
parser.add_argument('-t','--table', help='Table name for insertion', required=True)
parser.add_argument('-s','--skip-header', help='Skip first row on csv', action=argparse.BooleanOptionalAction)
parser.add_argument('-u','--uuid', help='Replace first column with uuids', action=argparse.BooleanOptionalAction)
parser.add_argument('-o','--output', help='Output file location', required=True)

args = parser.parse_args()

if not os.path.exists(args.input):
    raise Exception('Couldn\'t find input path')

# Load data
rows = []
with open(args.input) as f:
    reader = csv.reader(f)

    for index, row in enumerate(reader):
        if args.skip_header and index == 0:
            continue

        rows.append(row)

# Generate template
environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("migration.jinja")

now = datetime.now()
datecode = now.strftime("%Y%m%d%H%M%S")
version = f"Version{datecode}"
filename = version + '.php'

def escape_value(value):
    if type(value) is int:
        return value

    if type(value) is str:
        value.replace("'", "\\'")
        return f"\\'{value}\\'"

statements = []
for row in rows:
    if args.uuid:
        row[0] = str(uuid.uuid4())

    row = [escape_value(value) for value in row]

    values = ", ".join(row)
    statements.append(f"INSERT INTO {args.table} VALUES ({values})")

content = template.render(
    statements=statements,
    table=args.table,
    version=version
)

# Write file
with open(os.path.join(args.output, filename),"w", encoding="utf-8") as f:
    f.write(content)