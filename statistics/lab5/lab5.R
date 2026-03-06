# Madison Lovett, A01292253
# Lab 5, MATH 3042 set V
# Feb 6th, 2026

# 1.
# Number of people with antibodies out of 100000: 5117
hasAntibodies = function(n) {
  sum(sample(c(0, 1), size = n, replace = TRUE, prob = c(0.95, 0.05)))
}

# 2.
# Number of true positives out of 100000: 89949
truePositives = function(n) {
  sum(sample(c(0, 1), size = n, replace = TRUE, prob = c(0.10, 0.90)))
}

# 3.
# The rate of false positives is P(Test Positive | No Antibodies) = 1 - 0.92 = 0.08,
# meaning 8% of people without COVID-19 antibodies will incorrectly test positive.

# 4.
# Number of false positives out of 100000: 8064
falsePositives = function(n) {
  sum(sample(c(0, 1), size = n, replace = TRUE, prob = c(0.92, 0.08)))
}

# 5.
# If the test says a person does not have antibodies, I would estimate the probability
# that they truly don't have antibodies is around 98%. Since only 5% of the population
# has antibodies and the test has 90% sensitivity, very few people who actually have
# antibodies would be missed, so a negative result is likely correct.

# 6.
# If the test says a person has antibodies, I would estimate the probability that the
# test is correct is around 37%. This might seem low, but because only 5% of the
# population actually has antibodies while 8% of the large non-antibody population
# will falsely test positive, many of the positive results are actually false positives.

# 7.
# P(No Antibodies | Tests Negative): 0.9943334
probNegativeGivenTestsNegative = function(n) {
  withAntibodies = hasAntibodies(n)
  withoutAntibodies = n - withAntibodies
  falseNegatives = withAntibodies - truePositives(withAntibodies)
  trueNegatives = withoutAntibodies - falsePositives(withoutAntibodies)
  trueNegatives / (trueNegatives + falseNegatives)
}

# 8.
# P(Has Antibodies | Tests Positive): 0.3631381
probPositiveGivenTestsPositive = function(n) {
  withAntibodies = hasAntibodies(n)
  withoutAntibodies = n - withAntibodies
  tp = truePositives(withAntibodies)
  fp = falsePositives(withoutAntibodies)
  tp / (tp + fp)
}

# 9.
# I would say these results match my previous predictions :). Yes, a negative result
# is very confident, but a positive result has lots of room for error.

# 10.
# 10%
# P(No Antibodies | Tests Negative): 0.9885521
# P(Has Antibodies | Tests Positive): 0.5465782
#
# 50%
# P(No Antibodies | Tests Negative): 0.9018722
# P(Has Antibodies | Tests Positive): 0.9192495
#
# The results are heavily influenced by the random probability of the population itself,
# less so of the accuracy of the test (because the test is pretty accurate).
#
# But this begs the question... how did they figure out the percentage of the population
# has these antibodies? How accurate is that test?
