-- ############################################################################
-- Create the Position table
-- ############################################################################
   DROP TABLE IF EXISTS paylocity.dev.Position CASCADE;

   CREATE TABLE IF NOT EXISTS paylocity.dev.Position
   (
       guid        uuid          PRIMARY KEY,
       name        varchar(50)   NOT NULL UNIQUE,
       status      integer       NOT NULL
   );