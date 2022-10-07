from interface.AbstractFactory import AbstractFactory
from interface.AbstractBall import AbstractBall
from interface.AbstractGoal import AbstractGoal
from interface.AbstractPitch import AbstractPitch
from interface.AbstractPlayer import AbstractPlayer
from objects.Ball import Ball
from objects.Goal import Goal
from objects.Pitch import Pitch
from objects.Player import Player

class Factory(AbstractFactory):

    def createBall(self) -> AbstractBall:
        return Ball()

    def createGoal(self) -> AbstractGoal:
        return Goal()

    def createPlayer(self) -> AbstractPlayer:
        return Player()
        
    def createPitch(self) -> AbstractPitch:
        return Pitch()