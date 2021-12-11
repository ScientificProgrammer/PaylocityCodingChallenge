-- AUTHOR: Eric MIlgram, PhD
-- 
-- DATE: 09 Dec 2021
--
-- PURPOSE 
-- The purpose of these SQL statements is to create a developer user
-- for the PostgreSQL database used for the Paylocity Coding Challenge.
--
-- ############################################################################
-- Create the 'dev' schema, which is for DB development only
-- ############################################################################
-- ############################################################################
-- Create the first user of the 'dev' schema.
-- ############################################################################
  CREATE USER emilgram WITH PASSWORD 'CHANGE_ON_FIRST_LOGIN';

-- ############################################################################
-- Grant privileges to users
-- ############################################################################
  GRANT pccdev TO emilgram;

  ALTER ROLE emilgram
  IN DATABASE paylocity
  SET search_path TO dev;

-- ############################################################################
-- CREATE Table: Company
-- ############################################################################
  SET SCHEMA 'dev';