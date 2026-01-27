# Name: Madison Lovett
# Student number: A01292253

from dataclasses import dataclass
import random


@dataclass
class Vector:
    """Represents a vector in 3D space with x, y, and z coordinates."""
    x: float
    y: float
    z: float

    def __str__(self) -> str:
        return f"{self.x}, {self.y}, {self.z}"

    def add(self, vector: "Vector") -> "Vector":
        """Adds another vector to this one and returns a new Vector."""
        return Vector(self.x + vector.x, self.y + vector.y, self.z + vector.z)

    def to_tuple(self) -> tuple:
        """Returns the vector as a tuple (x, y, z)."""
        return self.x, self.y, self.z

    @staticmethod
    def create_random(min_val: float, max_val: float) -> "Vector":
        """Creates a Vector with random x, y, z values within the specified range."""
        return Vector(
            random.uniform(min_val, max_val),
            random.uniform(min_val, max_val),
            random.uniform(min_val, max_val)
        )


class Asteroid:
    """Represents an asteroid with circumference, position, and velocity."""

    _next_id = 1

    def __init__(self, circumference: float, position: Vector, velocity: Vector):
        """
        Initialize an Asteroid.

        :param circumference: circumference in metres
        :param position: position vector (x, y, z) in metres
        :param velocity: velocity vector (x, y, z) in metres per second
        """
        self.id = Asteroid._get_next_id()
        self._circumference = circumference
        self.position = position
        self.velocity = velocity

    def __str__(self) -> str:
        return (f"Asteroid {self.id} is currently at {self.position} and moving at "
                f"{self.velocity} meters per second. It has a circumference of {self._circumference}.")

    @classmethod
    def _get_next_id(cls) -> int:
        """Return the next unique ID and increment the counter."""
        current_id = cls._next_id
        cls._next_id += 1
        return current_id

    def move(self, dt: float) -> None:
        """
        Update the asteroid's position based on its velocity.

        :param dt: time delta in seconds
        """
        old_position = self.position
        self.position = self.position.add(Vector(dt * self.velocity.x, dt * self.velocity.y, dt * self.velocity.z))
        print(f"Asteroid {self.id} moved! Old Pos: {int(old_position.x)}, {int(old_position.y)}, {int(old_position.z)} "
              f"-> New Pos: {int(self.position.x)}, {int(self.position.y)}, {int(self.position.z)} "
              f"It has a circumference of {self._circumference}.")
        print(f"Current position: {int(self.position.x)}, {int(self.position.y)}, {int(self.position.z)}")
