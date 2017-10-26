# Anti-Duplicator

This script receive a folder name as parameter, scan the folder and its sub-folders and print list of duplicated files in the  the folder.

Duplicated files are files with the same file name and size.

# How to run

This script requires Python 3.5

How yo run in Linux:

```#!bash

$ python duplicates.py d:\test

# possibly requires call of python3 executive instead of just python
```

Output example:

```
python duplicates.py d:\test
Scanning completed

        Files with the same pair of file name and file size:
d:\test\111.docx
d:\test\444\111.docx
```

There is no difference to run in Windows 


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
