library(tibble)
library(dplyr)

jobs_guids <- c(
  "75db0af2-ef36-4c9d-a7c1-0549eb3e24e9",
  "2ee639aa-035a-4dfe-a3ed-e11d5a4b6a30",
  "adc12833-475e-4027-8fe8-d7845381b867",
  "caa7ba66-f120-45fb-808f-2e0e16aae2bc",
  "5f6cdd10-de9c-430a-9143-45b79eba7e44",
  "9347dea5-fcfa-48e1-8efd-af486d0fe575",
  "f36be466-2b5b-4404-a864-8de1dea27f10",
  "240fecb7-b6eb-4f33-b526-ba65cc097c43"
)

employee_guids <- c(
  "1d1ca01f-1ada-4463-817b-79e15ffd9875",
  "d0d46dba-e96e-4401-b4d9-d8c8c3e7119e",
  "13ef8f03-daa0-46a0-8b66-720ea84bc12f",
  "5908c141-12d1-4ff5-9f8f-12c1ef71f430",
  "88f9ddd6-cfa1-4201-9268-4c0dcff9c017",
  "d9537cf4-02a6-4900-805c-cd214a31a6e8",
  "baa94efd-fea0-4065-b0f1-98cd1a74a8bf",
  "e6878e0a-a8b9-40cc-b73b-530096c7401d"
)

position_guids <- c(
  "0550f13e-76d0-4b8e-99bf-fb3f16429f9b",
  "5b22cf08-a93e-4457-a869-203cc1e6370e",
  "5781d41f-cc64-469b-aba8-637b0204a096",
  "041ce313-3b4e-40ca-bcc7-4ba348a60d85",
  "b8121811-ca23-4209-a981-20651ec16200",
  "df4e534f-82e7-46b2-be90-5829e26eb5bb",
  "db7e3090-38bc-49bd-803c-d047be20600c",
  "7325831e-7701-42d7-87a0-bdc144cf0558",
  "e1b37547-5899-46cd-8af5-2bcf421d0a43"
)

company_guids <- c(
  "4c948630-bce9-4aae-ae6d-9898f3539dab",
  "78bffbd2-c6db-441f-b981-f92813e1791b",
  "ab447037-2255-4882-826b-56f598baba71",
  "5a2d1bf8-9367-4f07-9643-64e08dd0e874",
  "38a41864-38b6-4a28-b742-5f5ecfe6ad17"
)

lst_comp_pos_guids <- list(
  company_guid = company_guids,
  position_guid = position_guids
)

tib_all_comp_pos_guids <- as_tibble(
  expand.grid(
    lst_comp_pos_guids,
    stringsAsFactors = FALSE,
    KEEP.OUT.ATTRS = FALSE
  )
)

jobs <- tibble(
  guid = jobs_guids,
  company_guid = character(length(employee_guids)),
  position_guid = character(length(employee_guids)),
  employee_guid = employee_guids
)

set.seed(10852)

tib_rand_comp_pos_combos <- slice_sample(
  tib_all_comp_pos_guids,
  n = nrow(jobs),
  replace = TRUE
)

jobs$company_guid <- tib_rand_comp_pos_combos$company_guid
jobs$position_guid <- tib_rand_comp_pos_combos$position_guid

write.csv(as.data.frame(jobs), "clipboard", row.names = FALSE)

