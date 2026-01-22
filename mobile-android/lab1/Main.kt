/*
Madison Lovett, A01292253
Jan 14th, 2026
*/

const val VERSION_NUM = 1.0
const val SLOGAN = "deliver with a smile"

fun main() {
    val streetNum = 123
    val streetName = "loch ness road"
    var fullAddress: String? = if (VERSION_NUM >= 1) {
        "$streetNum $streetName, Glasgow, Scotland"
    } else {
        println("Starting beta version...\n...\n...\n...")
        null
    }
    var message: String = String.format("""
	Food Delivery Service v%s

Welcome to Glasgow's finest food delivery service, where we provide
you with swift instructions on where to deliver your food.

	Please deliver the food to:

	%s

Your hard work and commitment to delivering food are
always appreciated, and never forget...%s.

...Thank you.""", VERSION_NUM, fullAddress?.uppercase(), SLOGAN.uppercase())

    println(message)
}
