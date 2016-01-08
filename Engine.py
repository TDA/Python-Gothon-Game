__author__ = 'saipc'

from Map import *
from Bridge import *
from Corridor import *
from Death import *
from EscapePod import *
from WeaponArmory import *


class Engine(object):

    def __init__(self, scene):
        # needs to initialize the map
        self.map = Map()
        pass

    def play(self):
        pass

if __name__ =='__main__':
    # write down the logic for the game here
    # define each stage and the next/prev
    # according to the flowchart
    # let each scene return the nextScene as part
    # of play, so that we can easily move across the game
    pass