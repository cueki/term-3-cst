/*
Madison Lovett, A01292253
Feb 3rd, 2026
*/

package com.example.lib

fun main() {
    val manager = MissionManager()

    val dwarf = Dwarf()
    val gather = Gather(dwarf)

    manager.select(gather, object : MissionListener {
        override fun missionStart(minion: Minion) {
            println("A ${minion.race} was sent off to gather some resources")
        }

        override fun missionProgress() {
            println("...")
        }

        override fun missionComplete(minion: Minion, reward: String) {
            println("A ${minion.race} has returned from a gather and found $reward!")
        }
    })

    println()

    val elf = Elf()
    val hunt = Hunt(elf)

    manager.select(hunt, object : MissionListener {
        override fun missionStart(minion: Minion) {
            println("An ${minion.race} started a hunt!")
        }

        override fun missionProgress() {
            println("...")
        }

        override fun missionComplete(minion: Minion, reward: String) {
            println("An ${minion.race} has returned from a hunt, and found $reward!")
        }
    })

    println()

    val dwarf2 = Dwarf()
    val gather2 = Gather(dwarf2)

    manager.selectRepeatable(gather2, 3, object : MissionListener {
        override fun missionStart(minion: Minion) {
            println("A ${minion.race} was sent off to gather some resources")
        }

        override fun missionProgress() {
            println("...")
        }

        override fun missionComplete(minion: Minion, reward: String) {
            println("A ${minion.race} has returned from a gather and found $reward!")
        }
    })
}
