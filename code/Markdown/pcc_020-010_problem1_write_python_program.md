# Paylocity Coding Challenge: Problem 1 of 2

<div style="font-size: 1.5em; padding-bottom: 0;">

Eric Milgram, PhD

</div>

<table>
<tbody>
<tr>
<td style="padding: 0; display: none;">
<a href="https://github.com/ScientificProgrammer/PaylocityCodingChallenge">ScientificProgrammer/PaylocityCodingChallenge</a>
</td>
</tr>
<tr>
<td style="padding: 0;">
Created: December 15, 2021
</td>
</tr>
<tr>
<td style="padding: 0;">
Last Updated: 2022-01-19 08:04:56</span>
</td>
</tr>
</tbody>
</table>

## Write a Python script to `INSERT`, `UPDATE`, or `DELETE` records in a PostgreSQL database.

### You’re tasked with writing a Python script, which must do the following items.

1.  Read in a file that contains multiple lines.

    1.  Each line will be a JSON formatted record (which may be from any
        of the models above).

    2.  You will be able to differentiate which table to use by reading
        an extra column inside each record called `source_table`.

    3.  This state information can be found using `source_table`,
        `guid`, `action`, and `timestamp`.

2.  Print out the final state of each record (after all actions have
    been applied).

**NOTE**: You are free to add additional columns to your models as you
see fit for the purpose of testing your application.

