# Madison Lovett, A01292253
# Lab 2, MATH 3042 set V
# Jan 16th, 2026

library(dplyr)
library(MASS)
library(aplpack)
library(lattice)

# 1.
homeType = c("on campus", "with parents", "alone", "with roommates", "with spouse")
percents = c(10, 30, 5, 35, 20)
pie(percents, labels = homeType, col = c("red", "blue", "cyan", "green", "yellow"))

# 2.
hands = survey$W.Hnd
tab = table(hands)
labels = paste(rownames(tab), sep = "\n", tab)
pie(tab, labels, col = c("pink", "turquoise"), main = ("Writing hands of 237 students"))

# 3.
hands = survey$W.Hnd
tab = table(hands)
barplot(tab, horiz = TRUE, main = ("Writing hands of 237 students"))

# 4.
stem(survey$Height, scale = 2)

# 5.
Women = filter(survey, Sex == "Female")
WomensHeights = Women$Height
Men = filter(survey, Sex == "Male")
MensHeights = Men$Height
stem.leaf.backback(MensHeights, WomensHeights, m = 2, depths = FALSE)

# 6.
# The data seems to suggest that in general, women's heights are lower
# than men's heights by approximately 5-10 cm.

# 7.
WomensAges = filter(survey, Sex == "Female")$Age
MensAges = filter(survey, Sex == "Male")$Age
realAges = filter(survey, Age > 0)
rangeAges = range(realAges$Age)

# Shows from 16.8 to 77, so I will go from 10 to 80 in steps of 10 to encapsulate everyone:
breaks = seq(10, 80, by = 10)

# For women:
numWomensAges.cut = cut(WomensAges, breaks, right = FALSE)
numWomensAges.freq = table(numWomensAges.cut)
cbind(numWomensAges.freq)

# For men:
numMensAges.cut = cut(MensAges, breaks, right = FALSE)
numMensAges.freq = table(numMensAges.cut)
cbind(numMensAges.freq)

# From these two frequency tables it seems that there is not any
# significant difference between genders in this survey data, which makes
# sense if this survey is a random sampling from the general population.

# 8.
numHeights = survey$Height
hist(numHeights, breaks = seq(150, 200, by = 2.5), main = ("Heights of 237 students"), xlab = ("Heights (cm)"))

# 9.
breaks_ogive = seq(150, 200, by = 5)
numHeights.cut_ogive = cut(numHeights, breaks_ogive, right = FALSE)
numHeights.freq_ogive = table(numHeights.cut_ogive)
numHeights.cumfreq_ogive = cumsum(numHeights.freq_ogive)
freqs = c(0, numHeights.cumfreq_ogive)
plot(breaks_ogive, freqs, type = "b", main = "Ogive of 209 student heights", xlab = "student heights in cm", ylab = "number of students")

# 10.
xyplot(survey$Wr.Hnd ~ survey$Height, main = "Writing Hand Span vs Height", xlab = "Height (cm)", ylab = "Writing Hand Span (cm)")

# 11.
xyplot(survey$Wr.Hnd ~ survey$NW.Hnd, main = "Writing Hand Span vs Non-Writing Hand Span", xlab = "Non-Writing Hand Span (cm)", ylab = "Writing Hand Span (cm)")
xyplot(survey$Height ~ survey$Pulse, main = "Student Height vs Pulse Rate", xlab = "Pulse Rate (beats per minute)", ylab = "Height (cm)")
