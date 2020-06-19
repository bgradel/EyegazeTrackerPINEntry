study <- study..2020.06.18..19_54_58
library(tidyr)
library(mousetrap)
mousedf <- data.frame(study$timestamps, study$xpos, study$ypos)
mousedf = separate_rows(mousedf,study.timestamps,study.xpos, study.ypos,sep=",")
mousedf
mousedata <- mt_import_mousetrap(
  study,
  xpos_label = "xpos",
  ypos_label = "ypos",
  timestamps_label = "timestamps",
  mt_id_label = NULL,
  split = ",",
  duplicates = "ignore",
  reset_timestamps = TRUE,
  verbose = FALSE
)
mousedata

