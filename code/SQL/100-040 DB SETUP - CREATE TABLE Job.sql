-- ############################################################################
-- Create the paylocity.dev.Job table
-- ############################################################################
   DROP TABLE IF EXISTS paylocity.dev.Job CASCADE;

   CREATE TABLE IF NOT EXISTS paylocity.dev.Job
   (
       guid              uuid     NOT NULL,
       company_guid      uuid     NOT NULL,
       position_guid     uuid     NOT NULL,
       employee_guid     uuid     NOT NULL,
       CONSTRAINT Job_PK                  PRIMARY KEY (guid),
       CONSTRAINT Job_FK_company_guid     FOREIGN KEY (company_guid)  REFERENCES paylocity.dev.Company  (guid),
       CONSTRAINT Job_FK_position_guid    FOREIGN KEY (position_guid) REFERENCES paylocity.dev.Position (guid),
       CONSTRAINT Job_FK_employee_guid    FOREIGN KEY (employee_guid) REFERENCES paylocity.dev.Employee (guid),
       CONSTRAINT Job_unique_comp_pos_emp UNIQUE      (company_guid, position_guid, employee_guid)
   );
   
   COMMENT ON CONSTRAINT Job_unique_comp_pos_emp ON paylocity.dev.Job
   IS 'Prevent same person from having same job at same company';