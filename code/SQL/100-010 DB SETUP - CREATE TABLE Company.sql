-- ############################################################################
-- CREATE Table: paylocity.dev.Company
-- ############################################################################
   DROP TABLE IF EXISTS paylocity.dev.Company CASCADE;
   
   CREATE TABLE IF NOT EXISTS paylocity.dev.Company
   (
       guid        uuid          PRIMARY KEY,
       name        varchar(50)   NOT NULL UNIQUE,
       status      integer       NOT NULL
   );