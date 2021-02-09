# This code relies on the pacman, tidyverse and jsonlite packages
require(pacman)
p_load('tidyverse', 'jsonlite')

# We're going to assume that the data coming from
# the third-party tool has been loaded into R,
# for example from a CSV file.
#header_skip <- ifelse(skip_range[1] > 1, 0, skip_range[1])
header <- read_csv('tryingthis.csv', skip=2, n_max=1)

# Load the remainder of the file
data <- read_csv('tryingthis.csv', skip=3, col_names=colnames(header))
#data_raw <- read_csv('tryingthis.csv')

# Please also check that any extraneous data that
# an external tool might introduce are stripped
# before the following steps. For example, Qualtrics
# introduces two extra rows of metadata after the
# header. Un-commenting the following command removes
# this line and re-checks all column data types.
#data_raw <- data_raw[-c(1, 2),] %>% type_convert()

# One of the columns in this file contains the
# JSON-encoded data from lab.js
labjs_column <- 'labjsdata'

# Unpack the JSON data and discard the compressed version
data_raw %>%
  # Provide a fallback for missing data
  mutate(
    !!labjs_column := recode(.[[labjs_column]], .missing='[{}]')
  ) %>%
  # Expand JSON-encoded data per participant
  group_by_all() %>%
  do(
    fromJSON(.[[labjs_column]], flatten=T)
  ) %>%
  ungroup() %>%
  # Remove column containing raw JSON
  select(-matches(labjs_column)) -> data

# The resulting dataset, available via the 'data'
# variable, now contains both the experimental
# data collected by lab.js, as well as any other
# columns introduced by the software that collected
# the data. Values from the latter are repeated
# to fill added rows.

# As a final step, you might want to save the
# resulting long-form dataset
write_csv(data, 'labjs_data_output.csv')
