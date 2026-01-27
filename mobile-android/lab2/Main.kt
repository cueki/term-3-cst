/*
Madison Lovett, A01292253
Jan 20th, 2026
 */

fun main() {
    // array
    val w = arrayOf("kotlin", "java", "swift", "go", "rust", "C", "python")
    // mutable list
    val l = mutableListOf<Int>()
    // for loop
    for (vv in w) l.add(vv.length)
    // break + while
    var i = 0
    var (max, min) = 0 to Int.MAX_VALUE
    while (true) { if (i >= l.size) break else max = maxOf(max, l[i])
        min = minOf(min, l[i++])
    }
    // forEach
    val (b, s) = mutableListOf<String>() to mutableListOf<String>()
    w.forEach {
        if (it.length == max) b.add(it) else if (it.length == min) s.add(it)
    }
    println("Words: ${w.joinToString()}\nLengths: $l\nLongest: $b\nShortest: $s")
}
