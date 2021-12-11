-- AUTHOR: Eric MIlgram, PhD
-- 
-- DATE: 09 Dec 2021
--
-- PURPOSE 
-- The purpose of these SQL statements is to create the pccdev ROLE
-- for the PostgreSQL database used for the Paylocity Coding Challenge.
--
-- ############################################################################
-- Create the 'dev' schema, which is for DB development only
-- ############################################################################

-- ############################################################################
-- CREATE pccdev ROLE, then GRANT the ROLE permission to connect to the DB.
-- ############################################################################
  CREATE ROLE pccdev;

  GRANT CONNECT
  ON DATABASE paylocity
  TO pccdev;

-- ############################################################################
-- GRANT the pccdev ROLE the necessary permissions for
-- using the 'dev' SCHEMA.
-- ############################################################################
  GRANT USAGE, CREATE
  ON SCHEMA dev
  TO pccdev;

  GRANT
  ALL PRIVILEGES
  ON ALL TABLES
  IN SCHEMA dev
  TO pccdev;
  
  ALTER DEFAULT PRIVILEGES
  IN SCHEMA dev
  GRANT ALL PRIVILEGES
  ON TABLES
  TO pccdev;

  GRANT USAGE
  ON ALL SEQUENCES
  IN SCHEMA dev
  TO pccdev;

  ALTER DEFAULT PRIVILEGES
  IN SCHEMA dev
  GRANT USAGE
  ON SEQUENCES
  TO pccdev;