package com.bcit.lib

class Dog : Pet{

    override val name: String
        get() = "Rover"

    override val sound: String
        get() = "Woof woof"

    override fun play() {
        println("$name is fetching the ball, $sound")
    }

    override fun interact() {
        println("$name is wagging their tail, $sound")
    }

    override fun feed() {
        println("$name ate some dog treats")
    }
}