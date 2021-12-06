# Adapted from
# https://github.com/r-dbi/RPostgres#basic-usage

library(DBI)
library(RPostgres)

# Connect to a specific postgres database
con <- dbConnect(
  drv      = RPostgres::Postgres(),
  dbname   = 'paylocity',
  host     = 'paylocity-db-dev-01.ctexcplmewvh.us-east-1.rds.amazonaws.com',
  port     = 5432,
  user     = Sys.getenv("PAYLOCITY_DB_USERNAME"),
  password = Sys.getenv("PAYLOCITY_DB_PW"))

dbGetInfo(con)

dbListTables(con)

dbWriteTable(con, "mtcars", mtcars)

dbListTables(con)

dbListFields(con, "mtcars")

dbReadTable(con, "mtcars")

# You can fetch all results:
res <- dbSendQuery(con, "SELECT * FROM mtcars WHERE cyl = 4")

dbFetch(res)

dbClearResult(res)

# Or a chunk at a time
res <- dbSendQuery(con, "SELECT * FROM mtcars WHERE cyl = 4")

while (!dbHasCompleted(res)) {
  chunk <- dbFetch(res, n = 5)
  
  print(nrow(chunk))
}

# Clear the result
dbClearResult(res)

# Disconnect from the database
dbDisconnect(con)
