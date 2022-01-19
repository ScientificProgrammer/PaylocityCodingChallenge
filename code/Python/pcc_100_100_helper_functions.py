"""Helper functions for the Paylocity Coding Challenge."""

import os
import re
import sys


__all__ = ["ExtractModuleNameFromFileName", "normalize_path", "BannerPrint"]

_FILE_EXTENSION = "py"


# def BannerPrint(
#     MarquisStr: str,
#     BannerChar: str = "*",
#     BannerWidth: int = "80",
#     *,
#     PrintTopBorder: bool = True,
#     LinesAboveTopBorder: int = 1,
#     LinesBelowTopBorder: int = 0,
#     LinesAboveMarquisStr: int = 1,
#     LinesBelowMarquisStr: int = 1,
#     PrintBottomBorder: bool = True,
#     LinesAboveBottomBorder: int = 0,
#     LinesBelowBottomBorder: int = 1,
# ) -> str:
#     """
#         Print a banner to make a text string standout.

#                                     LinesAboveTopBorder    == 1
#     ******************************  PrintTopBorder         == True
#            My Sample Text           MarquisStr             == "My Sample Text"
#     ******************************  PrintBottomBorder      == True
#                                     LinesBelowBottomBorder == 1
#     """
#     if PrintTopBorder:
#         if int(LinesAboveTopBorder) > 0:
#             print("\n" * int(LinesAboveTopBorder - 1))
#         if int(LinesBelowTopBorder) > 0:
#             print("\n" * int(LinesBelowTopBorder - 1))
#     if int(LinesAboveMarquisStr) > 0:
#         print("\n" * int(LinesAboveMarquisStr - 1))
#     if int(BannerWidth - len(MarquisStr)) > 2:
#         print(MarquisStr.center(BannerWidth - 2, " "))
#     else:
#         print(MarquisStr)
#     if int(LinesBelowMarquisStr) > 0:
#         print("\n" * int(LinesBelowMarquisStr - 1))
#     if PrintBottomBorder:
#         if int(LinesAboveBottomBorder) > 0:
#             print("\n" * int(LinesAboveBottomBorder - 1))
#         if int(LinesBelowBottomBorder) > 0:
#             print("\n" * int(LinesBelowBottomBorder - 1))


def BannerPrint(
    MarquisStr: str, BannerChar: str = "*", BannerWidth: int = 80
) -> str:  # noqa: E501
    """
    Print a banner to make a text string standout.
    """

    print("")
    print("".ljust(BannerWidth, "*"))
    if int(BannerWidth) - len(MarquisStr) > 2:
        print(f" {MarquisStr} ".center(int(BannerWidth) - 2, " "))
    else:
        print(MarquisStr)
    print("".ljust(BannerWidth, "*"))
    print("")


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
