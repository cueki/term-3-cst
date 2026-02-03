/*
Madison Lovett, A01292253
Feb 3rd, 2026
*/

package com.example.lib

interface MissionListener {
    fun missionStart(minion: Minion)
    fun missionProgress()
    fun missionComplete(minion: Minion, reward: String)
}
