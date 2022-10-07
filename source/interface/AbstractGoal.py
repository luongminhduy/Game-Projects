
from abc import abstractmethod


class AbstractGoal:

    @abstractmethod
    def update(self):
        pass