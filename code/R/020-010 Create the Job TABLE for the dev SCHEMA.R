library(uuid)
library(tibble)
library(dplyr)
library(here)

N_JOB_UUIDS      <- 20                       # N_JOB_UUIDS must equal N_EMPLOYEE_UUIDS
N_EMPLOYEE_UUIDS <- N_JOB_UUIDS              # because of the data model constraints
N_COMPANY_UUIDS  <- 8
N_POSITION_UUIDS <- N_JOB_UUIDS + 13

jobs_guids      <- UUIDgenerate(n = N_JOB_UUIDS)
employee_guids  <- UUIDgenerate(n = N_EMPLOYEE_UUIDS)
company_guids   <- UUIDgenerate(n = N_COMPANY_UUIDS)
position_guids  <- UUIDgenerate(n = N_POSITION_UUIDS)

# #######################################################
# Build the employees table
# #######################################################
employees <- tibble(
  guid = employee_guids,
  state = sample(
    c("CA", "FL", "NY", "TX"),
    length(employee_guids),
    replace = TRUE),
  status = sample(
    1:3,
    length(employee_guids),
    replace = TRUE)
)

employees1 <- employees %>% 
  mutate(guid = paste0("{", guid, "}", sep = ""))

write.csv(as.data.frame(employees1), here("./data/employees.csv"), row.names = FALSE)

# #######################################################
# Build the jobs table
# #######################################################
jobs <- tibble(
  guid = jobs_guids,
    company_guid = sample(
    company_guids,
    size = N_JOB_UUIDS,
    replace = TRUE
  ),
  employee_guid = employee_guids
)

jobs1 <- jobs %>%
  mutate_all(~ paste0("{", ., "}", sep = ""))

write.csv(as.data.frame(jobs1), here("./data/jobs.csv"), row.names = FALSE)

# #######################################################
# Build the companies table
# #######################################################
companies <- tibble(
  guid = company_guids
)

companies$name <- paste("Company Name", 1:nrow(companies))

companies$status <- sample(1:3, nrow(companies), replace = TRUE)

companies1 <- companies %>% 
  mutate(guid = paste0("{", guid, "}", sep = ""))

write.csv(as.data.frame(companies1), here("./data/companies.csv"), row.names = FALSE)

# #######################################################
# Build the positions table
# #######################################################
positions <- tibble(
  guid = position_guids
)

positions$name <- paste("Position", 1:nrow(positions))

positions$status <- sample(1:3, nrow(positions), replace = TRUE)

positions1 <- positions %>% 
  mutate(guid = paste0("{", guid, "}", sep = ""))

write.csv(as.data.frame(positions), here("./data/positions.csv"), row.names = FALSE)
