"""
    Main driver module for the Paylocity Coding Challenge.
"""


import os
import pprint as pp
import sys

import pcc_030_020_payload_parser


def main():
    PAYLOAD_FILE_BASENAME = "010_paylocity_sample_payload_for_db_loading.txt"

    PAYLOAD_FILE_DIR_REL = "../../data/"

    PAYLOAD_FILE_PATH_ABS = os.path.abspath(
        "/".join([PAYLOAD_FILE_DIR_REL, PAYLOAD_FILE_BASENAME])
    )

    def bannerPrint(
        BannerStr,
        BannerFillChar="*",
        BannerWidth=80,
        PrintNewLineBefore=True,
        PrintNewLineAfter=True,
    ):
        """Print a banner string to highlight important output."""

        if PrintNewLineBefore:
            print("\n")
        print("".ljust(BannerWidth, BannerFillChar))
        print(BannerStr)
        print("".ljust(BannerWidth, BannerFillChar))
        if PrintNewLineAfter:
            print("\n")

    # PROJECT_HOME = PAYLOAD_FILE_PATH_ABS[
    #     0 : PAYLOAD_FILE_PATH_ABS.rfind("/data")  # noqa: E203
    # ]  # noqa: E501

    # CONFIG_FILE_NAME = "/".join(  # noqa: E501
    #     [PROJECT_HOME, PAYLOAD_FILE_PATH_ABS, PAYLOAD_FILE_BASENAME]  # noqa: E501
    # )  # noqa: E501

    MODULE_NAME = os.path.basename(sys.argv[0]).split(".")[0]

    bannerPrint("Test this!")

    bannerPrint(f"Module '{MODULE_NAME}' was imported successfully.\n")
    print(
        "See\n"
        f"        >>> help({MODULE_NAME})\n"
        "\n"
        "for more details on using this module.\n\n"
    )

    bannerPrint(f"Attempting to read payload from {PAYLOAD_FILE_PATH_ABS}")

    rslt = pcc_030_020_payload_parser.ParsePayloadFile(PAYLOAD_FILE_PATH_ABS)

    bannerPrint(
        f"Pretty printing the parsed payload from {PAYLOAD_FILE_PATH_ABS}"
    )  # noqa: E501

    pp.pprint(rslt, width=200)

    return rslt


if __name__ == "__main__":
    main()
