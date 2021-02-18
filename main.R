library(rmarkdown)

render("index.Rmd")

library(dplyr)
library(flexdashboard)
library(igraph)
library(readxl)
library(sf)
library(sfnetworks)
library(tidygraph)
library(tidyverse)
library(tmap)
library(geosphere)

tmap_mode("view")

stations = st_read("data/tfl_stations_new.json") %>%
  rename("Number of Lines" = "Number.of.Lines", "Station ID" = "Station.ID", "Line(s)" = "Lines")
lines = st_read("data/tfl_lines_new.json")
zones = st_read("data/tfl_zones.json")

colors = c(
  "#B26300", # Bakerloo
  "#DC241F", # Central
  "#FFD329", # Circle
  "#9364CC", # Crossrail
  "#e1eb5b", # Crossrail 2
  "#007D32", # District
  "#00AFAD", # DLR
  "#E0A9BE", # Hammersmith & City
  "#A1A5A7", # Jubliee
  "#9B0058", # Metropolitan
  "#000000", # Northern
  "#EF7B10", # Overground
  "#0019A8", # Piccadilly
  "#0098D8", # Victoria
  "#93CEBA" # Waterloo & City
)

tm_shape(zones)+
  tm_polygons(col="name", alpha=.2, legend.show=FALSE)+
  tm_shape(lines) +
  tm_lines(col="Line", scale=3, palette = colors) +
  tm_shape(stations) +
  tm_dots() 


