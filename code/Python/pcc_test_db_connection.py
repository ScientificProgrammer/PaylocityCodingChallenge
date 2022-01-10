"""
  This module is used to test connectivity to a PostgreSQL database.

  AUTHOR:        Eric Milgram, PhD

  APPLICATION:   Paylocity Coding Challenge

  DEPENDENCIES:  1) psycopg2
                        This package does the heavy lifting for connecting to a
                        PostgreSQL database server. For more details about how
                        to install 'psycopg2' for your specific implementation,
                        visit the following URL.
                          https://pypi.org/project/psycopg2/

                  2) pcc_config_parser.py
                        This module was developed specifically for this
                        project. Essentially, it is a wrapper for base Python's
                        configparser.ConfigParser.

                        Note that this module requires a valid database
                        configuration file, which contains the essential
                        information needed to make a connection to a PostgreSQL
                        database, such as the URI of the database, the port on
                        which the database is running, and the user credentials
                        for the database.

                        For more information about using this module and
                        creating the database configuration file, see the help
                        documentation, which can be accessed via Python's
                        standard help interface (after importing the module).
                        For example,

                          >>> import pcc_config_parser
                          >>> help(pcc_config_parser)
"""

# import os.path
import sys
import psycopg2
from pcc_config_parser import config
from pathlib import PurePath


class pcc_custom_error(Exception):
    """
    Base class for derived Exception classes used in this module.
    """

    pass


class pcc_invalid_num_cmd_line_args_error(pcc_custom_error):
    """
    Thrown when this module is called directly with an invalid number
    of command line arguments.
    """

    pass


def connect(configfilename="database.ini", configfilesection="postgresql"):
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

            1) Uses the 'pcc_config_parser.config() function to parse a
               configuration file containing the security credentials
               needed to connect to a PostgreSQL database.

            2) Use the credentials to make the connection to the database.

            3) From the db connection object, request a database cursor and
               save it.

            4) Use the database cursor to execute a single 'SELECT version()'
               statement.

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
        print("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(**params)

        # 3) Create a database cursor.
        cur = conn.cursor()

        # 4) Execute a single SELECT statement.
        print(
            """
**********************************************************************
*  SUCCESS! Connected to the database server. Retrieving DB version  *
**********************************************************************
PostgreSQL database version information:
            """
        )
        cur.execute("SELECT version()")

        # 5) Display the PostgreSQL database server version.
        db_version = cur.fetchone()

        print(
            f"""
********************************************************************
{db_version}
********************************************************************
            """
        )

        # 6) Close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        # 7) Close the database connection.
        if conn is not None:
            conn.close()
            print("Database connection closed.\n")
    # ************************** END connect() **************************


def main():
    MODULE_NAME = PurePath(sys.argv[0]).stem

    num_args = len(sys.argv) - 1

    print(f"num_args = {num_args}")

    # def connect_to_db(nargs):
    #   def connect_db_zero_args():
    #     msg = """
    #       ------------------------------------------------------------------------------
    #         No command line arguments were furnished. Attempting to connect
    #         to the PostgreSQL DB with the following default parameters.

    #             FILENAME: 'database.ini'                    (default)
    #             SECTION:  'postgresql'                      (default)
    #       ------------------------------------------------------------------------------
    #     """
    #     connect()
    #     return(msg)

    #   def connect_db_one_arg():
    #     msg = """
    #       ------------------------------------------------------------------------------
    #         One command line argument was given. Attempting to connect to the
    #         PostgreSQL DB with the following parameters.

    #           FILENAME: {0}
    #           SECTION:  'postgresql'                      (default)
    #       ------------------------------------------------------------------------------
    #     """.format(sys.argv[1])
    #     connect(sys.argv[1])
    #     return(msg)

    #   def connect_db_two_args():
    #     msg = """
    #       ------------------------------------------------------------------------------
    #         One command line argument was given. Attempting to connect to the
    #         PostgreSQL DB with the following parameters.

    #           FILENAME: {0}
    #           SECTION:  'postgresql'                      (default)
    #       ------------------------------------------------------------------------------
    #     """.format(sys.argv[1])
    #     connect(sys.argv[1])
    #     return(msg)

    #   def connect_db_invalid_num_args()
    #       ------------------------------------------------------------------------------
    #     """.format(MODULE_NAME)
    #     raise pcc_invalid_num_cmd_line_args_error(err_msg)

    #   switcher = {
    #     0: connect_db_zero_args(),
    #     1: connect_db_one_arg(),

    help_msg = f"""
For more information about using this module, see help({MODULE_NAME})
    """
    print(help_msg)

    # print("num_args == {0}".format(num_args))

    # output_msg = connect_to_db(num_args)

    # print(output_msg)


#   assert num_args >= 0 and num_args <= 2, f"""
# ERROR: Invalid number of args passed to {__name__} in module {MODULE_NAME}
#   """

#   print(process_args(num_args))

#   assert(False == True), "For debugging only. Delete from production."

#   if num_args == 0:
#     msg = """
# ------------------------------------------------------------------------------
#   No command line arguments were furnished. Attempting to connect
#   to the PostgreSQL DB with the following default parameters.

#       FILENAME: 'database.ini'                    (default)
#       SECTION:  'postgresql'                      (default)
# ------------------------------------------------------------------------------
#       """
#     print(msg)
#     connect()

#   elif num_args == 1:
#     msg = """
# ------------------------------------------------------------------------------
#   One command line argument was given. Attempting to connect to the
#   PostgreSQL DB with the following parameters.

#     FILENAME: {0}
#     SECTION:  'postgresql'                      (default)
# ------------------------------------------------------------------------------
#       """.format(sys.argv[1])
#     print(msg)
#     connect(sys.argv[1])

#   elif num_args == 2:
#     msg = """
# ------------------------------------------------------------------------------
#   One command line argument was given. Attempting to connect to the
#   PostgreSQL DB with the following parameters.

#     FILENAME: {0}
#     SECTION:  {1}
# ------------------------------------------------------------------------------
#       """.format(sys.argv[1], sys.argv[2])
#     print(msg)
#     connect(sys.argv[1], sys.argv[2])

# ------------------------------------------------------------------------------
#     """.format(MODULE_NAME)
#     raise pcc_invalid_num_cmd_line_args_error(err_msg)

# *******************************************************************
# End main()                                                        *
# *******************************************************************
