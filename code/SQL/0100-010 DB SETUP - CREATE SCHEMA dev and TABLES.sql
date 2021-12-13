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

-- ############################################################################
-- Create the company table
-- ############################################################################
  
  CREATE TABLE company
  (
      guid        uuid          PRIMARY KEY,
      name        varchar(50)   NOT NULL UNIQUE,
      status      integer       NOT NULL,
      created     timestamp     NOT NULL DEFAULT NOW()
  );


-- ############################################################################
-- Create the position table
-- ############################################################################
  CREATE TABLE position
  (
      guid        uuid          PRIMARY KEY,
      name        varchar(50)   NOT NULL UNIQUE,
      status      integer       NOT NULL,
      created     timestamp     NOT NULL DEFAULT NOW()
  );

-- ############################################################################
-- Create the employee table
-- ############################################################################
  CREATE TABLE employee
  (
      guid        uuid          PRIMARY KEY,
      state       varchar(50)   NOT NULL,
      status      integer       NOT NULL,
      created     timestamp     NOT NULL DEFAULT NOW()
  );

-- ############################################################################
-- Create the job table
-- ############################################################################
  CREATE TABLE job
  (
      guid              uuid             NOT NULL,
      company_guid      uuid             NOT NULL,
      employee_guid     uuid             NOT NULL,
      created           timestamp        NOT NULL DEFAULT NOW(),
      CONSTRAINT job_PK                  PRIMARY KEY (guid),
      CONSTRAINT job_FK_company_guid     FOREIGN KEY (company_guid)  REFERENCES company  (guid),
      CONSTRAINT job_FK_employee_guid    FOREIGN KEY (employee_guid) REFERENCES employee (guid),
      CONSTRAINT job_unique_comp_emp UNIQUE      (company_guid, employee_guid)
  );
  
  COMMENT ON CONSTRAINT job_unique_comp_emp ON job
  IS 'Prevent same person from having same job at same company';
