import os
import argparse
from .utils import get_directory_structure, write_structure_to_file

def main():
    parser = argparse.ArgumentParser(description='Generate directory structure.')
    parser.add_argument('root_dir', type=str, nargs='?', default='.', help='Root directory to traverse (default: current directory)')
    parser.add_argument('output_file', type=str, nargs='?', default='directory_structure.txt', help='Output file to save the directory structure (default: directory_structure.txt)')
    args = parser.parse_args()
    
    structure = get_directory_structure(args.root_dir)
    write_structure_to_file(structure, args.output_file)

if __name__ == '__main__':
    main()
