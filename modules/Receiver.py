from abc import ABC, abstractmethod
from typing import List


class Position(ABC):
    x: float = None
    y: float = None
    z: float = None

    def __init__(self, x, y, z):
        self.set_position(x, y, z)

    def get_position(self):
        return Position(self.x, self.y, self.z)

    def set_position(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class VisionReceiver(ABC):
    ball_position = None
    robots_yellow: List[Position] = []
    robots_blue: List[Position] = []
    # field_size : List[Size] = None

    @abstractmethod
    def set_yellow_robots(self):
        pass

    @abstractmethod
    def set_blue_robots(self):
        pass

    @abstractmethod
    def set_ball_positions(self):
        pass