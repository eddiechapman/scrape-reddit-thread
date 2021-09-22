#!/usr/bin/env python3
"""
Convert CSV reddit comment data into text files. 

Output files will be named `comment_id`.txt and contain only comment body.

Usage:
    $ ./csv2txt.py [COMMENT_CSV] [OUTPUT_DIR]

    COMMENT_CSV     A path to a CSV file containing Reddit comment data
    OUTPUT_DIR      A path to a directory where text file will be written

"""
import csv
import pathlib
import sys


def main():
    if len(sys.argv) < 3:
        raise SystemExit('Usage: csv2txt.py [COMMENT_CSV] [OUTPUT_DIR]')
    
    comments_file = pathlib.Path(sys.argv[1])
    if not comments_file.exists():
        raise SystemExit(f'Could not find COMMENT_CSV: {comments_file}')
    
    output_dir = pathlib.Path(sys.argv[2])
    if output_dir.exists() and not output_dir.is_dir():
        raise SystemExit(f'OUTPUT_DIR is not a directory: {output_dir}')

    output_dir.mkdir(exist_ok=True)

    with comments_file.open('r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            p = output_dir / pathlib.Path(row['id'] + '.txt')
            p.write_text(row['body'])

    print(f'Text files written to {output_dir}')

    return 0


if __name__ == '__main__':
    print(main())
