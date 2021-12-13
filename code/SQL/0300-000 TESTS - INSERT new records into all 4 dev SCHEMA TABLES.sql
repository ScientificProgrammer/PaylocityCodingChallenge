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

INSERT INTO company
  (guid, name, status)
VALUES
  ('{089a7eef-11b6-45e5-aca0-8b4b17a11d73}', 'Company Name 1', 2),
  ('{855afa01-da1e-4b0c-abf6-d9c1f6a45366}', 'Company Name 2', 1),
  ('{526acbbe-8b3f-4d9a-98ec-ce3177d6eb81}', 'Company Name 3', 1),
  ('{8c54bd20-01d9-495c-9902-45db8d20cffb}', 'Company Name 4', 1),
  ('{07891a33-08c5-46e5-95b8-50db0476bcc5}', 'Company Name 5', 3),
  ('{44a6a889-be1f-410a-9ce7-d03472c5ef09}', 'Company Name 6', 1),
  ('{df638ca0-4043-421f-b24e-a356c0cc363b}', 'Company Name 7', 3),
  ('{11eb173b-a047-4428-accb-962b2850ce09}', 'Company Name 8', 3);

INSERT INTO position
  (guid, name, status)
VALUES
  ('998ecaa7-c85d-47a1-a732-5dff6e73a4e6', 'Position 1', 1),
  ('ac750d9c-b52b-4a1d-bbad-3021734a6c9d', 'Position 2', 2),
  ('24da000e-ffab-4c81-8781-a30e63140ef5', 'Position 3', 2),
  ('0b9d6dce-8ee3-4ecc-83be-8fad937df5c4', 'Position 4', 3),
  ('87258240-f2b5-4a59-b3ad-e07900c8349d', 'Position 5', 1),
  ('b7e3a605-320f-4e6d-bc51-6e4b9fd1c53d', 'Position 6', 3),
  ('2e4e513a-b001-4043-af78-b29017e5f0c5', 'Position 7', 2),
  ('1d1957f0-efc0-461a-80a4-eece7b11d7b5', 'Position 8', 1),
  ('dfd5b9db-c698-42a0-b0a0-0a41d9b0394d', 'Position 9', 1),
  ('367aff20-163c-46d4-9da8-1a98c4cb6315', 'Position 10', 2),
  ('29e4e4d5-a2bb-431b-8bfa-db8914f90a7d', 'Position 11', 1),
  ('62eaf078-a323-48c8-8128-6a6dc35e5da4', 'Position 12', 3),
  ('f77d8883-cab5-481f-bc12-d4ccf1484f0f', 'Position 13', 3),
  ('9402b39d-336e-47c8-b452-b8e69e352b4b', 'Position 14', 1),
  ('0338f3ca-7cf8-4809-a37b-61f2fb8cb0a9', 'Position 15', 1),
  ('56a9d707-aa62-478a-a153-c309430393a4', 'Position 16', 2),
  ('9ca305da-9b3e-4007-92ca-e27bf244472d', 'Position 17', 1),
  ('47aa1d8b-4aeb-4f3c-a34e-9855b075b494', 'Position 18', 2),
  ('721881a6-d22e-4a9e-82c2-19f0083bcb3f', 'Position 19', 2),
  ('fd65efbc-1a52-4f09-8f2f-f47f753b29f0', 'Position 20', 3),
  ('1087824d-7ed4-41f9-aa90-56058130bba7', 'Position 21', 1),
  ('9bad83cf-2a36-4c0a-a085-69b86e579c13', 'Position 22', 3),
  ('271612c9-68a5-4d36-95c8-32d5d21d4f3c', 'Position 23', 1),
  ('43825b53-298c-456a-87d9-14bd9fa8e482', 'Position 24', 3),
  ('7ede7f3e-afbd-4942-b1ca-b0d28da89fb7', 'Position 25', 3),
  ('dc2276a3-1445-4a42-beb7-e79ac4aad31b', 'Position 26', 2),
  ('a561241a-193e-41ab-9940-71ecd9af4b1a', 'Position 27', 2),
  ('f6868964-206b-4e55-81d7-f9ba7ae2796f', 'Position 28', 2),
  ('ac689b79-4e90-49e7-8eab-140795a865ef', 'Position 29', 3),
  ('dd2a7940-df64-4e35-be7b-a05c9f2122ee', 'Position 30', 3),
  ('d601af9f-810d-43b8-a6f5-a2d7332e44cf', 'Position 31', 2),
  ('a8f97fc0-e69a-4899-a324-39193f264274', 'Position 32', 2),
  ('36f67e37-13ee-46c8-8842-e8cf6a36d599', 'Position 33', 3);

