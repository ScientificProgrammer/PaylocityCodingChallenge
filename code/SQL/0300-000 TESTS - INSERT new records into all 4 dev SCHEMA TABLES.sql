-- AUTHOR: Eric MIlgram, PhD
-- 
-- DATE: 09 Dec 2021
--
-- PURPOSE 
-- The purpose of these SQL statements is to insert record data
-- into the 'company', 'position', 'employee', and 'job' tables in
-- the 'dev' schema for the PostgreSQL database used for the
-- Paylocity Coding Challenge.
--
-- ############################################################################
-- Be sure to set the correct value for the schema.
-- ############################################################################
SET search_path TO dev;

-- ############################################################################
-- Start the transaction before any inserts and only commit it if all
-- inserts work properly.
-- ############################################################################
BEGIN TRANSACTION;

    INSERT INTO Company
      (guid, name, status)
    VALUES
      ('{4c948630-bce9-4aae-ae6d-9898f3539dab}', 'My Test Company 1', 1),
      ('{78bffbd2-c6db-441f-b981-f92813e1791b}', 'My Test Company 2', 1),
      ('{ab447037-2255-4882-826b-56f598baba71}', 'My Test Company 3', 1),
      ('{5a2d1bf8-9367-4f07-9643-64e08dd0e874}', 'My Test Company 4', 1),
      ('{38a41864-38b6-4a28-b742-5f5ecfe6ad17}', 'My Test Company 5', 1);

    INSERT INTO Position
      (guid, name, status)
    VALUES
      ('{0550f13e-76d0-4b8e-99bf-fb3f16429f9b}', 'Data Scientist 1',  1),
      ('{5b22cf08-a93e-4457-a869-203cc1e6370e}', 'Data Scientist 2',  1),
      ('{5781d41f-cc64-469b-aba8-637b0204a096}', 'Data Scientist 3',  1),
      ('{041ce313-3b4e-40ca-bcc7-4ba348a60d85}', 'Business Analyst 1',  1),
      ('{b8121811-ca23-4209-a981-20651ec16200}', 'Business Analyst 2',  1),
      ('{df4e534f-82e7-46b2-be90-5829e26eb5bb}', 'Program Manager 1',  1),
      ('{db7e3090-38bc-49bd-803c-d047be20600c}', 'Program Manager 2',  1),
      ('{7325831e-7701-42d7-87a0-bdc144cf0558}', 'Systems Architect 1',  1),
      ('{e1b37547-5899-46cd-8af5-2bcf421d0a43}', 'Systems Architect 2',  1);

    INSERT INTO Employee
      (guid, state, status)
    VALUES
      ('{1d1ca01f-1ada-4463-817b-79e15ffd9875}', 'NY', 3),
      ('{d0d46dba-e96e-4401-b4d9-d8c8c3e7119e}', 'MN', 1),
      ('{13ef8f03-daa0-46a0-8b66-720ea84bc12f}', 'CA', 1),
      ('{5908c141-12d1-4ff5-9f8f-12c1ef71f430}', 'IA', 3),
      ('{88f9ddd6-cfa1-4201-9268-4c0dcff9c017}', 'LA', 1),
      ('{d9537cf4-02a6-4900-805c-cd214a31a6e8}', 'GA', 3),
      ('{baa94efd-fea0-4065-b0f1-98cd1a74a8bf}', 'CA', 2),
      ('{e6878e0a-a8b9-40cc-b73b-530096c7401d}', 'IL', 2);

    INSERT INTO JOB
      (guid, company_guid, employee_guid)
    VALUES
      ('{75db0af2-ef36-4c9d-a7c1-0549eb3e24e9}', '{78bffbd2-c6db-441f-b981-f92813e1791b}', '{1d1ca01f-1ada-4463-817b-79e15ffd9875}'),
      ('{2ee639aa-035a-4dfe-a3ed-e11d5a4b6a30}', '{4c948630-bce9-4aae-ae6d-9898f3539dab}', '{d0d46dba-e96e-4401-b4d9-d8c8c3e7119e}'),
      ('{adc12833-475e-4027-8fe8-d7845381b867}', '{4c948630-bce9-4aae-ae6d-9898f3539dab}', '{13ef8f03-daa0-46a0-8b66-720ea84bc12f}'),
      ('{caa7ba66-f120-45fb-808f-2e0e16aae2bc}', '{4c948630-bce9-4aae-ae6d-9898f3539dab}', '{5908c141-12d1-4ff5-9f8f-12c1ef71f430}'),
      ('{5f6cdd10-de9c-430a-9143-45b79eba7e44}', '{5a2d1bf8-9367-4f07-9643-64e08dd0e874}', '{88f9ddd6-cfa1-4201-9268-4c0dcff9c017}'),
      ('{9347dea5-fcfa-48e1-8efd-af486d0fe575}', '{78bffbd2-c6db-441f-b981-f92813e1791b}', '{d9537cf4-02a6-4900-805c-cd214a31a6e8}'),
      ('{f36be466-2b5b-4404-a864-8de1dea27f10}', '{38a41864-38b6-4a28-b742-5f5ecfe6ad17}', '{baa94efd-fea0-4065-b0f1-98cd1a74a8bf}'),
      ('{240fecb7-b6eb-4f33-b526-ba65cc097c43}', '{78bffbd2-c6db-441f-b981-f92813e1791b}', '{e6878e0a-a8b9-40cc-b73b-530096c7401d}');

COMMIT TRANSACTION;