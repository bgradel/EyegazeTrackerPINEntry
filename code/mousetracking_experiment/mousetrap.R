
library(tidyr)
library(mousetrap)
library(ggplot2)
library(grid)
library(png)
#remove all rows w/o mouse tracking data
#or else mousetrap will give errors
cleanstudy <- fullexperiment[-c(1,5,6,7,8),]  
mousedata <- mt_import_mousetrap(
  cleanstudy,
  xpos_label = "xpos",
  ypos_label = "ypos",
  timestamps_label = "timestamps",
  mt_id_label = NULL,
  split = ",",
  duplicates = "ignore",
  reset_timestamps = TRUE,
  verbose = FALSE
)


mt_plot(mousedata, use = "trajectories", x = "xpos", y="ypos", color = "mt_id") #plot of all screens
mt_heatmap(mousedata, use="trajectories",dimensions = c("xpos","ypos"),
           filename = NULL, plot_dims = FALSE, verbose = TRUE)
mt_plot_per_trajectory(mousedata, file = "trajectories.pdf", use = "trajectories",
                       x = "xpos",
                       y = "ypos",) #saves individual screens to a pdf file
mousevel <- mt_derivatives(mousedata,use = "trajectories",dimensions = c("xpos", "ypos"),
               timestamps = "timestamps",)


