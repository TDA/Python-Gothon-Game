__author__ = 'saipc'
from Scene import *
#
# from Corridor import Corridor
# from EscapePod import EscapePod
# from WeaponArmory import WeaponArmory
from random import * # for choice()

# bridge is also a scene
class Bridge(Scene):

    def __init__(self, choices = None, name = None):
        choices = choices or ["Jump", "Cross"]
        super(Bridge, self).__init__(choices, name)

    def play(self):
        while True:
            choice = self.get_choice()
            if self.choices[0] == choice:
                print "Oops, you died"
                return False
            elif self.choices[1] == choice:
                print "Great, you crossed"
                return True
            else:
                print "Invalid choice, choose again"

    def get_next_scene(self, scene = None):
        scene = scene or choice([2, 3, 4])
        return scene

if __name__ == '__main__':
    # tiny bridge test driver
    name = raw_input('Enter your name: ')
    bridge_scene = Bridge(["Jump", "Cross"], name)
    bridge_scene.enter()
    bridge_scene.list_choices()
    bridge_scene.play()
    # bridge_scene.move_next_scene()
    # print(bridge_scene.next_scene)
