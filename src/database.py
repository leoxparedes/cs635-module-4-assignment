"""
Simple file based data access utility functions.
"""
from pathlib import Path
DB_DIR = Path(__file__).parent

#Read file
def read_csv(filename):
    path = DB_DIR / filename
    if not path.exists():
        return []
    with path.open('r', encoding='utf-8') as f:
        return [line.strip().split(',') for line in f if line.strip()]

#Append to file
def append_csv(filename, row):
    path = DB_DIR / filename
    with path.open('a', encoding='utf-8') as f:
        f.write(','.join(map(str,row)) + '\n')

#Write to file
def write_csv(filename, rows):
    path = DB_DIR / filename
    with path.open('w', encoding='utf-8') as f:
        for row in rows:
            f.write(','.join(map(str,row)) + '\n')
