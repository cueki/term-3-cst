/*
Madison Lovett, A01292253
Feb 3rd, 2026
*/

package com.example.lib

class MissionManager {
    fun select(mission: Mission, listener: MissionListener) {
        mission.start(listener)
    }

    fun selectRepeatable(mission: Repeatable, times: Int, listener: MissionListener) {
        mission.repeat(times, listener)
    }
}
