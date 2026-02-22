package com.bcit.lib

class ExcitedBehavior : Playable {
    override fun play() {
        println("Your pet is running around excitedly!")
    }
}

class LazyBehavior : Playable {
    override fun play() {
        println("Your pet doesn't want to play, they rather lay in the sun.")
    }
}
