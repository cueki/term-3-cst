/*
Madison Lovett, A01292253
Jan 27th, 2026
*/

package com.example.lib

fun main() {
    val historyFacts = mapOf(
        1492 to "Christopher Columbus discovers America",
        1601 to "William Shakespear writes Hamlet",
        1632 to "Galileo discovered the acceleration of gravity on Earth to be 9.8m/s",
        1838 to "Roughly 9.46 trillion km, the light-year is the first used as a measurement in astronomy",
        2020 to "Covid 19 Pandemic",
    )
    for(fact in historyFacts) { println(fact) }
    println()

    // anon
    val getByKey = fun(key: Int): String? { return historyFacts[key] }
    println(getByKey(1492))

    // yambda
    val printFact: (String) -> Unit = { println(it) }
    printFact(historyFacts.getValue(1601))

    // god awful nightmare
    fun displayUsing(map: Map<Int, String>, selector: (Map<Int, String>) -> String) {
        println(selector(map))
    }
    displayUsing(historyFacts) { it.getValue(1632) }

    // java
    fun showEntry(entry: Pair<Int, String>) { println(entry.second) }
    historyFacts.entries.elementAt(3).toPair().let(::showEntry)

    // programming paradigms
    fun findFact(values: List<String>, n: Int): String {
        return if (n == 0) values.first() else findFact(values.drop(1), n - 1)
    }
    println(findFact(historyFacts.values.toList(), 4))
}