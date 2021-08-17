import pathlib as psl
import sys # sys.stdout
import io # StringIO
import os
def exist_file(abspath: str):
    """
    Returns if a file exists (minified)

    _fileutil.py - Python 3.8 - Ubuntu 20.04 LTS (Tested on Arch Linux (MANJARO))
    """
    return psl.Path(abspath).exists()

def pred_path(path: str, _path2: str):
    """
    Adds two path(es) together.

    _fileutil.py - Python 3.8 - Ubuntu 20.04 LTS
    """
    return path + _path2

def unix_mntdir(path: str):
    return "/" + path

def man_dir(path: str):
    """
    Redirects the path of man to 
    """
    if exist_file("/usr/bin/man"):
        raise TypeError("_fileutil: man is not installed")
    return unix_mntdir("usr/share/man")

