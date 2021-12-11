-- AUTHOR: Eric MIlgram, PhD
-- 
-- DATE: 08 Dec 2021
--
-- PURPOSE 
-- The purpose of these SQL statements is to properly set up required
-- schemas and tables for the PostgreSQL database used for the
-- Paylocity Coding Challenge.
--
-- ############################################################################
-- Create the 'dev' schema, which is for DB development only
-- ############################################################################
  CREATE SCHEMA dev;

  COMMENT ON SCHEMA dev IS 'The dev schema for Paylocity Coding Challenge developers';

  SET search_path TO dev;
  
  CREATE TABLE IF NOT EXISTS Company
  (
      guid        uuid          PRIMARY KEY,
      name        varchar(50)   NOT NULL UNIQUE,
      status      integer       NOT NULL,
      created     timestamp     NOT NULL DEFAULT NOW()
  );


-- ############################################################################
-- Create the Position table
-- ############################################################################
  CREATE TABLE IF NOT EXISTS Position
  (
      guid        uuid          PRIMARY KEY,
      name        varchar(50)   NOT NULL UNIQUE,
      status      integer       NOT NULL,
      created     timestamp     NOT NULL DEFAULT NOW()
  );

-- ############################################################################
-- Create the Employee table
-- ############################################################################
  CREATE TABLE IF NOT EXISTS Employee
  (
      guid        uuid          PRIMARY KEY,
      state       varchar(50)   NOT NULL,
      status      integer       NOT NULL,
      created     timestamp     NOT NULL DEFAULT NOW()
  );

-- ############################################################################
-- Create the Job table
-- ############################################################################
  CREATE TABLE IF NOT EXISTS Job
  (
      guid              uuid             NOT NULL,
      company_guid      uuid             NOT NULL,
      position_guid     uuid             NOT NULL,
      employee_guid     uuid             NOT NULL,
      created           timestamp        NOT NULL DEFAULT NOW(),
      CONSTRAINT Job_PK                  PRIMARY KEY (guid),
      CONSTRAINT Job_FK_company_guid     FOREIGN KEY (company_guid)  REFERENCES Company  (guid),
      CONSTRAINT Job_FK_position_guid    FOREIGN KEY (position_guid) REFERENCES Position (guid),
      CONSTRAINT Job_FK_employee_guid    FOREIGN KEY (employee_guid) REFERENCES Employee (guid),
      CONSTRAINT Job_unique_comp_pos_emp UNIQUE      (company_guid, position_guid, employee_guid)
  );
  
  COMMENT ON CONSTRAINT Job_unique_comp_pos_emp ON Job
  IS 'Prevent same person from having same job at same company';
