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

Stations2 <- st_read("data/tfl_stations_new2.json")
st_geometry(Stations2) <- NULL
Lines2 <- st_read("data/tfl_lines_new2.json")

Lines2 <- mutate(Lines2, Length = st_length(Lines2)) %>%
  inner_join(Stations2, c("start_sid" = "Station.ID")) %>%
  inner_join(Stations2, c("end_sid" = "Station.ID"))
view(Lines2)
st_geometry(Lines2) <- NULL
Lines2 <- Lines2 %>%
  group_by(start_sid, end_sid, Line) %>%
  summarise(Length = sum(Length))

view(Lines2)

  group_by(Lines2, Line) %>%
  summarise("Total length" = sum(Length), "Average length" = mean(Length), stations=n()) %>%
  view()
view(Lines2)



