"""
    Main driver module for the Paylocity Coding Challenge.
"""

import os
import pprint as pp
import sys
import psycopg2
import pcc_030_010_config_parser as connparser
import pcc_030_020_payload_parser as plparser
import pcc_100_100_helper_functions as hf

# Define Global Constants
PAYLOAD_FILE_BASENAME = "010_paylocity_sample_payload_for_db_loading.txt"
PAYLOAD_FILE_DIR_REL = "../../data/"
DB_DSN_FILENAME = "pcc_000_010_aws_pg_dev02.ini"
DB_DSN_FILE_SECTION_NAME = "postgresql"


def GetAbsPathFromRelPath() -> str:
    """
    Encapsulate building the complete file path to the payload file.

    The challenge here was building the complete, absolute
    qualified pathname to the file containing the sample payload
    data.

    This process has to work on both Posix and Windows file systems,
    and it has to work regardless of where the HOME directory
    of this project is located.

    Most of the work is performed by the 'helper functions' in
    the 'pcc_100_100_helper_functions module'. I put all of this
    code here so as to allow the reader to understand what work
    was being done, if they were interested, while simultaneously
    not cluttering up the sequence of events in the program's workflow.

    Here are the two critical assumptions that must be true.

        1)  The payload file must be named as follows.

                "010_paylocity_sample_payload_for_db_loading.txt"

        2)  The payload file must be present in the following
            relative parent directory location.

                "../../data/"
    """
    PAYLOAD_FILE_PATH_ABS = os.path.abspath(
        "/".join([PAYLOAD_FILE_DIR_REL, PAYLOAD_FILE_BASENAME])
    )
    return PAYLOAD_FILE_PATH_ABS


def ParseLocalPayloadFile() -> list:
    """Parse a local payload file."""
    payloadFilename = GetAbsPathFromRelPath()
    hf.BannerPrint(f"Attempting to read payload from {payloadFilename}")
    ParsedPayload = []
    ParsedPayload = plparser.ParsePayloadFile(payloadFilename)
    hf.BannerPrint(
        f"Pretty printing the parsed payload from {payloadFilename}"
    )  # noqa: E501
    pp.pprint(ParsedPayload, width=200)
    return ParsedPayload


def _main():
    """Performs the overall workflow of the Paylocity Coding Challenge"""
    # STEP 1: Print Module Name to the console
    MODULE_NAME = hf.ExtractModuleNameFromFileName(sys.argv[0])
    hf.BannerPrint(f"Module '{MODULE_NAME}' was imported successfully.")

    # STEP 2: Parse the local payload file and save the results.
    # rslt = ParseLocalPayloadFile()
    # pp.pprint(rslt)

    # STEP 3a: Open a connection to the database
    DSN = connparser.ParseDBConfigFile(
        DB_DSN_FILENAME, DB_DSN_FILE_SECTION_NAME
    )  # noqa: E501
    DBConn = None
    SQLStatement = (
        "select table_schema, table_name, table_type\n"
        "from information_schema.tables\n"
        "order by table_schema, table_name;"
    )
    try:
        DBConn = psycopg2.connect(**DSN)
        # print("DBConn should be open")
        # print(DBConn.info)
        dbCursor = DBConn.cursor()
        dbCursor.execute(SQLStatement)
        qryResults = dbCursor.fetchall()
        pp.pprint(qryResults, width=300)
        dbCursor.close()
    except psycopg2.DatabaseError as DBError:
        print(DBError)
    finally:
        if DBConn is not None:
            DBConn.close()
            print("Database connection closed.\n")


if __name__ == "__main__":
    _main()
