# man.man(1) - Python3 Library for Compressing, Decompressing, and reading Unix manual pages.
## SYNOPSIS

import *man.man* as *man*

*man.compress(page)*

*man.decompress(page)*

*man.read_page(page)*

## DESCRIPTION

*man* is a python3 library for simply reading, compressing, or getting native data about Unix manual pages.

*man* is 100% native and uses no external APIs other than the Python API.

*man* is also **Open Source**, using one of the most liberal licenses (MIT).

## OPTIONS

    **db**
        Sets DEBUG to value. Only valid in Python3 Functions.
    **page**
        The page to look for.
    **abspath**
        The absolute path of something.