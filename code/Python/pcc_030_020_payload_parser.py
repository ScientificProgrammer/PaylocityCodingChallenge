"""
  This module contains the function(s) necessary to parse a file
  containing sample data that will be used to hold a payload for
  uploading into a PostgreSQL database as part of the
  Paylocity Coding Challenge.

  AUTHOR: Eric Milgram, PhD

  APPLICATION: Paylocity Coding Challenge
"""

import json
import os.path
import pprint
import sys
from pcc_100_100_helper_functions import ExtractModuleNameFromFileName


def ParsePayloadFile(payload_filename: str) -> list:
    """
        PURPOSE:
            Reads an input file, parses its records, stores them in a
            dictionary of lists.

        PARAMETERS:
            1) payload_filename (required):
                Name of the file that contains the payload data to be parsed.

        RETURNS:
            A list containing all of the valid records read from the
            input file, each of which will be stored as a dictionary.

            Each of these dictionaries will contain all of the information
            required to perform updates to the Paylocity Coding Challenge
            Database Schema.

            One of the dictionary keys will be named "action". This key's
            value will specify at least one of the following
            actions to be performed on specific database table.

                1. INSERT: Insert a new record into the database table.

                2. UPDATE: Update an existing record in the corresponding
                           table.

                3. DELETE: Delete a record from the corresponding database
                           table.

            In addition to the requested action, each of these dictionaries
            will contain additional keys that give more information about
            which table and record(s) on which the target actions
            are to be performed. Shown below is a sample list
            that will yield additional insight on the record structure
            to expect.
        [
            {
                "table": "Company",
                "action": "DELETE",
                "timestamp": "700.0",
                "guid": "55bd6d92-7731-4006-9f84-79264f8fba24",
                "name": "Cheesey Za",
                "status": "1"
            },
            {
                "table": "Position"
                "action": "DELETE",
                "timestamp": "600.0",
                "guid": "ca391508-2f5d-4529-b7c8-d3d76e05cdd6",
                "name": "Code Monkey",
                "status": "1"
            },
            {
                "table": "Employee",
                "action": "INSERT",
                "timestamp": "100.0",
                "guid": "e086115c-0ca1-480c-8fa8-5e1773558b9f",
                "state": "PA",
                "status": "1"
            },
            {
                "table": "Job",
                "action": "INSERT",
                "timestamp": "100.0",
                "guid": "58291fe5-4e4c-41da-87a5-e1fccb8aac25",
                "company_guid": "1c898066-858e-406c-a15d-36146c9642de",
                "employee_guid": "e086115c-0ca1-480c-8fa8-5e1773558b9f"
            }
    ]
    """
    if not os.path.exists(payload_filename):
        raise Exception(f"Payload file {payload_filename} could not be found.")

    payload_records = []

    with open(payload_filename, "rt") as payloadFileCursor:
        print("\n")
        print(
            f"{os.path.basename(sys.argv[0])}: Opening",
            payload_filename,
            "for reading\n",
        )

        for line in payloadFileCursor:
            rec = json.loads(line.strip())
            payload_records.append(rec)

        payloadFileCursor.close()

    return payload_records


def _main():
    MODULE_NAME = ExtractModuleNameFromFileName(__file__)

    if len(sys.argv) != 2:
        warnMsg = (
            f"{MODULE_NAME}\n"
            "This module was called from the "
            "command line with an invalid number of parameters. "
            "Module is returning an empty list. `"
            "For more information, see this module's help documentation.\n"
            f"\t>>> help({MODULE_NAME})\n"
        )
        raise UserWarning(warnMsg)
        return []
    rslt = ParsePayloadFile(sys.argv[1])
    pprint.pprint(rslt, width=80)
    return rslt


if __name__ == "__main__":
    _main()
