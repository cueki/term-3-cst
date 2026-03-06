# Madison Lovett, A01292253
# Lab 6, MATH 3042 set V
# March 5th, 2026

# 1.
# a)
m = 10
n = 10000
freq = table(replicate(n, sum(sample(1:6, m, replace=TRUE) == 3))) / n
barplot(freq, xlab="Number of 3s", ylab="Relative Frequency", main="Relative Frequencies of 3s")

# b)
freq = table(rbinom(n, m, 1/6)) / n
barplot(freq, xlab="Number of 3s", ylab="Relative Frequency", main="Relative Frequencies of 3s")

# 2.
# Rolling a die and checking if it's a 3 is a Bernoulli trial with p = 1/6, and counting
# successes across m independent trials is exactly what the binomial distribution models.
# So rbinom() is just a more efficient shortcut for the same experiment.

# 3.
# a)
dbinom(100, 300, 1/3)
# [1] 0.04881277

# b)
pbinom(100, 300, 1/3)
# [1] 0.5271102

# c)
pbinom(99, 300, 1/3)
# [1] 0.4782974

# d)
1 - pbinom(109, 300, 1/3)
# [1] 0.1227525

# 4.
x = 0:4
probs = dhyper(x, m = 4, n = 48, k = 8)
jack_table = data.frame(Jacks = x, Probability = round(probs, 6))
barplot(probs, names.arg = x, main = "Probability of Jacks Drawn (from 8 Cards)",
        xlab = "Number of Jacks", ylab = "Probability")

# 5.
sim_cards_sample = function(m, n) {
  deck = c(rep(1, 4), rep(0, 48))

  jack_counts = replicate(n, {
    hand = sample(deck, m, replace = FALSE)
    sum(hand)
  })

  freq = table(factor(jack_counts, levels = 0:4))
  rel_freq = freq / n
  result = data.frame(Jacks = 0:4,  RelativeFrequency = as.numeric(rel_freq))
  print(result)
  barplot(as.numeric(rel_freq),
          names.arg = 0:4,
          main = "Simulated Distribution of Jacks (10000 Simulations)",
          xlab = "Number of Jacks",
          ylab = "Relative Frequency")
}

sim_cards_hyper = function(m, n) {
  jack_counts = rhyper(nn = n, m = 4, n = 48, k = m)

  freq = table(factor(jack_counts, levels = 0:4))
  rel_freq = freq / n

  result = data.frame(Jacks = 0:4, RelativeFrequency = as.numeric(rel_freq))
  print(result)

  barplot(as.numeric(rel_freq),
          names.arg = 0:4,
          main = "Simulated Distribution of Jacks (10000 Simulations)",
          xlab = "Number of Jacks",
          ylab = "Relative Frequency",)
}

# a)
sim_cards_sample(m = 8, n = 10000)

# b)
sim_cards_hyper(m = 8, n = 10000)

# 6.
# Both simulations produce relative frequencies that closely approximate the probabilities
# from dhyper(), but they are not identical because the simulations involve "randomness".

# 7.
# a)
dhyper(100, 333, 666, 300)
# [1] 0.05834763

# b)
phyper(100, 333, 666, 300)
# [1] 0.5304624

# c)
phyper(99, 333, 666, 300)
# [1] 0.4721148

# d)
1 - phyper(109, 333, 666, 300)
# [1] 0.08253631

# e)
phyper(110, 333, 666, 300) - phyper(89, 333, 666, 300)
# [1] 0.8759101

# 8.
x = 0:34
probs = dgeom(x, prob = 1/5)
ticket_table = data.frame(FailuresBeforeWin = x, TotalTickets = x + 1,
    Probability = round(probs, 6))
barplot(probs, names.arg = x + 1,
        main = "Tickets Purchased Before Winning (p = 1/5)",
        xlab = "Total Tickets Purchased", ylab = "Probability", las = 2, cex.names = 0.7)

