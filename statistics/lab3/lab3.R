# Madison Lovett, A01292253
# Lab 1, MATH 3042 set V
# Jan 30th, 2026

library(mosaic)
library(MASS)

# 1.
absMean = mean(~Days, data = quine)
absMedian = median(~Days, data = quine)
absSD = sd(~Days, data = quine)
pearsonian = 3 * (absMean - absMedian) / absSD
pearsonian
# Result: 1.007598
# This value is >1 which indicates a right skew.

# 2.
hist(quine$Days)
# The tail is pulling to the right, that one student with 81 absences is
# pulling a lot of weight. In other words, it is consistent with Q1.

# 3.
boxplot(quine$Days, 
        main = "Distribution of Student Absences",
        ylab = "Number of Days Absent")
# The boxplot suggests that there are 7 outliers, and that a typical
# student was absent between 5 and 22 days.

# 4.
favstats(~Days, data = quine)
# min  Q1  median  Q3   max   mean      sd    n  missing
#   0   5    11   22.75  81  16.4589  16.25322  146    0

# 5.
boxplot(Days ~ Age, data = quine)
# Approximately 50% of F2 students were absent between about 5 and 32 days,
# whereas 50% of F1 students were absent between only about 5 and 15 days.
# This suggests F2 students have the most variability in absences.
#
# 50% of F3 students were absent for more than approximately 18-20 days,
# compared to F0 and F1 where 50% of students were absent more than only
# about 10 days. Older students (F3) tend to miss more school.
#
# All four age groups have outliers (students with unusually high absences).
# However, the F2 group has the most extreme outlier at approximately 80 days.

# 6.
sd(Days ~ Age + Sex, data = quine)
# F1.M are the most consistent with a standard deviation of only 5.3,
# while F2.F are the least consistent with the highest standard deviation of 23.1.

# 7.
quantile(Days ~ Lrn, data = quine, probs = c(0.2, 0.4, 0.6, 0.8))
quantile(Days ~ Sex, data = quine, probs = c(0.2, 0.4, 0.6, 0.8))
quantile(Days ~ Eth, data = quine, probs = c(0.2, 0.4, 0.6, 0.8))
# Ethnicity would allow the most accurate prediction because the two
# ethnicity groups (A and N) show the largest differences at every percentile.

# 8.
maleF0 = subset(quine, Sex == "M" & Age == "F0")
options(digits = 2)
data.frame(PercentileRank = percent_rank(maleF0$Days))

# 9.
zscores = scale(quine$Days)

# Count observations at different z-score thresholds
sum(abs(zscores) >= 1)  # Result: 32
sum(abs(zscores) >= 2)  # Result: 8
sum(abs(zscores) >= 3)  # Result: 3
