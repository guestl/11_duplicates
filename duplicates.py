import logging
import os.path
import argparse
import collections


def get_file_dictionary(dir_name):
    result_list = dict()

    tree = os.walk(dir_name)

    for disk, dirs, files in tree:
        for file in files:
            path = os.path.join(disk, file)
            path = os.path.abspath(path)
            result_list[path] = ''.join(
                [file, ' - ', str(os.path.getsize(path))])

    return result_list


if __name__ == '__main__':
    # Look at command-line args
    parser = argparse.ArgumentParser(description='This script scans\
             for duplicated files in directories.')
    parser.add_argument('--mf', '-mf', type=str, required=True,
                        help='Main folder full path.')

    args = parser.parse_args()

    folder_name = args.mf

    if os.path.isdir(folder_name):
        print('Scanning..', end='\r')

        file_list = get_file_dictionary(folder_name)

        print('Scanning completed', end='\r')
        print()
    else:
        logging.error("Folder '{}' must exists".format(folder_name))
        exit()

    dup_list = collections.defaultdict(list)

    for key, value in file_list.items():
        dup_list[value].append(key)

    print([dup_items for dup_items in dup_list.values() if len(dup_items) > 1])
