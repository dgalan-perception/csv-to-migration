This script allows you to convert csv files to symfony migrations.

# Usage
First, install requirements
```
pip install -r requirements.txt
```

Then follow usage instructions
```
usage: generate.py [-h] -i INPUT -t TABLE [-s | --skip-header | --no-skip-header] [-u | --uuid | --no-uuid] -o OUTPUT

Convert csv files to Symfony migrations

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        CSV file path
  -t TABLE, --table TABLE
                        Table name for insertion
  -s, --skip-header, --no-skip-header
                        Skip first row on csv
  -u, --uuid, --no-uuid
                        Replace first column with uuids
  -o OUTPUT, --output OUTPUT
                        Output file location
```

Example usage loading a CSV, skipping first row, and writting to current directory
```
python3 generate.py -i /home/user/Documents/WORK/utils/pct_phone_prefix.csv -t phone_prefix -o . -s
```