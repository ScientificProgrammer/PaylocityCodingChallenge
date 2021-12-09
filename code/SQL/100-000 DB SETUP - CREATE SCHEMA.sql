-- AUTHOR: Eric MIlgram, PhD
-- 
-- DATE: 08 Dec 2021
--
-- PURPOSE 
-- The purpose of these SQL statements is to properly set up required
-- schemas and roles for the PostgreSQL database used for the
-- Paylocity Coding Challenge.
--
-- This code was adapted from the code posted by Mr. Yaser Raja
-- in a blog post titled "Managing PostgreSQL users and roles," which
-- was published on the "AWS Database Blog" on 04 MAR 2019. The post's
-- permalink is
-- https://aws.amazon.com/blogs/database/managing-postgresql-users-and-roles/

-- ############################################################################
-- Create the Paylocity database
-- NOTE: The steps in this section are not required when using PostgreSQL on
--       AWS RDS.
-- ############################################################################
-- CREATE DATABASE paylocity
-- WITH 
--    OWNER = postgres
--    ENCODING = 'UTF8'
--    LC_COLLATE = 'en_US.UTF-8'
--    LC_CTYPE = 'en_US.UTF-8'
--    TABLESPACE = pg_default
--    CONNECTION LIMIT = -1;

-- SET default_tablespace = pg_default;

-- ############################################################################
-- Create the 'dev' schema, which is for DB development only
-- ############################################################################
   CREATE SCHEMA dev;

   COMMENT ON SCHEMA dev IS 'Schema for developers';

-- ############################################################################
-- REVOKE privileges from 'public' role from public
-- ############################################################################
   REVOKE CREATE ON SCHEMA public FROM PUBLIC;

   REVOKE ALL ON DATABASE paylocity FROM PUBLIC;

-- ############################################################################
-- CREATE Read-only role
-- ############################################################################
   CREATE ROLE readonly;

   GRANT CONNECT ON DATABASE paylocity TO readonly;

   GRANT USAGE ON SCHEMA dev TO readonly;

   GRANT SELECT ON ALL TABLES IN SCHEMA dev TO readonly;

   ALTER DEFAULT PRIVILEGES IN SCHEMA dev
   GRANT SELECT ON TABLES TO readonly;

-- ############################################################################
-- CREATE Read/write role
-- ############################################################################
   CREATE ROLE readwrite;

   GRANT CONNECT ON DATABASE paylocity TO readwrite;

   GRANT USAGE, CREATE ON SCHEMA dev TO readwrite;

   GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA dev TO readwrite;

   ALTER DEFAULT PRIVILEGES IN SCHEMA dev
   GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO readwrite;

   GRANT USAGE ON ALL SEQUENCES IN SCHEMA dev TO readwrite;

   ALTER DEFAULT PRIVILEGES IN SCHEMA dev
   GRANT USAGE ON SEQUENCES TO readwrite;

-- ############################################################################
-- Create users
-- ############################################################################
   CREATE USER reporting_user1 WITH PASSWORD 'reporting_user1CHANGE_ON_FIRST_LOGIN';

   CREATE USER reporting_user2 WITH PASSWORD 'reporting_user2CHANGE_ON_FIRST_LOGIN';

   CREATE USER app_user1 WITH PASSWORD 'CHANGE_ON_FIRST_LOGIN';

   CREATE USER app_user2 WITH PASSWORD 'CHANGE_ON_FIRST_LOGIN';

-- ############################################################################
-- Grant privileges to users
-- ############################################################################
   GRANT readonly TO reporting_user1;

   GRANT readonly TO reporting_user2;

   GRANT readwrite TO app_user1;

   GRANT readwrite TO app_user2;