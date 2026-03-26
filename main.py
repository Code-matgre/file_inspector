import os

from file_inspector import core

import argparse

def main():
    parser = argparse.ArgumentParser(description='File Inspector')
    parser.add_argument('--file', type=str, help='Path to the file to inspect')
    args = parser.parse_args()

    print(f'analizzando: {args.file}')
    risultato = core.calchash(args.file)
    print(f'sha256: {risultato[0]}')
    print(f'md5: {risultato[1]}')
    print(f'sha1: {risultato[2]}')

if __name__ == "__main__":
    main()