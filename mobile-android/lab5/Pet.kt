package com.bcit.lib

interface Playable{
    fun play()
}

interface Interactable{
    val sound:String
    fun interact()
}

interface Feedable{
    fun feed()
}

interface Pet : Playable, Interactable, Feedable{
    val name:String
}

