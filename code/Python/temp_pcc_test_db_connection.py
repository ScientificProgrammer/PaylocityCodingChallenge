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
        For example,

            >>> import pcc_030_010_config_parser
            >>> help(pcc_030_010_config_parser)
"""
import sys
import psycopg2
import pcc_030_010_config_parser
from pcc_100_100_helper_functions import ExtractModuleNameFromFileName


def ConnectToPostgreSQLDatabase(
    config_filename="database.ini", config_file_section="postgresql"
):  # noqa: E501
    """
    PURPOSE:
        Test the ability to connect to a PostgreSQL database.

    PARAMETERS:
        1) config_filename (optional):
            * Name of the file that contains the DB credentials
              and connection information.
            * default: database.ini

        2) config_file_section (optional):
            * Name of the file section that contains the
              credential and connection information.
            * default: "postgresql"

    RETURNS: Nothing

    OVERVIEW:
        This function performs the following sequence of events.
            1) Uses the 'pcc_030_010_config_parser.config() function to parse a
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
    dbConn = None

    try:
        # 1) Read DB connection parameters.
        params = pcc_030_010_config_parser.ParseDBConfigFile(
            config_filename, config_file_section  # noqa: E501
        )  # noqa: E501

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


def main():
    MODULE_NAME = ExtractModuleNameFromFileName(__file__)
    NUM_ARGS = len(sys.argv) - 1

    errMsg = (
        f"'{MODULE_NAME}' was called from the command line "
        "with an invalid number of arguments. Aborting."
    )

    # print(f"num_args = {NUM_ARGS}")

    # def CallDBConnector(argc):
    #     def arg0():
    #         ConnectToPostgreSQLDatabase()

    #     def arg1():
    #         ConnectToPostgreSQLDatabase(sys.argv[1])

    #     def arg2():
    #         ConnectToPostgreSQLDatabase(sys.argv[1], sys.argv[2])

    #     def invalidArgs():
    #         raise Exception(errMsg)

    #     Selector = {0: arg0, 1: arg1, 2: arg2}

    #     FuncSel = Selector.get(NUM_ARGS, invalidArgs)

    #     FuncSel()

    # CallDBConnector(NUM_ARGS)

    if NUM_ARGS == 0:
        ConnectToPostgreSQLDatabase()

    elif NUM_ARGS == 1:
        ConnectToPostgreSQLDatabase(sys.argv[1])

    elif NUM_ARGS == 2:
        ConnectToPostgreSQLDatabase(sys.argv[1], sys.argv[2])

    else:
        raise Exception(errMsg)


if __name__ == "__main__":
    main()
