# Parse a payload file that will be used to hold a payload for
# uploading into a PostgreSQL database

import sys
import json
import pprint as pp

if len(sys.argv) != 3:
  print("ERROR:")
  print("\t", sys.argv[0], "must be called with exactly 2 parameters, 'INPUT_PAYLOAD_FILE_PATH' and 'OUTPUT_FILE_PATH'")
  print("\n\t", "EXAMPLE: must be called with exactly 2 parameters, 'INPUT_PAYLOAD_FILE_PATH' and 'OUTPUT_FILE_PATH'")
  print("\t", "In this instance, it was called with", len(sys.argv) - 1, "parameters.")

#payloadFilename = "D:/GoogleDrive/eric.milgram/Career/Job Prospects/2021-11-09 Paylocity/020 Paylocity Coding Challenge/Paylocity Coding Challenge/data/010_Paylocity_sample_payload_for_DB_loading.txt"
payloadFilename = "./data/010_Paylocity_sample_payload_for_DB_loading.txt"

#outputFilename = "D:/GoogleDrive/eric.milgram/Career/Job Prospects/2021-11-09 Paylocity/020 Paylocity Coding Challenge/Paylocity Coding Challenge/output/010_payload_parsing_results.txt"
outputFilename = "./output/010_payload_parsing_results.txt"

payloadRecords = []

with open(payloadFilename,'rt') as payloadFileCursor:
    # read the file with a for loop
    for line in payloadFileCursor:
        payloadRecords.append(json.loads(line.strip()))
        
print("\n", len(payloadRecords), " lines were read from '", payloadFilename, "'", sep = "")

# for rec in payloadRecords[0:5]:
#   pp.pprint(rec)
#   print("\n")

# for rec in sorted(payloadRecords, key = lambda rec : (rec["action"], rec["source_table"])):
#   pp.pprint(rec)
#   print("\n")

lstDeletions = [rec for rec in payloadRecords if rec["action"] == "DELETE"]
lstTablesWithDeletions = list(set(vals['source_table'] for vals in lstDeletions))
lstTablesWithDeletions.sort()

print("==========================================================")
print("                     DELETIONS                            ")
print("==========================================================")
print("Names of tables with deletions:")
print("==========================================================")

for tblName in lstTablesWithDeletions:
  print(tblName)

print("==========================================================")
print("There are", len(lstDeletions), "records to DELETE")
print("==========================================================")

for rec in lstDeletions:
  pp.pprint(rec)
  print("==========================================================")

