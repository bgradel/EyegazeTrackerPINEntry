study <- test2

study
library(tidyr)
library(mousetrap)
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

mousedata$trajectories
mt_time_normalize(
  mousedata,
  use = "trajectories",
  save_as = "tn_trajectories",
  dimensions = c("xpos", "ypos"),
  timestamps = "timestamps",
  nsteps = 200,
  verbose = FALSE
)
mt_plot(mousedata, use = "trajectories", x = "xpos", y="ypos", color = "mt_id")
mt_heatmap(mousedata, use="trajectories",dimensions = c("xpos","ypos"),
           filename = NULL, plot_dims = FALSE, verbose = TRUE)
