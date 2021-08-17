import os
import pathlib
import sys
import man._fileutil as fsutil
import tarfile
import zipfile

"""
# importing the "tarfile" module
import tarfile
  

file = tarfile.open('man.1.tar.gz')
  
print(file.getnames())
  

file.extractall('./Destination_FolderName')
  
file.close()
"""


def compress(pageabs: str):
    if fsutil.exist_file(pageabs):
        ManZip = zipfile.ZipFile(pageabs + ".man.gz", 'w')
        ManZip.write(pageabs)
        ManZip.close()
    else:
        raise FileNotFoundError("File for " + pageabs + " not located.")

def read_page(page: str):
    if fsutil.exist_file("/usr/bin/man"):
        os.system("/usr/bin/man " + page)
    else:
        raise FileNotFoundError("Page for " + page + " not located.")

def decompress(path: str):
    if path.endswith(".gz"): # check to make sure it's a manual page type.
        ManZip = zipfile.ZipFile(path, 'r')
        ManZip.extractall()
        ManZip.close()