import os.path
import argparse
import collections


def get_file_dictionary(dir_name):
    result_list = dict()

    tree = os.walk(dir_name)

    for disk, dirs, file_names in tree:
        for file_name in file_names:
            path = os.path.join(disk, file_name)
            abspath = os.path.abspath(path)
            result_list[abspath] = "{} - {}".format(
                file_name, str(os.path.getsize(abspath)))

    return result_list


def get_duplicates(list_with_duplicates):
    dup_list = collections.defaultdict(list)

    for file_name_size_pair, full_file_name in file_list.items():
        dup_list[full_file_name].append(file_name_size_pair)
    return dup_list


if __name__ == '__main__':
    # Look at command-line args
    parser = argparse.ArgumentParser(description='This script scans\
             for duplicated files in directories.')
    parser.add_argument('main_folder_name', type=str,
                        help='Main folder full path.')

    args = parser.parse_args()

    folder_name = args.main_folder_name

    if os.path.isdir(folder_name):
        print('Scanning..', end='\r')

        file_list = get_file_dictionary(folder_name)

        print('Scanning completed', end='\r')
        print()
    else:
        exit("Folder '{}' must exists".format(folder_name))

    dup_list = get_duplicates(file_list)

    for dup_items in dup_list.values():
        if len(dup_items) > 1:
            print("\n\tFiles with the same pair of file name and file size:")
            for single_duplicate_filename in dup_items:
                print(single_duplicate_filename)
