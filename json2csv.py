import csv
import json
import pathlib
import sys

COMMENT_FIELDS = [
    'id',
    'author',
    'body', 
    'created',
    'created_utc',
    'score',
    'ups',
    'downs',
    'controversiality',
    'is_submitter',
    'edited',
    'depth', 
    'name', 
    'parent_id',  
    'permalink'
]


def main():
    if not len(sys.argv) == 3:
        raise SystemExit('Usage: json2csv.py [JSON DIRECTORY] [OUTFILE]')

    print('Finding comment data...')

    json_dir = pathlib.Path(sys.argv[1])
    if not json_dir.exists():
        raise SystemExit(f'Could not locate {sys.argv[1]}')
    elif not json_dir.is_dir():
        raise SystemExit(f'Error - not a directory: {sys.argv[1]}')

    outfile = pathlib.Path(sys.argv[2])
    if outfile.exists():
        raise SystemExit(f'OUTFILE already exists: {outfile}')

    print('Reading comment data...')

    json_data = []
    for p in json_dir.iterdir():
        if p.suffix.endswith('json'):
            with p.open('r') as f:
                data = json.load(f)
                data_cleaned = {k: v for k, v in data.items() if k in COMMENT_FIELDS}
                json_data.append(data_cleaned)

    print('Writing comment data to csv...')

    with outfile.open('w') as f:
        writer = csv.DictWriter(f, fieldnames=COMMENT_FIELDS)
        writer.writeheader()
        writer.writerows(json_data)

    print(f'Finished writing comment data to {outfile}')

    return 0


if __name__ == '__main__':
    print(main())
