#!/usr/bin/python3

"""
  This module is used to test connectivity to a PostgreSQL database.
  
  AUTHOR:        Eric Milgram, PhD

  APPLICATION:   Paylocity Coding Challenge

  DEPENDENCIES:  1) NON-STANDARD PYTHON MODULES - PUBLICLY AVAILABLE
                    a) psycopg2               This package does the heavy lifting for connecting to a
                                              PostgreSQL database server. Visit
                                              https://pypi.org/project/psycopg2/
                                              for more details about how to install 'psycopg2' for your
                                              implementation.

                  2) NON-STANDARD PYTHON MODULES - CUSTOM

                    b) pcc_config_parser.py   Wrapper for configparser.ConfigParser

                 2) A valid database configuration file. See the help for 'pcc_config_parser.py' for more information.
                 
"""
import os.path
import sys
import psycopg2
from pcc_config_parser import config
from pathlib import PurePath

class CustomError(Exception):
  """
     Base class for derived Exception classes used in this module.
  """

class InvalidNumCmdLineArgsError(CustomError):
  """
    Thrown when this module is called directly with an invalid number
    of command line arguments.
  """
  def __init__(self, message):
    self.message = message
  
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

            7) Close the database connection.

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
  mod_name = PurePath(sys.argv[0]).stem
  # help_msg = """

  #    For more information about using this module, enter the interactive Python environment and type the following commands.
  #      >>>import {0}
  #      >>> help({0}) 

  #   """.format(mod_name)
  # print(help_msg)

  num_args = len(sys.argv) - 1

  if num_args == 0:
    msg = """
  ------------------------------------------------------------------------------
    No command line arguments were furnished. Attempting to connect
    to the PostgreSQL DB with the following default parameters.

        FILENAME: 'database.ini'                    (default)
        SECTION:  'postgresql'                      (default)
  ------------------------------------------------------------------------------
      """
    print(msg)
    connect()

  elif num_args == 1:
    msg = """
  ------------------------------------------------------------------------------
      One command line argument was given. Attempting to connect to the
      PostgreSQL DB with the following parameters.

        FILENAME: {0}
        SECTION:  'postgresql'                      (default)
  ------------------------------------------------------------------------------
      """.format(sys.argv[1])
    print(msg)
    connect(sys.argv[1])

  elif num_args == 2:
    msg = """
  ------------------------------------------------------------------------------
      One command line argument was given. Attempting to connect to the
      PostgreSQL DB with the following parameters.

        FILENAME: {0}
        SECTION:  {1}
  ------------------------------------------------------------------------------
      """.format(sys.argv[1], sys.argv[2])
    print(msg)
    connect(sys.argv[1], sys.argv[2])

  else:
    err_msg = """
  ------------------------------------------------------------------------------
      ERROR: An invalid number of command line args were given.
             This module should be called with 0, 1, or 2 parameters.
  ------------------------------------------------------------------------------
    """.format(mod_name)
    raise InvalidNumCmdLineArgsError(err_msg)
