"""
  Read PostgreSQL database configuration values from a .ini file.

  AUTHOR: Eric Milgram, PhD

  APPLICATION: Paylocity Coding Challenge

  For more information on using configparser, visit
  https://www.postgresqltutorial.com/postgresql-python/connect/
"""

import sys
import os
import errno
from configparser import ConfigParser


class CustomError(Exception):
    """Base class for exceptions defined in this module."""


class InvalidNumArgsError(CustomError):
    """
    Thrown when this module is called directly with an invalid number
    of command line arguments.
    """


class ConfigFileNotFoundError(CustomError):
    """
    Exception raised if the target 'config' file cannot be found.

    Attributes:
        config_filename    --Name of the file that was attempted to be parsed.

        long_message       --A more detailed error message

        message             --Concise error message
    """

    def __init__(self, config_filename):
        self.errcode = errno.ENOENT
        self.errmsg = os.strerror(errno.ENOENT)
        self.config_filename = config_filename
        self.message = f"""

**********************************************************
  ERROR ATTEMPTING TO READ DATABASE CONFIGURATION FILE
**********************************************************
    ERROR CODE: '{self.errcode}'
    ERROR MSG:  '{self.errmsg}'
    FILENAME:   '{self.config_filename}'

 The specified database configuration file could not be
 located. Please ensure that the file exists and you
 have read permissions for it.
***********************************************************

        """
        super().__init__(self.message)


class InvalidConfigSectionError(CustomError):
    """
    Exception raised if the target 'section' is not found
    in a file to be parsed.

    Attributes:
        config_filename    --Name of the file that was attempted to be parsed.

        section_name       --The name of the targer 'section' that was not
                             found in the config file.

        message            --Concise error message
    """

    def __init__(self, config_filename, section_name):
        self.config_filename = config_filename
        self.section_name = section_name
        self.message = f"""

**********************************************************
  ERROR ATTEMPTING TO PARSE DATABASE CONFIGURATION FILE
**********************************************************
    FILENAME:     '{config_filename}'
    FILE SECTION: '{section_name}'

    The database configuration file was located.
    However, either

    1) the specified section could not be found
       within the file, or

    2) it contained invalid information.

    Please open the file and confirm that the
    configuration section exists and contains valid
    values. For more information, review the help
    information located in
        >> help(pcc_030_010_config_parser.config)
    or review the documentation for the standard
    Python 'configparser' module.
**********************************************************

        """
        super().__init__(self.message)


def config(filename="database.ini", section="postgresql"):
    """
    PURPOSE:
        Read a configuration file and parse the information
        needed to connect to a PostgreSQL database server.

    PARAMETERS:
        1) filename:
            * optional
            * Name of the file that contains the DB credentials
              and connection information.

        2) section:
            * optional
            * Name of the file section that contains the
              credential and connection information.

    RETURNS:
        A Python dictionary containing the information needed
        by the 'psycopg2' module to make a connection to a PostgreSQL database.

    OVERVIEW:
      This function performs the following sequence of events.
          1. Check to see if 'filename' exists.

          2. Allocate a new configparser.ConfigParser() object.

          3. Read 'filename' and extract the DB configuration information
             from 'section'. A sample file configuration is shown here.

                [postgresql]
                host=paylocity-db-name.awsservername.us-east-1.rds.amazonaws.com
                port=5432
                database=suppliers
                user=postgres
                password=ASUPERSECRETHARDTOGUESSPASSWORD

            NOTES:
              a) If file section information does not contain an entry for
                 'port', a default value of 5432 will be used to attempt
                  connecting to the database.

              b) The password can contain non-alpha characters such as !@#$%^&.
                 However, if the password does contain '%' characters, each one
                 will have to be escaped by including an extra '%' character.
                 For example, assume that a DB password is 'poqnid$sf%njasdfb'.

                 In the config file, the password line should be written as
                 shown below (notice the %% character).
                    password=poqnid$sf%%njasdfb

                 If the '%' characters in the password are not properly
                 escaped, Python will interpret the '%' characters as
                 formatting characters and either throw an error trying to
                 interpret the sequence or indicate that the DB
                 credentials/connection information is invalid.

            4. Store the parsed information in a Python dictionary object and
               return the object to the function caller.

    """
    if not os.path.exists(filename):
        raise ConfigFileNotFoundError(filename)

    # create a parser
    parser = ConfigParser()

    # read config file
    parser.read(filename)

    # get section, default to postgresql
    pg_db = {}

    if parser.has_section(section):
        params = parser.items(section)

        for param in params:
            pg_db[param[0]] = param[1]

    else:
        raise InvalidConfigSectionError(
            config_filename=filename, section_name=section
        )  # NoQA

    return pg_db


def main():
    """
    Primary purpose is to validate arguments passed via the command line.

    If the command line arguments are valid, then main()
    will call config(). Although config() performs
    validation, too, the extra validation here in main()
    can be useful diagnostically, especially if someone
    is calling this module from the command line.
    """
    NUM_ARGS = len(sys.argv) - 1
    MODULE_NAME = os.path.basename(sys.argv[0])

    def FunctionCallSelector(numargs):
        def args0():
            msg = """

**********************************************************
No command line arguments were furnished. Attempting to
connect to the PostgreSQL DB with the following default
parameters.

  FILENAME: 'database.ini'                    (default)
  SECTION:  'postgresql'                      (default)
**********************************************************

            """
            # print(msg)
            config()

            return msg

        def args1():
            msg = f"""

**********************************************************
One command line argument was given. Attempting to
connect to the PostgreSQL DB with the following parameters.

FILENAME: {sys.argv[1]}
SECTION:  'postgresql'                      (default)
**********************************************************

            """
            # print(msg)
            config(sys.argv[1])
            return msg

        def args2():
            msg = f"""

**********************************************************
Two command line arguments were given. Attempting to
connect to the PostgreSQL DB with the following parameters.

FILENAME: {sys.argv[1]}
SECTION:  {sys.argv[2]}
**********************************************************

            """
            # print(msg)
            config(sys.argv[1], sys.argv[2])
            return msg

        def argsInvalidNum():
            errMsg = f"""

**********************************************************
ERROR: Invalid number of command line args.
**********************************************************
    Module was called with '{numargs}' args,
    but the valid number of arguments is
    0, 1, or 2.

    See
        >> help({MODULE_NAME})
    for more details.
**********************************************************

            """
            raise InvalidNumArgsError(errMsg)

        Switcher = {0: args0, 1: args1, 2: args2}

        return Switcher[numargs]()

    print(FunctionCallSelector(NUM_ARGS))


if __name__ == "__main__":
    print("------------------------------------------------")
    print("------------------------------------------------")
    print("")
    print(f"sys.argv[1]=={sys.argv[1]}")
    print("------------------------------------------------")
    print("------------------------------------------------")
    print("")
    main()
