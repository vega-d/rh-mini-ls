#!/usr/bin/python3
import os
import stat
from datetime import datetime


def mini_ls(files, recursive=False):
    for file in files:
        try:
            if os.path.isdir(file):
                if file in ['.', './']:
                    print("Current Directory:")
                else:
                    print(f"Directory: {file}:")
                _list_dir(file, recursive)
            else:
                print(f"File: {file}:")
                _print_file_info(file)
            print()
        except FileNotFoundError:
            print(f'[ERROR] \"{file}\" is not a file or directory.')
        except NotADirectoryError:
            print(f'[ERROR] \"{file[:-1]}\" is a file and not a directory.')


def _list_dir(directory, recursive):
    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if recursive and os.path.isdir(path):
            _list_dir(path, recursive)
        else:
            _print_file_info(path)


def _print_file_info(path):
    """
    Accepts a path parameter and outputs the stats for it in this format:
    1000 drwxr-xr-x 2024-07-24 12:51:12 venv/
    ownder permissions date time path
    :param path: string
    :return:
    """
    stat_info = os.stat(path)
    owner = stat_info.st_uid
    permissions = stat.filemode(stat_info.st_mode)
    modified_time = datetime.fromtimestamp(stat_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
    print(f"{owner} {permissions} {modified_time} {path.lstrip('./')}" + ('/' if os.path.isdir(path) else ''))


def main():
    import argparse
    parser = argparse.ArgumentParser(description='mini-ls command')
    parser.add_argument('files', nargs='*', default=['.'], help='Files or directories to list')
    parser.add_argument('-r', '--recursive', action='store_true', help='List directories recursively')
    args = parser.parse_args()

    mini_ls(args.files, args.recursive)


if __name__ == '__main__':
    main()
