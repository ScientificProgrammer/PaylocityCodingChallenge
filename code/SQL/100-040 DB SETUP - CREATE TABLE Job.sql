-- ############################################################################
-- Create the paylocity.dev.Job table
-- ############################################################################
   DROP TABLE IF EXISTS paylocity.dev.Job CASCADE;

   CREATE TABLE IF NOT EXISTS paylocity.dev.Job
   (
       guid          uuid   PRIMARY KEY,
       company_guid  uuid   NOT NULL,
       position_guid uuid   NOT NULL,
       employee_guid uuid   NOT NULL,
       FOREIGN KEY (company_guid)  REFERENCES paylocity.dev.Company  (guid),
       FOREIGN KEY (position_guid) REFERENCES paylocity.dev.Position (guid),
       FOREIGN KEY (employee_guid) REFERENCES paylocity.dev.Employee (guid),
       UNIQUE (company_guid, employee_guid)
   );