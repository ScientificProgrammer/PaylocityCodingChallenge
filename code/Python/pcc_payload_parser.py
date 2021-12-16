#!/usr/bin/python3
"""
  This module contains the function(s) necessary to parse a file containing sample data that will be
  used to hold a payload for uploading into a PostgreSQL database as part of the
  Paylocity Coding Challenge.
  
  AUTHOR: Eric Milgram, PhD

  APPLICATION: Paylocity Coding Challenge
"""

import sys
import os.path

def parse_payload_file(payload_filename, output_log_file_path = ""):
  """
    PURPOSE:
            Reads an input file, parses its records, stores them in a dictionary of lists.

    PARAMETERS: 
            payload_filename: (string - required)
                              Name of the file that contains the payload data to be parsed.

            output_file_path: (string - optional)
                              Name of the file where the output of the parsing operation
                              should be stored. If this parameter is not furnished,
                              then no output log will be saved.
    RETURNS:
            A dictionary containing all of the valid records read from the input
            file. This dictionary will contain up to four keys, one for each of the expected
            database tables.

              1. Company

              2. Position

              3. Employee

              4. Job

            In turn, each of these dictionaries will contain at least one dictionary, each of which will
            contain a key named "action" whose value will specify at least one of the following actions
            to be performed for the corresponding database table.

              1. INSERT: Insert a new record into the database table.

              2. UPDATE: Update an existing record in the corresponding table.

              3. DELETE: Delete a record from the corresponding database table.
             
             In addition to the requested action, each of these dictionaries will contain additional
             keys that give more information about the record on which the action is to be performed.
             The sample dictionary shown below gives additional insight.

            {
              "Company": [
                {"action": "DELETE", "timestamp": "700.0", "guid": "55bd6d92-7731-4006-9f84-79264f8fba24", "name": "Cheesey Za", "status": "1"},
                {"action": "INSERT", "timestamp": "100.0", "guid": "1c898066-858e-406c-a15d-36146c9642de", "name": "Paylocity", "status": "1"},
                {"action": "UPDATE", "timestamp": "300.0", "guid": "1c898066-858e-406c-a15d-36146c9642de", "name": "Paylocity", "status": "2"}
              ],
              "Position": [
                {"action": "DELETE", "timestamp": "600.0", "guid": "ca391508-2f5d-4529-b7c8-d3d76e05cdd6", "name": "Code Monkey", "status": "1"},
                {"action": "INSERT", "timestamp": "100.0",  "guid": "40a36493-f450-4331-874c-5ef01aabe1d5", "name": "Software Eng", "status": "1"},
                {"action": "UPDATE", "timestamp": "300.0",  "guid": "40a36493-f450-4331-874c-5ef01aabe1d5", "name": "Software Engineer", "status": "1"}
              ],
              "Employee":
              [
                {"action": "INSERT", "timestamp": "100.0",  "guid": "e086115c-0ca1-480c-8fa8-5e1773558b9f", "state": "PA", "status": "1"},
                {"action": "UPDATE", "timestamp": "100.0",  "guid": "d4926109-b6c9-4447-a53c-b787684e10f1", "state": "IL", "status": "2"},
                {"action": "DELETE", "timestamp": "300.0",  "guid": "275ac9c6-8902-4fec-9a19-25ddfc8d8ff8", "state": "OH", "status": "1"},
              ],
              "Job": [
                {
                  "action": "INSERT",
                  "timestamp": "100.0",
                  "guid": "58291fe5-4e4c-41da-87a5-e1fccb8aac25",
                  "company_guid": "1c898066-858e-406c-a15d-36146c9642de",
                  "employee_guid": "e086115c-0ca1-480c-8fa8-5e1773558b9f"
                }
              ] 
            }
  """
  def check_parameters(payload_filename, output_log_file_path):
    err_msg = "Run help(parse_payload_file) for more information on how to use this function.\n"
    # err_msg = "                                                                                                           \n"
    #   err_msg += "**********************************************************************************************************\n"
    #   err_msg += " ERROR in pcc_db_payload_parser.parse_payload_file(): INVALID PARAMETER(S)                               *\n"
    #   err_msg += "**********************************************************************************************************\n"
    #   err_msg += "                                                                                                          \n"
    #   err_msg += "  parse_payload_file() accepts up to 2 parameters but requires at least 1 parameter:                      \n"
    #   err_msg += "                                                                                                          \n"
    #   err_msg += "  PARAMETER                      OPTIONAL/REQUIRED       NOTES                                            \n"
    #   err_msg += "  1) INPUT_PAYLOAD_FILENAME      REQUIRED                Must be a valid filename                         \n"
    #   err_msg += "                                                                                                          \n"
    #   err_msg += "  2) <PARSING_OUTPUT_FILENAME>   OPTIONAL                Must be a valid filename and user must have      \n"
    #   err_msg += "                                                         write permission for the target location         \n"
    #   err_msg += "  DEFAULT VALUES FOR OPTIONAL PARAMETERS:                                                                 \n"
    #   err_msg += "  <PARSING_OUTPUT_FILENAME>                              020_paylocity_output_parsing_sample_payload.txt  \n"
    #   err_msg += "**********************************************************************************************************\n"
    #   err_msg += "                                                                                                          \n"

    if not os.path.exists(payload_filename):
      err_msg = "Payload file '" + str(payload_filename) + "' could not be found.\n" + err_msg
      raise Exception(err_msg)
    else:
      print("I couldn't find an error!")

  check_parameters()

  payload_records = []

  with open(pPayloadFilename,'rt') as payloadFileCursor:
      print("\nOpening", pPayloadFilename, "for reading\n")
      for line in payloadFileCursor:
          payload_records.append(json.loads(line.strip()))
          
  # lstDeletions = [rec for rec in payload_records if rec["action"] == "DELETE"]
  # lstTablesWithDeletions = list(set(vals['source_table'] for vals in lstDeletions))
  # lstTablesWithDeletions.sort()

  source_table_company  = [rec for rec in payload_records if rec["source_table"] == "Company"]
  source_table_position = [rec for rec in payload_records if rec["source_table"] == "Position"]
  source_table_employee = [rec for rec in payload_records if rec["source_table"] == "Employee"]
  source_table_job      = [rec for rec in payload_records if rec["source_table"] == "Job"]

  dictionary_results = {
    "Company":  list(source_table_company),
    "Position": list(source_table_position),
    "Employee": list(source_table_employee),
    "Job":      list(source_table_job)
  }

  # lstTablesWithDeletions = list(set(vals['source_table'] for vals in source_table_company))
  # lstTablesWithDeletions.sort()

  return(dictionary_results)

print(sys.argv[0], "is running as", __name__)

if __name__ == "__main__":
  parse_payload_file(sys.argv(1))
