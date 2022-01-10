"Testing jedi auto-completion and other features"

import sys
from pathlib import PurePath


def GetModuleName() -> str:
    """
    Return the 'basename' (i.e. with the path stripped out)
    of the currently running module
    """
    return PurePath(sys.argv[0]).stem


def main():
    """Only run if running as a standalone module"""

    print("Just a test")

    print(
        f"""

        The currently running module is named '{GetModuleName()}'.

    """
    )


if __name__ == "__main__":
    main()
