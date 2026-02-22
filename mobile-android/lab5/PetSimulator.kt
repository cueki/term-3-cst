package com.bcit.lib

import kotlin.properties.Delegates
import kotlin.system.exitProcess

fun Pet.customAction(action: Pet.() -> Unit) {
    this.action()
}

class PetSimulator {

    private var invalidChoiceCount: Int by Delegates.observable(0) { _, _, newValue ->
        when (newValue) {
            1 -> println("Oops, That's not a valid option. Please try again.")
            2 -> println("Oops, That's not a valid option. Please, this time enter one of the choices provided.")
            3 -> {
                println("Too many invalid choices. Exiting the program.")
                exitProcess(0)
            }
        }
    }

    fun start() {
        while (true) {
            println()
            println("Choose pet:")
            println("1. Dog\n2. Cat\n3. Exit")
            when (readln().toIntOrNull()) {
                1 -> {
                    val pet = Dog()
                    adopt(pet)
                }
                2 -> {
                    val behavior = chooseBehaviour() ?: continue
                    val pet = Cat(behavior)
                    adopt(pet)
                }
                3 -> return
                else -> {
                    invalidChoiceCount++
                }
            }
        }
    }

    private fun chooseBehaviour(): Playable? {
        while (true) {
            println()
            println("Choose a behaviour:")
            println("1. Excited\n2. Lazy\n3. Go back")
            when (readln().toIntOrNull()) {
                1 -> return ExcitedBehavior()
                2 -> return LazyBehavior()
                3 -> return null
                else -> invalidChoiceCount++
            }
        }
    }

    private fun adopt(pet: Pet) {
        pet.customAction {
            println("$name is so happy to have a new home!")
        }

        while (true) {
            println()
            println("What would you like to do with ${pet.name}?")
            println("1. Play\n2. Feed\n3. Interact\n4. Back")
            when (readln().toIntOrNull()) {
                1 -> pet.play()
                2 -> pet.feed()
                3 -> pet.interact()
                4 -> return
                else -> {
                    invalidChoiceCount++
                }
            }
        }
    }

}