# 9.
sim_lottery_sample = function(n) {
  tickets_bought = replicate(n, {
    count = 0
    repeat {
      ticket = sample(c("win", "lose"), 1, prob = c(1/5, 4/5))
      count = count + 1
      if (ticket == "win") break
    }
    count
  })

  max_val = max(tickets_bought)
  freq = table(factor(tickets_bought, levels = 1:max_val))
  rel_freq = freq / n

  result = data.frame(TotalTickets = 1:max_val,
                      RelativeFrequency = as.numeric(rel_freq))
  result = result[result$RelativeFrequency >= 0.0001, ]

  barplot(result$RelativeFrequency,
          names.arg = result$TotalTickets,
          main = "Tickets Before Winning (p = 1/5, n = 10000 simulations)",
          xlab = "Total Tickets Purchased",
          ylab = "Relative Frequency",
          las = 2,
          cex.names = 0.7)
}

sim_lottery_hyper = function(n) {
  tickets_bought = rgeom(n, prob = 1/5) + 1

  max_val = max(tickets_bought)
  freq = table(factor(tickets_bought, levels = 1:max_val))
  rel_freq = freq / n

  result = data.frame(TotalTickets = 1:max_val,
                      RelativeFrequency = as.numeric(rel_freq))
  result = result[result$RelativeFrequency >= 0.0001, ]

  barplot(result$RelativeFrequency,
          names.arg = result$TotalTickets,
          main = "Simulated Distribution: Tickets Before Winning (p = 1/5, n = 10000 simulations)",
          xlab = "Total Tickets Purchased",
          ylab = "Relative Frequency",
          las = 2,
          cex.names = 0.7)
}

# a)
sim_lottery_sample(n = 10000)

# b)
sim_lottery_hyper(n = 10000)

# 10.
# Both simulations produce relative frequencies that approximate the exact probabilities
# from dgeom(), but are not identical due to randomness. Both bar plots show the same
# right-skewed, decreasing pattern as the exact distribution. With n = 10,000 simulations,
# relative frequencies are typically within a few hundredths of the exact values. Increasing
# n would bring them even closer, (Law of Large Numbers).

# 11.
# a)
pgeom(499, prob = 0.001)
# [1] 0.3936211

# b)
1 - pgeom(1199, prob = 0.001)
# [1] 0.3010134

# c)
pgeom(2000, prob = 0.001) - pgeom(999, prob = 0.001)
# [1] 0.2326307

# 12.
x = 0:6
probs = dpois(x, lambda = 0.75)
flaw_table = data.frame(Flaws = x, Probability = round(probs, 6))
barplot(probs, names.arg = x, main = "Flaws per Metre of Fibre Optic Cable",
        xlab = "Number of Flaws", ylab = "Probability")

# 13.
sim_flaws = function(n) {
  flaw_counts = rpois(n, lambda = 0.75)

  max_val = max(flaw_counts)
  freq = table(factor(flaw_counts, levels = 0:max_val))
  rel_freq = freq / n

  result = data.frame(Flaws = 0:max_val,
                      RelativeFrequency = as.numeric(rel_freq))
  result = result[result$RelativeFrequency >= 0.0001, ]

  barplot(result$RelativeFrequency,
          names.arg = result$Flaws,
          main = "Flaws per Metre of Cable",
          xlab = "Number of Flaws",
          ylab = "Relative Frequency")
}

sim_flaws(n = 10000)

# 14.
# Both distributions show the same shape, highest probability at 0 flaws, decreasing as
# the number of flaws increases. With n = 10,000 simulations, the relative frequencies are
# typically within a few hundredths of the exact dpois() values. As with the previous
# simulations, increasing n would bring the relative frequencies even closer to the exact
# probabilities, as expected.

# 15.
# a)
dpois(34, lambda = 34)
# [1] 0.06825056

# b)
ppois(30, lambda = 34)
# [1] 0.2803502

# c)
1 - ppois(38, lambda = 34)
# [1] 0.2166179

# d)
1 - ppois(37, lambda = 34)
# [1] 0.2681011

# e)
ppois(40, lambda = 34) - ppois(29, lambda = 34)
# [1] 0.6429105

# f)
ppois(34, lambda = 34)^2
# [1] 0.297506

# g)
ppois(68, lambda = 68)
# [1] 0.532192
