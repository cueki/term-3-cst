# 1
FlipOnce = function()
{  
  HeadOrTail<- sample(c("Heads", "Tails"), 1)
  return(HeadOrTail)
}

# 2
CoinResults=function(n)
{
  coinList = sample(c("Heads", "Tails"), n, repl=TRUE)
  return(coinList)
}

# 3
ProbHeads=function(n)
{
  coinList<-CoinResults(n)
  numHeads<-sum(coinList=="Heads")
  return(numHeads/n)
}

MaxAndMinHeads = function(m, n)
{
  result = replicate(n, ProbHeads(m))
  return(c(max(result), min(result)))
}

# 4
RollDie = function(n) {
  rolls = sample(1:6, n, replace = TRUE)                                                                                                                                                                       
  barplot(table(rolls),
          main = paste("Distribution of outcomes of", n, "die rolls"),                                                                                                                                          
          xlab = "Outcome",
          ylab = "Frequency")
}

# 5
RollSomeDice = function(n, m) {
  for (i in 1:n) {
    count_threes = replicate(n, sum(sample(1:6, m, replace = TRUE) == 3))
  }
  
  dist = table(count_threes)
  print(dist)
  
  barplot(dist,
          main = paste("Number of 3's obtained in rolling", m, "dice"),
          xlab = "Number of 3's",
          ylab = "Frequency")
}
# 6
DrawCardsWithReplacement = function(n, m) {
  deck = c(rep(1, 26), rep(0, 26))
  red_counts = replicate(n, sum(sample(deck, m, replace = TRUE)))
  barplot(table(factor(red_counts, levels = 0:m)),
          main = paste("Red cards drawn WITH replacement (m =", m, ")"),
          xlab = "Number of red cards",
          ylab = "Frequency")
}

# 7
DrawCardsWithoutReplacement = function(n, m) {
  deck = c(rep(1, 26), rep(0, 26))
  red_counts = replicate(n, sum(sample(deck, m, replace = FALSE)))
  barplot(table(factor(red_counts, levels = 0:m)),
          main = paste("Red cards drawn WITHOUT replacement (m =", m, ")"),
          xlab = "Number of red cards",
          ylab = "Frequency")
}

