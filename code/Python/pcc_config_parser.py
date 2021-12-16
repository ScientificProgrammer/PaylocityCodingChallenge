#!/usr/bin/python3

"""
  Read PostgreSQL database configuration values from a .ini file.
  
  AUTHOR: Eric Milgram, PhD

  APPLICATION: Paylocity Coding Challenge

  For more information on using configparser, visit
  https://www.postgresqltutorial.com/postgresql-python/connect/
"""

import sys
import os.path
from configparser import ConfigParser

def config(filename = 'database.ini', section = 'postgresql'):
  """
    PURPOSE:
            Read a configuration file and parse the information
            needed to connect to a PostgreSQL database server.

    PARAMETERS: 
            filename:
              (string - optional)
                            Name of the file that contains the DB credentials
                            and connection information.

            section:
              (string - optional)
                            Name of the file section that contains the
                            credential and connection information.
    RETURNS:
            A Python dictionary containing the information needed
            by the 'psycopg2' module to make a connection to
            a PostgreSQL database.

    OVERVIEW:
          This function performs the following sequence of events.
          1) Check to see if 'filename' exists.

          2) Allocate a new configparser.ConfigParser() object.

          3) Read 'filename' and extract the DB configuration information
             from 'section'. A sample file configuration is shown here.

                [postgresql]
                host=paylocity-db-name.awsservername.us-east-1.rds.amazonaws.com
                port=5432
                database=suppliers
                user=postgres
                password=ASUPERSECRETHARDTOGUESSPASSWORD

              NOTES:
                  a) If file section information does not contain an
                     entry for 'port', a default value of 5432 will be
                     used to attempt connecting to the database.

                  b) The password can contain non-alpha characters such as !@#$%^&. However,
                     if the password does contain '%' characters, each one will have to
                     be escaped by including an extra '%' character. For example,
                     assume that a DB password is 'poqnid$sf%njasdfb'. In the config
                     file, the password line should be written as
                     shown below (notice the %% character). 
                     
                        password=poqnid$sf%%njasdfb

                    If the '%' characters in the password are not properly escaped, Python
                    will interpret the '%' characters as formatting characters and either
                    throw an error trying to interpret the sequence or indicate that the
                    DB credentials/connection information is invalid.

            4) Store the parsed information in a Python dictionary object and return the object
               to the function caller.
            
  """
  if not os.path.exists(filename):
    raise Exception("Unable to find a file with name of '{0}'".format(filename))

  # create a parser
  parser = ConfigParser()

  # read config file
  parser.read(filename)

  # get section, default to postgresql
  db = {}

  if parser.has_section(section):
    params = parser.items(section)
  
    for param in params:
      db[param[0]] = param[1]

  else:
    raise Exception('Section {0} not found in the {1} file'.format(section, filename))

  return db

if __name__ == "__main__":
  num_args = len(sys.argv) - 1

  if num_args == 0:
    print("No command line arguments")
    config()

  elif num_args == 1:
    print("The ini file path is...........................'{0}'".format(sys.argv[1]))
    config(sys.argv[1])  

  elif num_args == 2:
    print("The ini file path is...........................'{0}'".format(sys.argv[1]))
    print("Section of ini file to process is named........'{0}'".format(sys.argv[2]))
    config(sys.argv[1], sys.argv[2])

  else:
    raise Exception("ERROR: Invalid number of command line args.")