INSERT INTO employee
  (guid, state, status)
VALUES
  ('{ff5cf501-92d9-4acd-b720-508d834fcdd9}', 'FL', 3),
  ('{b29d98a9-fb44-47a9-b877-2a23d82e88a2}', 'FL', 1),
  ('{aaa63040-ee5c-4516-855f-66c95dbbefc4}', 'TX', 1),
  ('{75ccba66-e628-4eea-ab8d-a288174220cc}', 'NY', 2),
  ('{cebb8031-44ff-4da8-afe5-94896c4dd032}', 'CA', 3),
  ('{ca1ef153-55d0-4029-8ddf-2f86ab1c4ab8}', 'NY', 2),
  ('{26500ce5-6d8b-408c-9a73-c63943d523c1}', 'CA', 2),
  ('{9a0d6b05-2d16-46c2-8654-a020ed8c2017}', 'CA', 1),
  ('{8590597a-00e4-49a1-9fa6-7f42019b397e}', 'CA', 1),
  ('{f85b0443-a413-451e-b8e3-19d674c73761}', 'FL', 3),
  ('{b17e6022-424e-44bf-8136-5c344b3a5a75}', 'CA', 1),
  ('{da0e7882-702f-419a-a43e-18e5d0373478}', 'FL', 3),
  ('{02b92af1-64de-4998-a1d6-41fee4643ce2}', 'NY', 1),
  ('{6d7ecb2d-506c-4ca6-b09c-255534b0dd7a}', 'FL', 2),
  ('{59a1f4f4-bb0f-4b3a-9d57-da9caa8172be}', 'CA', 1),
  ('{e7904964-c8dd-4689-8533-88d8da05a790}', 'CA', 1),
  ('{8bd61b0e-77eb-4bd5-af4a-13f2d0dcfd8e}', 'NY', 2),
  ('{a432df2f-0940-469b-abdf-ec09949e311e}', 'TX', 2),
  ('{a5470a6d-783a-41f1-a92d-93975673a9c9}', 'FL', 1),
  ('{f8abd993-59bf-43c7-9e3f-a7be9ceb1fae}', 'CA', 3);

INSERT INTO job
  (guid, company_guid, employee_guid)
