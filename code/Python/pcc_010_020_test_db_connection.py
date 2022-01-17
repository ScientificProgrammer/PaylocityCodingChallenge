"""
  This module is used to test connectivity to a PostgreSQL database.

  AUTHOR:        Eric Milgram, PhD

  APPLICATION:   Paylocity Coding Challenge

  DEPENDENCIES:
1) psycopg2
        This package does the heavy lifting for connecting to a
        PostgreSQL database server. For more details about how to
        install 'psycopg2' for your specific implementation, visit
        the following URL.
            https://pypi.org/project/psycopg2/

2) pcc_030_010_config_parser
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
"""
import os.path
import sys
import psycopg2
import pcc_030_010_config_parser

__all__ = ["ConnectToPostgreSQLDatabase"]


def ConnectToPostgreSQLDatabase(
    config_filename: str = "database.ini",
    config_file_section: str = "postgresql",
) -> None:
    """
    PURPOSE:
        Test the ability to connect to a PostgreSQL database.

    PARAMETERS:
        1) config_filename (optional):
            a) Name of the file that contains the DB credentials
              and connection information.

            b) default: 'database.ini'

        2) config_file_section (optional):
            a) Name of the file section that contains the
              credential and connection information.

            b) default: 'postgresql'

    RETURNS: Nothing

    OVERVIEW:
    This function performs the following sequence of events.
        1)  Uses the 'pcc_030_010_config_parser.ParseDBConfigFile()
            function to parse a configuration file containing the
            security credentials needed to connect to a PostgreSQL
            database.

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
    dbConn = None

    try:
        # 1) Read DB connection parameters.
        params = pcc_030_010_config_parser.ParseDBConfigFile(
            config_filename, config_file_section
        )

        # 2) Connect to the PostgreSQL server.
        print("Connecting to the PostgreSQL database...")
        dbConn = psycopg2.connect(**params)

        # 3) Create a database cursor.
        dbCur = dbConn.cursor()

        # 4) Execute a single SELECT statement.
        print(
            """

****************************************************************
*  SUCCESS! Connected to the db server. Retrieving DB version  *
****************************************************************
PostgreSQL database version information:
"""
        )
        dbCur.execute("SELECT version()")

        # 5) Display the PostgreSQL database server version.
        dbVerStr = dbCur.fetchone()

        print(f"{dbVerStr}\n")

        # 6) Close the communication with the PostgreSQL
        dbCur.close()

    except psycopg2.DatabaseError as DBError:
        print(DBError)

    finally:
        # 7) Close the database connection.
        if dbConn is not None:
            dbConn.close()
            print("Database connection closed.\n")
    # ************************** END connect() **************************


def _main():
    NUM_ARGS = len(sys.argv) - 1
    MODULE_NAME = os.path.basename(sys.argv[0])

    print(f"num_args = {NUM_ARGS}")

    if NUM_ARGS == 0:
        msg = """
**********************************************************
No command line arguments were furnished. Attempting to
connect to the PostgreSQL DB with the following default
parameters.

  FILENAME: 'database.ini'                    (default)
  SECTION:  'postgresql'                      (default)
**********************************************************
        """
        print(msg)
        ConnectToPostgreSQLDatabase()

    elif NUM_ARGS == 1:
        msg = f"""
**********************************************************
One command line argument was given. Attempting to
connect to the PostgreSQL DB with the following parameters.

FILENAME: {sys.argv[1]}
SECTION:  'postgresql'                      (default)
**********************************************************
        """
        print(msg)
        ConnectToPostgreSQLDatabase(sys.argv[1])

    elif NUM_ARGS == 2:
        msg = f"""
**********************************************************
Two command line arguments were given. Attempting to
connect to the PostgreSQL DB with the following parameters.

FILENAME: {sys.argv[1]}
SECTION:  {sys.argv[2]}
**********************************************************
"""
        print(msg)
        ConnectToPostgreSQLDatabase(sys.argv[1], sys.argv[2])

    else:
        errMsg = f"""

**********************************************************
ERROR: Invalid number of command line args.
**********************************************************
    Module was called with '{NUM_ARGS}' args,
    but the valid number of arguments is
    0, 1, or 2.

    See
        >> help({MODULE_NAME})
    for more details.
**********************************************************

"""
        raise Exception(errMsg)


if __name__ == "__main__":
    _main()
