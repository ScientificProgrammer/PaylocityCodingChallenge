library(tibble)
library(dplyr)
library(stringr)

# v1 <- Sys.getenv()
# v1_names <- attr(v1, "names", exact = TRUE)
# grep("rstudio", v1_names, ignore.case = TRUE, value = TRUE)

envvars <- tibble(
    envvar = attr(Sys.getenv(), "names", exact = TRUE),
    envval = as.character(Sys.getenv())
)

rstudioenvvals <- envvars %>%
    mutate(
        UPPERENVVAR = toupper(envvar),
        UPPERENVVAL = toupper(envval)
    ) %>%
    filter(
        stringr::str_detect(
            UPPERENVVAR, "RSTUDIO") | stringr::str_detect(UPPERENVVAL, "RSTUDIO"
        )
    ) %>% arrange(UPPERENVVAR, UPPERENVVAL, envvar, envval) %>%
    select(c(-UPPERENVVAR, -UPPERENVVAL))

rstudioenvvals