VALUES
  ('{b0aaa752-b9e3-41f9-a226-e9acdd994769}', '{11eb173b-a047-4428-accb-962b2850ce09}', '{ff5cf501-92d9-4acd-b720-508d834fcdd9}'),
  ('{d1b7ab40-2e29-4213-9c76-0b3675572def}', '{11eb173b-a047-4428-accb-962b2850ce09}', '{b29d98a9-fb44-47a9-b877-2a23d82e88a2}'),
  ('{9053d1e7-58e8-4109-b10f-3a4fd336d592}', '{07891a33-08c5-46e5-95b8-50db0476bcc5}', '{aaa63040-ee5c-4516-855f-66c95dbbefc4}'),
  ('{f6e5cb23-36c0-4012-9b2d-c6432cfafd00}', '{089a7eef-11b6-45e5-aca0-8b4b17a11d73}', '{75ccba66-e628-4eea-ab8d-a288174220cc}'),
  ('{879c523f-62fa-4ba8-ad4b-4f4e12022d87}', '{07891a33-08c5-46e5-95b8-50db0476bcc5}', '{cebb8031-44ff-4da8-afe5-94896c4dd032}'),
  ('{47d0fb10-8031-4f1d-bd6e-5b7ea44f53ed}', '{855afa01-da1e-4b0c-abf6-d9c1f6a45366}', '{ca1ef153-55d0-4029-8ddf-2f86ab1c4ab8}'),
  ('{0cf296f4-88b4-4aef-b403-72f705affacd}', '{8c54bd20-01d9-495c-9902-45db8d20cffb}', '{26500ce5-6d8b-408c-9a73-c63943d523c1}'),
  ('{81eb16a5-df15-4641-88f5-a69eed7dbe49}', '{44a6a889-be1f-410a-9ce7-d03472c5ef09}', '{9a0d6b05-2d16-46c2-8654-a020ed8c2017}'),
  ('{6f77debf-76b8-459a-90af-fbc9943c2182}', '{df638ca0-4043-421f-b24e-a356c0cc363b}', '{8590597a-00e4-49a1-9fa6-7f42019b397e}'),
  ('{58bffa18-843d-44af-aeb0-b64d2db79b94}', '{11eb173b-a047-4428-accb-962b2850ce09}', '{f85b0443-a413-451e-b8e3-19d674c73761}'),
  ('{451b4a94-7417-4666-9ab6-753e9dcbea11}', '{089a7eef-11b6-45e5-aca0-8b4b17a11d73}', '{b17e6022-424e-44bf-8136-5c344b3a5a75}'),
  ('{50e28cc8-8969-453e-aef3-d0853f8dc1c3}', '{089a7eef-11b6-45e5-aca0-8b4b17a11d73}', '{da0e7882-702f-419a-a43e-18e5d0373478}'),
  ('{06e26306-85c2-43e5-9888-8f88fdf16ca3}', '{44a6a889-be1f-410a-9ce7-d03472c5ef09}', '{02b92af1-64de-4998-a1d6-41fee4643ce2}'),
  ('{4c436d85-7715-4ffa-9bf1-38a65511f3a4}', '{44a6a889-be1f-410a-9ce7-d03472c5ef09}', '{6d7ecb2d-506c-4ca6-b09c-255534b0dd7a}'),
  ('{525aeaf4-f69d-4494-b2d4-2f4cdd4fd712}', '{df638ca0-4043-421f-b24e-a356c0cc363b}', '{59a1f4f4-bb0f-4b3a-9d57-da9caa8172be}'),
  ('{f9be1237-59fb-4510-ac18-1eb4e3f4bbec}', '{df638ca0-4043-421f-b24e-a356c0cc363b}', '{e7904964-c8dd-4689-8533-88d8da05a790}'),
  ('{bf7a3c0d-a01b-4e8b-88fd-611ba27c866a}', '{44a6a889-be1f-410a-9ce7-d03472c5ef09}', '{8bd61b0e-77eb-4bd5-af4a-13f2d0dcfd8e}'),
  ('{17f1c55b-1e8d-47c4-b480-65c22d8825e5}', '{089a7eef-11b6-45e5-aca0-8b4b17a11d73}', '{a432df2f-0940-469b-abdf-ec09949e311e}'),
  ('{f196a006-8e70-451e-9a72-be86a5c73cbd}', '{11eb173b-a047-4428-accb-962b2850ce09}', '{a5470a6d-783a-41f1-a92d-93975673a9c9}'),
  ('{53ad30e2-8ff6-4b1c-98db-5e9f2147b974}', '{07891a33-08c5-46e5-95b8-50db0476bcc5}', '{f8abd993-59bf-43c7-9e3f-a7be9ceb1fae}');

COMMIT TRANSACTION;