-- ############################################################################
-- Create the Employee table
-- ############################################################################
   DROP TABLE IF EXISTS paylocity.dev.Employee CASCADE;

   CREATE TABLE IF NOT EXISTS paylocity.dev.Employee
   (
       guid        uuid          PRIMARY KEY,
       state       varchar(50)   NOT NULL,
       status      integer       NOT NULL
   );