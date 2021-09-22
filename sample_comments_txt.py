#!/usr/bin/env python3
"""
Create a text file containing multiple Reddit comment body text.

Usage:
    $ ./sample_comments_txt.py [COMMENTS_DIR] [N] [OUTPUT]

    COMMENTS_DIR    Path to directory containing comment text files
    N               Number of comment files to sample
    OUTPUT          Path to write text file containing sampled comments

"""
import pathlib
import random
import sys


def main():
    if len(sys.argv) < 4:
        raise SystemExit('Usage: sample_comments_txt.py [COMMENTS_DIR] [N] [OUTPUT]')

    comments_dir = pathlib.Path(sys.argv[1])
    if not comments_dir.exists:
        raise SystemExit(f'Cannot find COMMENTS_DIR: {comments_dir}')
    elif not comments_dir.is_dir():
        raise SystemExit(f'COMMENTS_DIR must be a directory: {comments_dir}')
    
    try:
        n = int(sys.argv[2])
    except ValueError:
        raise SystemExit(f'Could not parse N. Please supply an integer value: {sys.argv[2]}')

    output = pathlib.Path(sys.argv[3])
    if output.exists():
        raise SystemExit(f'OUTPUT file already exists: {output}')
    
    comment_files = list(comments_dir.glob('*.txt'))

    if n > len(comment_files):
        raise SystemExit(f'N ({n}) cannot exceed number of comment files ({len(comment_files)}')

    sample_files = set()

    while len(sample_files) < n:
        index = random.randrange(0, len(comment_files))
        sample_file = comment_files[index]
        sample_files.add(sample_file)

    with output.open('w') as f:
        for p in sample_files:
            f.write(f'{p.stem}\n\n\n')
            f.writelines(p.read_text())
            f.write(f'\n\n\n\n\n\n\n\n{"-" * 80}\n')

    print(f'Sampled comment body text written to {output}')

    return 0


if __name__ == '__main__':
    print(main())
