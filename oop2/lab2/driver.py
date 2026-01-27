from datetime import datetime as dt, timedelta as td
import math
import random
import time

from asteroid import Asteroid, Vector

# Name: Madison Lovett
# Student number: A01292253

MICROSECONDS_IN_SECOND = 1_000_000

class Controller:
    NUM_ASTEROIDS = 100
    MIN_RADIUS = 1
    MAX_RADIUS = 4
    CUBE_SIZE = 100
    MAX_VELOCITY = 5

    def __init__(self):
        """Initialize the controller with a list of randomly generated asteroids."""
        self.asteroids = []
        for _ in range(self.NUM_ASTEROIDS):
            radius = self._generate_random_radius()
            circumference = self._calculate_circumference(radius)
            position = Vector.create_random(0, self.CUBE_SIZE)
            velocity = Vector.create_random(-self.MAX_VELOCITY, self.MAX_VELOCITY)
            self.asteroids.append(Asteroid(circumference, position, velocity))

    @staticmethod
    def _generate_random_radius() -> float:
        """Generate a random radius within the configured range."""
        return random.uniform(Controller.MIN_RADIUS, Controller.MAX_RADIUS)

    @staticmethod
    def _calculate_circumference(radius: float) -> float:
        """Calculate circumference from radius."""
        return 2 * math.pi * radius

    def simulate(self, seconds: int) -> None:
        """
        Simulate asteroid movement for the specified number of seconds.

        Waits until second rolls over before starting, then moves
        all asteroids once per second.

        :param seconds: number of seconds to simulate
        """

        now = dt.now()
        microseconds_to_wait = MICROSECONDS_IN_SECOND - now.microsecond
        time.sleep(microseconds_to_wait / MICROSECONDS_IN_SECOND)

        start_time = dt.now()
        print("Moving Asteroids!")
        print("-" * 17)
        print(f"Simulation Start Time: {start_time}")

        for i in range(seconds):
            for asteroid in self.asteroids:
                asteroid.move(dt=1)

            if i < seconds - 1:
                next_tick = start_time + td(seconds=i + 1)
                sleep_duration = (next_tick - dt.now()).total_seconds()
                if sleep_duration > 0:
                    time.sleep(sleep_duration)


def main():
    controller = Controller()
    controller.simulate(1)


if __name__ == '__main__':
    main()