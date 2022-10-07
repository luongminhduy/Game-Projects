
from abc import abstractmethod
from AbstractBall import AbstractBall
from AbstractPlayer import AbstractPlayer
from AbstractGoal import AbstractGoal
from AbstractPitch import AbstractPitch


class AbstractFactory:

    @abstractmethod
    def createBall(self) -> AbstractBall:
        pass

    @abstractmethod
    def createPlayer(self) -> AbstractPlayer:
        pass

    @abstractmethod
    def createGoal(self) -> AbstractGoal:
        pass

    @abstractmethod
    def createPitch(self) -> AbstractPitch:
        pass