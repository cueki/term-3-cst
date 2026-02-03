/*
Madison Lovett, A01292253
Feb 3rd, 2026
*/

package com.example.lib

abstract class Mission(protected val minion: Minion) {
    init {
        println(minion.catchphrase)
    }

    fun start(listener: MissionListener) {
        listener.missionStart(minion)
        listener.missionProgress()
        listener.missionProgress()
        val time = determineMissionTime()
        val rewardResult = reward(time)
        listener.missionComplete(minion, rewardResult)
    }

    protected abstract fun determineMissionTime(): Int
    protected abstract fun reward(time: Int): String
}
