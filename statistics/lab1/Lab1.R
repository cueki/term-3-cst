# Madison Lovett, A01292253
# Lab 1, MATH 3042 set V
# Jan 14th, 2026

library(dplyr)
library(stringi)

# 1.
fastrunners = filter(TenMileRace, time < 4000)

# 2a)
femalerunners = filter(TenMileRace, sex == "F")

# 2b)
foreignrunners = filter(TenMileRace, stri_length(state) > 2)

# 3.
count(TenMileRace, state)

# 4.
fastest_female = min(femalerunners$time)
fastermales = filter(TenMileRace, sex == "M" & time < fastest_female)

# 5.
sortedtimes = arrange(TenMileRace, time)
five_percent = nrow(sortedtimes) * 0.05
averagerunners = filter(sortedtimes, row_number() > five_percent &
  (row_number() < (nrow(sortedtimes) - five_percent)))
hist(averagerunners$time)
