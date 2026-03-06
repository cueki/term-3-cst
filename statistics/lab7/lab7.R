# Madison Lovett, A01292253
# Lab 7, MATH 3042 set V
# March 6th, 2026

# 1.
DiceMeans = function(n, m) {
  sample_means = replicate(n, mean(sample(1:6, m, replace = TRUE)))

  mean_of_means = mean(sample_means)
  sd_of_means = sd(sample_means)

  barplot(table(round(sample_means, 2)),
          main = paste("Means for rolling", m, "dice", n, "times"),
          xlab = "Sample Mean",
          ylab = "Frequency")

  return(c(Mean = mean_of_means, SD = sd_of_means))
}

# Mean: 3.498800 SD: 1.703552
# Mean: 3.482250 SD: 1.202645
# Mean: 3.5079800 SD: 0.5406714
# Mean: 3.5006500 SD: 0.2419402
# Mean: 3.4993460 SD: 0.1693059

# 2.
BusWaitTimes = function(n) {
  wait_times = runif(n, min = 0, max = 20)
  hist(wait_times,
       main = paste("Waiting times for", n, "people (bus every 20 min)"),
       xlab = "Waiting Time (minutes)",
       ylab = "Frequency")
}
# From these graphs, I would say that they are mostly uniform, however, due to the
# randomness, the smaller sample results in data that is slightly skewed with a longer
# wait time. This is to be expected, as with 100 people and 20 minutes, each 2 min
# bucket should contain between 5 and 15 people.

# 3.
# Roughly half of the sample waits less than minutes, this is to be expected as it is
# uniform, therefore the average wait time is in the middle, ie, 10 minutes. Any other
# answer would be non uniform...