A sample input file is provided for you. It can be downloaded directly
from the [data
subdirectory](./data/010_Paylocity_sample_payload_for_DB_loading.txt) of
this repo, and it is also available in the **Appendix** (see
[below](#31-sample-input-database-payload-file)). When processing this
file, your code should print an output similar to what is shown here.

------------------------------------------------------------------------

    Company
    ==========
    {'guid': '1c898066-858e-406c-a15d-36146c9642de', 'name': 'Paylocity', 'status': '2'}
    {'guid': '0090d7b0-b07a-47cd-b295-ff798a6c0613', 'name': 'Burrito Shack', 'status': '2'}

------------------------------------------------------------------------

    Position
    ==========
    {'guid': '40a36493-f450-4331-874c-5ef01aabe1d5', 'name': 'Software Engineer', 'status': '1'}
    {'guid': 'f9b3ee71-7fb2-4dd5-9c13-b4c10d11fde7', 'name': 'Data Engineer',     'status': '1'}

------------------------------------------------------------------------

    Employee
    ==========
    {'guid': 'e086115c-0ca1-480c-8fa8-5e1773558b9f', 'state': 'FL', 'status': '2'}
    {'guid': '4e0c8c17-b031-4a72-b73d-f0a85570826d', 'state': 'MI', 'status': '3'}
    {'guid': 'd4926109-b6c9-4447-a53c-b787684e10f1', 'state': 'IL', 'status': '3'}
    {'guid': '259d5154-5f76-481b-b0f9-53e24c3b570e', 'state': 'NY', 'status': '1'}

------------------------------------------------------------------------

    Job
    ==========
    {'guid': '58291fe5-4e4c-41da-87a5-e1fccb8aac25', 'company_guid': '1c898066-858e-406c-a15d-36146c9642de', 'employee_guid': 'e086115c-0ca1-480c-8fa8-5e1773558b9f'}
    {'guid': 'f73a2796-4579-4779-8345-f0dfcf7dd533', 'company_guid': '0090d7b0-b07a-47cd-b295-ff798a6c0613', 'employee_guid': '4e0c8c17-b031-4a72-b73d-f0a85570826d'}
    {'guid': '5ab54bb5-b72d-40f8-9a49-e0d2d004d7a9', 'company_guid': '0090d7b0-b07a-47cd-b295-ff798a6c0613', 'employee_guid': '259d5154-5f76-481b-b0f9-53e24c3b570e'}

------------------------------------------------------------------------

Your code will be evaluated on the following elements, which will also
form the basis for our questions.

1.  Algorithm

2.  Print Management

3.  Code Abstraction

4.  Documentation

5.  Testing

<blockquote style="font-size: 1.75em; background-color: lightgray; box-shadow: 5px 5px 10px black; margin: 2em auto 2em auto; padding: 1.5em; border-radius: 1em; text-align; center;">
This is your chance to show us what you can do! Have fun with the
exercise!
</blockquote>

------------------------------------------------------------------------

# APPENDICES

## Sample Input Database Payload File

NOTE: Although the full contents of the sample payload file are shown
below, you can also download the file from the [data
subdirectory](./data/010_Paylocity_sample_payload_for_DB_loading.txt) of
this repo.

Alternatively, you can also download this file directly using `curl` or
`wget` via the [raw
link](https://raw.githubusercontent.com/ScientificProgrammer/PaylocityCodingChallenge/master/data/010_Paylocity_sample_payload_for_DB_loading.txt).
See the code in the next section for an example.

### Bash Shell Code to Download the Payload Data File

    BASE_URL="raw.githubusercontent.com/ScientificProgrammer/PaylocityCodingChallenge"
    FILE_NAME="010_Paylocity_sample_payload_for_DB_loading.txt"

    curl -i -SL "https://${BASE_URL}/master/data/${FILE_NAME}" -o ${FILE_NAME}

------------------------------------------------------------------------

### Full Data Set

    { "source_table": "Company",  "action": "INSERT", "timestamp": "100.0",  "guid": "1c898066-858e-406c-a15d-36146c9642de", "name": "Paylocity",  "status": "1" }
    { "source_table": "Company",  "action": "INSERT", "timestamp": "200.0",  "guid": "0090d7b0-b07a-47cd-b295-ff798a6c0613", "name": "Taco Shack", "status": "1" }
    { "source_table": "Company",  "action": "UPDATE", "timestamp": "300.0",  "guid": "1c898066-858e-406c-a15d-36146c9642de", "name": "Paylocity",  "status": "2" }
    { "source_table": "Employee", "action": "INSERT", "timestamp": "100.0",  "guid": "e086115c-0ca1-480c-8fa8-5e1773558b9f", "state": "PA", "status": "1" }
    { "source_table": "Job",      "action": "INSERT", "timestamp": "100.0",  "guid": "58291fe5-4e4c-41da-87a5-e1fccb8aac25", "company_guid": "1c898066-858e-406c-a15d-36146c9642de", "employee_guid": "e086115c-0ca1-480c-8fa8-5e1773558b9f" }
    { "source_table": "Position", "action": "INSERT", "timestamp": "100.0",  "guid": "40a36493-f450-4331-874c-5ef01aabe1d5", "name": "Software Eng",  "status": "1" }
    { "source_table": "Company",  "action": "UPDATE", "timestamp": "400.0",  "guid": "0090d7b0-b07a-47cd-b295-ff798a6c0613", "name": "Burrito Shack", "status": "1" }
    { "source_table": "Employee", "action": "INSERT", "timestamp": "200.0",  "guid": "275ac9c6-8902-4fec-9a19-25ddfc8d8ff8", "state": "OH", "status": "1" }
    { "source_table": "Employee", "action": "INSERT", "timestamp": "400.0",  "guid": "4e0c8c17-b031-4a72-b73d-f0a85570826d", "state": "VA", "status": "1" }
    { "source_table": "Job",      "action": "INSERT", "timestamp": "200.0",  "guid": "f73a2796-4579-4779-8345-f0dfcf7dd533", "company_guid": "0090d7b0-b07a-47cd-b295-ff798a6c0613", "employee_guid": "4e0c8c17-b031-4a72-b73d-f0a85570826d" }
    { "source_table": "Employee", "action": "DELETE", "timestamp": "300.0",  "guid": "275ac9c6-8902-4fec-9a19-25ddfc8d8ff8", "state": "OH", "status": "1" }
    { "source_table": "Position", "action": "INSERT", "timestamp": "200.0",  "guid": "f9b3ee71-7fb2-4dd5-9c13-b4c10d11fde7", "name": "Data Eng", "status": "1" }
    { "source_table": "Employee", "action": "UPDATE", "timestamp": "500.0",  "guid": "e086115c-0ca1-480c-8fa8-5e1773558b9f", "state": "PA", "status": "2" }
    { "source_table": "Employee", "action": "UPDATE", "timestamp": "600.0",  "guid": "e086115c-0ca1-480c-8fa8-5e1773558b9f", "state": "FL", "status": "2" }
    { "source_table": "Company",  "action": "UPDATE", "timestamp": "400.0",  "guid": "0090d7b0-b07a-47cd-b295-ff798a6c0613", "name": "Burrito Shack",     "status": "2" }
    { "source_table": "Position", "action": "UPDATE", "timestamp": "300.0",  "guid": "40a36493-f450-4331-874c-5ef01aabe1d5", "name": "Software Engineer", "status": "1" }
    { "source_table": "Employee", "action": "UPDATE", "timestamp": "700.0",  "guid": "4e0c8c17-b031-4a72-b73d-f0a85570826d", "state": "VA", "status": "2" }
    { "source_table": "Employee", "action": "INSERT", "timestamp": "800.0",  "guid": "d4926109-b6c9-4447-a53c-b787684e10f1", "state": "IL", "status": "1" }
    { "source_table": "Company",  "action": "INSERT", "timestamp": "600.0",  "guid": "55bd6d92-7731-4006-9f84-79264f8fba24", "name": "Cheesey Za", "status": "1" }
    { "source_table": "Employee", "action": "INSERT", "timestamp": "900.0",  "guid": "7010237f-3cfa-4dcf-83f5-39d6bd912b91", "state": "CA", "status": "1" }
    { "source_table": "Position", "action": "INSERT", "timestamp": "400.0",  "guid": "ca391508-2f5d-4529-b7c8-d3d76e05cdd6", "name": "Code Monkey", "status": "1" }
    { "source_table": "Employee", "action": "UPDATE", "timestamp": "100.0",  "guid": "d4926109-b6c9-4447-a53c-b787684e10f1", "state": "IL", "status": "2" }
    { "source_table": "Employee", "action": "UPDATE", "timestamp": "1100.0", "guid": "7010237f-3cfa-4dcf-83f5-39d6bd912b91", "state": "NV", "status": "2" }
    { "source_table": "Position", "action": "UPDATE", "timestamp": "500.0",  "guid": "f9b3ee71-7fb2-4dd5-9c13-b4c10d11fde7", "name": "Data Engineer", "status": "1" }
    { "source_table": "Employee", "action": "UPDATE", "timestamp": "1200.0", "guid": "4e0c8c17-b031-4a72-b73d-f0a85570826d", "state": "VA", "status": "3" }
    { "source_table": "Employee", "action": "DELETE", "timestamp": "1300.0", "guid": "7010237f-3cfa-4dcf-83f5-39d6bd912b91", "state": "NV", "status": "2" }
    { "source_table": "Position", "action": "DELETE", "timestamp": "600.0",  "guid": "ca391508-2f5d-4529-b7c8-d3d76e05cdd6", "name": "Code Monkey", "status": "1" }
    { "source_table": "Employee", "action": "UPDATE", "timestamp": "1400.0", "guid": "d4926109-b6c9-4447-a53c-b787684e10f1", "state": "IL", "status": "3" }
    { "source_table": "Employee", "action": "UPDATE", "timestamp": "1500.0", "guid": "4e0c8c17-b031-4a72-b73d-f0a85570826d", "state": "MI", "status": "3" }
    { "source_table": "Company",  "action": "DELETE", "timestamp": "700.0",  "guid": "55bd6d92-7731-4006-9f84-79264f8fba24", "name": "Cheesey Za", "status": "1" }
    { "source_table": "Employee", "action": "INSERT", "timestamp": "1600.0", "guid": "259d5154-5f76-481b-b0f9-53e24c3b570e", "state": "NY", "status": "1" }
    { "source_table": "Job",      "action": "INSERT", "timestamp": "300.0",  "guid": "5ab54bb5-b72d-40f8-9a49-e0d2d004d7a9", "company_guid": "0090d7b0-b07a-47cd-b295-ff798a6c0613", "employee_guid": "259d5154-5f76-481b-b0f9-53e24c3b570e" }

<div style="height: 5em;">

</div>
