#!/usr/bin/python3

"""
  This module is used to test connectivity to a PostgreSQL database.
  
  AUTHOR:        Eric Milgram, PhD

  APPLICATION:   Paylocity Coding Challenge

  DEPENDENCIES:  1) NON-STANDARD PYTHON MODULES
                    a) pcc_config_parser.py

                 2) A valid database configuration file. See the help for 'pcc_config_parser.py' for more information. 
                 
"""

import os.path
import sys
import psycopg2
from pcc_config_parser import config

def connect(configfilename = 'database.ini', configfilesection = 'postgresql'):
  """
    PURPOSE:
            Test the ability to connect to a PostgreSQL database.

    PARAMETERS: 
            configfilename:
              (string - optional)
                            Name of the file that contains the DB credentials
                            and connection information.

            configfilesection:
              (string - optional)
                            Name of the file section that contains the
                            credential and connection information.
    RETURNS:
            Nothing

    OVERVIEW:
            This function performs the following sequence of events.

            1) Uses the 'pcc_config_parser.config() function to parse a configuration file
               containing the security credentials needed to connect to a PostgreSQL database.

            2) Use the credentials to make the connection to the database.

            3) From the db connection object, request a database cursor and save it.

            4) Use the database cursor to execute a single 'SELECT version()' statement.

            5) Print the database version information to 'stdout'.

            6) Close the database cursor.

            7) Close the database cursor.

    ACKNOWLEDGMENTS:
            This code was adapted from the following web-page.
            https://www.geeksforgeeks.org/postgresql-connecting-to-the-database-using-python/
  """
  conn = None

  try:
    # 1) Read DB connection parameters.
    params = config(configfilename, configfilesection)

    # 2) Connect to the PostgreSQL server.
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(**params)
  
    # 3) Create a database cursor.
    cur = conn.cursor()
    
    # 4) Execute a single SELECT statement.
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')

    # 5) Display the PostgreSQL database server version.
    db_version = cur.fetchone()
    print(db_version)
    
    # 6) Close the communication with the PostgreSQL
    cur.close()

  except (Exception, psycopg2.DatabaseError) as error:
    print(error)

  finally:
    # 7) Close the database connection.
    if conn is not None:
      conn.close()
      print('Database connection closed.')
 
if __name__ == "__main__":
  help_msg = "For more information about this module, type help({0}) from within the interactive Python environment.".format(sys.argv[0])
  num_args = len(sys.argv) - 1

  if num_args == 0:
    print("No command line arguments were given. Connecting with default parameters.")
    print("DEFAULT FILENAME: database.ini")
    print("DEFAULT SECTION:  postgresql")
    connect()

  elif num_args == 1:
    print("Database ini file path is......................{0}".format(sys.argv[1]))
    connect(sys.argv[1])  

  elif num_args == 2:
    print("Database ini file path is......................{0}".format(sys.argv[1]))
    print("Section of database ini file to process is.....{0}".format(sys.argv[2]))
    connect(sys.argv[1], sys.argv[2])

  else:
    err_msg  = "ERROR: An invalid number of command line args were given.\n"
    err_msg += "       For more information, please see the help documentation\n"
    err_msg += "       for this module, '{0}' and\n".format(sys.argv[0])
    err_msg += "       'pcc_config_parser.py'. If you are running Python interactively,\n"
    err_msg += "       try the following from the command prompt.\n"
    err_msg += "       \n"
    err_msg += "       help({0})\n".format(sys.argv[0])
    err_msg += "       help(pcc_config_parser)\n"
    err_msg += "       \n"
    raise Exception(err_msg)
