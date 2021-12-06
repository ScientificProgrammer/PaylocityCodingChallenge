<div style="font-size: 1em;">

Last updated on 2021-12-06 09:33:01

</div>

------------------------------------------------------------------------

<!---
::: {style="font-size: 1.25em; color: gray;"}
This coding challenge will be part of the interview for Paylocity.
:::
--->
<blockquote style="font-size: 1.75em; background-color: lightgray; box-shadow: 5px 5px 10px black; margin: 2em auto 2em auto; padding: 1.5em; border-radius: 1em; text-align; center;">

A written summary of the candidate’s work from these coding challenges
must be submitted to Paylocity at least 24 hours prior to the
candidate’s interview.

</blockquote>

------------------------------------------------------------------------

<!--- ********************** PART 1: CODING CHALLENGE OVERVIEW ********************** --->

# 1 PAYLOCITY CODING CHALLENGE OVERVIEW

## 1.1 PYTHON EXERCISE

Each candidate is required to complete the following exercise and return
it a minimum of 24 hours before their interview. They will be asked to
share their ideas with the team during the interview. They should be
prepared to walk the team through concepts such as the following.

1.  “*Here is a summary of the work that I performed.*”

2.  “*How did I accomplish the task?*”

3.  “*Why did I choose a particular approach?*”

Also be prepared for a few questions from the team such as, “*What would
you do if ‘this issue’ came up?*”

The team wants to get an idea how the person thinks. Also, the
submitted/developed code should run.

The expectation is that the candidate will complete the `Python`
exercise ahead of time and walk through their answer during the
**Technical Interview**. The candidate will be expected to present their
code and show it running on their machine.

## 1.2 MULTI-PART SQL EXERCISE: LIVE WALK-THROUGH

Shown below are three tables from a relational database conceptual data
model.

<div style='float: left; margin-right: 1em;'>

<table class="table table-bordered table-striped table-hover table-condensed table-responsive" style="width: auto !important; margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;color: white !important;background-color: gray !important;font-size: 20px;"> Employee </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;width: 15em; "> guid </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 15em; "> status </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 15em; "> state </td>
  </tr>
</tbody>
</table>

</div>

<div style='float: left; margin: 0 1em 0 1em;'>

<table class="table table-bordered table-striped table-hover table-condensed table-responsive" style="width: auto !important; margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;color: white !important;background-color: gray !important;font-size: 20px;"> Company </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;width: 15em; "> guid </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 15em; "> name </td>
  </tr>
</tbody>
</table>

</div>

<div style='float: left; margin: 0 1em 0 1em;'>

<table class="table table-bordered table-striped table-hover table-condensed table-responsive" style="width: auto !important; margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;color: white !important;background-color: gray !important;font-size: 20px;"> Job </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;width: 15em; "> guid </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 15em; "> company_guid </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 15em; "> position_guid </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 15em; "> employee_guid </td>
  </tr>
</tbody>
</table>

</div>

<div style="clear: both;">

The expectation is that the candidate is able to write SQL live while
using whatever tool they have access to, as well as asking questions of
the team. For our data needs, we will be either retrieving or inserting
additional data into our physical database schema that is based on the
data model described here. All of the following actions will be
performed on the physical database schema.

</div>

**ACTIONS**

-   INSERT
-   UPDATE
-   DELETE

A `timestamp` will be inserted or updated with various records in each
of the tables in our database.

------------------------------------------------------------------------

<!--- ********************** PART 2: CODING CHALLENGE DETAILS ********************** --->

# 2 CODING CHALLENGE DETAILS

## 2.1 WRITE A PYTHON SCRIPT

You’re tasked with writing a Python script, which must do the following
items.

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
this repo, and it is also available in the Appendix (see
[below](#31-sample-input-database-payload-file)). When processing this
file, your code should print an output similar to what is shown here.

------------------------------------------------------------------------

    Company
    ==========
    {'guid': '1c898066-858e-406c-a15d-36146c9642de', 'name': 'Paylocity', 'status': '2'}
    {'guid': '0090d7b0-b07a-47cd-b295-ff798a6c0613', 'name': 'Burrito Shack', 'status': '2'}

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

    Position
    ==========
    {'guid': '40a36493-f450-4331-874c-5ef01aabe1d5', 'name': 'Software Engineer', 'status': '1'}
    {'guid': 'f9b3ee71-7fb2-4dd5-9c13-b4c10d11fde7', 'name': 'Data Engineer',     'status': '1'}

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

## 2.2 SQL EXERCISE

[Figure 1](#fig-container-erd-company-employee-position), which is shown
below, illustrates an *entity relationship diagram* (ERD) for a logical
data model consisting of three tables named *Company*, *Employee*, and
*Position*. The ERD represented in **Figure 1** also contains the
following informational elements, which are important for constructing a
physical data model.

1.  *Field names* for each table

2.  *Data types* for each field

3.  *Field constraints*, including *primary keys* and *foreign keys*

4.  *Foreign key relationships* between *tables*, including
    *directionality*, *cardinality*, and *optionality*

<div id="fig-container-erd-company-employee-position"
style="margin: 2em auto 2em auto; padding: 2em; border: solid thin black; border-radius: 2em; box-shadow: 3px 3px 5px black;">

![**FIGURE 1:** Sample ERD for logical data model for a company/employee
relational
database](img/fig_company_db_schema_939x151.png "Entity Relationship Diagram for a Company/Employee Logical Data Model")

</div>

For the data model illustrated in **Figure 1**, please complete the
following actions.

1.  Write a SQL query to generate a result set for a report that
    contains the average salary for all employees.

2.  Update the previous query to generate a result set showing the
    average salary for all employees within each company.

3.  Let’s assume your previous query was long running. Please describe
    the process you would use to find the root causes of the query’s
    sluggishness?

------------------------------------------------------------------------

# 3 APPENDICES

## 3.1 Sample Input Database Payload File

NOTE: Although the full contents of the sample payload file are shown
below, you can also download the file directly from the [data
subdirectory of this
repo](./data/010_Paylocity_sample_payload_for_DB_loading.txt). Also, the
[raw
content](https://raw.githubusercontent.com/ScientificProgrammer/PaylocityCodingChallenge/master/data/010_Paylocity_sample_payload_for_DB_loading.txt)
of the file can be downloaded directly using https.

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
