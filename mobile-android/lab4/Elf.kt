/*
Madison Lovett, A01292253
Feb 3rd, 2026
*/

package com.example.lib

class Elf : Minion() {
    override val race: String = "Elf"
    override val baseHealth: Int = 2
    override val baseSpeed: Int = 8
    override val backpackSize: Int = 3
    override val catchphrase: String = "My arrows never miss!"
}
