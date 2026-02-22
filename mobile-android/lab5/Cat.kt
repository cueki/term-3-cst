package com.bcit.lib

class Cat(behavior: Playable) : Pet, Playable by behavior {

    override val name: String
        get() = "Whiskers"

    override val sound: String
        get() = "Meow"

    override fun interact() {
        println("$name is purring, $sound")
    }

    override fun feed() {
        println("$name ate some cat food")
    }
}
