from enum import Enum

class Speed(Enum):

    def __str__(self):
        return str(self.value)

    SLOW = 0.5
    NORMAL = 0.1
    FAST = 0.05
