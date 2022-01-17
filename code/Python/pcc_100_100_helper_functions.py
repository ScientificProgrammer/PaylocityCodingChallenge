"""Helper functions for the Paylocity Coding Challenge."""

import os
import re
import sys


__all__ = ["ExtractModuleNameFromFileName", "normalize_path"]

_FILE_EXTENSION = "py"


def normalize_path(path: str) -> str:
    """
    Normalize a file system path regardless of OS.

    CREDITS:
        https://stackoverflow.com/a/20713238/4507836
    """
    return os.path.normpath(os.sep.join(re.split(r"\\|/", path)))


def ExtractModuleNameFromFileName(filename: str) -> str:
    """
    Extract the basename portion of a Python module file.

    EXAMPLES:

        >>> from pcc_100_100_helper_functions import *
        >>> ExtractModuleNameFromFileName('C:\\python\\py_mod.py')
        'py_mod'
        >>> ExtractModuleNameFromFileName('/usr/home/eric/python/py_mod.py')
        'py_mod'

    """

    if filename is None or filename == "":
        raise ValueError("'filename' must not be empty")

    baseFileName = os.path.basename(normalize_path(filename))

    if baseFileName.rpartition(".")[2] != _FILE_EXTENSION:
        errMsg = (
            f"'filename' must terminate with '.{_FILE_EXTENSION}'  "
            "(case sensitive)\n"
        )
        raise ValueError(errMsg)

    moduleName = baseFileName.rpartition(".")[0]

    return moduleName


def main():
    """main() function for module."""

    MODULE_NAME = ExtractModuleNameFromFileName(__file__)

    if len(sys.argv) > 1:
        warnMsg = (
            f"'{MODULE_NAME}' does not accept any command line parameters.\n"
            "See help documentation for more information.\n"
            f"    >>> help({MODULE_NAME})\n"
        )
        raise UserWarning(warnMsg)


if __name__ == "__main__":
    main()
