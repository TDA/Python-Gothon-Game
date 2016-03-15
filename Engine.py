from random import choice

__author__ = 'saipc'

from Bridge import Bridge
from Corridor import Corridor
from Death import Death
from EscapePod import EscapePod
from WeaponArmory import WeaponArmory

scenes = [
    None, # to fill for 0
    Bridge,
    Corridor,
    WeaponArmory,
    EscapePod
]

class Engine(object):

    def __init__(self, scene):
        # needs to initialize the map
        self.map = scene
        pass

    def play(self):
        Start_Class= choice([Bridge, Corridor, WeaponArmory, EscapePod])
        name = raw_input('Enter your name: ')
        scene = Start_Class(None, name)
        while scene != None:
            scene.enter()
            scene.list_choices()
            is_to_proceed = scene.play()
            if is_to_proceed == None:
                # means game over, exit
                exit(0)
            elif is_to_proceed == True:
                scene = scenes[scene.get_next_scene()](None, name) # move to the next scene
            else:
                scene = Death(None, name) # will auto exit on next iteration

        pass

if __name__ =='__main__':
    # write down the logic for the game here
    # define each stage and the next/prev
    # according to the flowchart
    # let each scene return the nextScene as part
    # of play, so that we can easily move across the game
    engine = Engine(None)
    engine.play()
    pass