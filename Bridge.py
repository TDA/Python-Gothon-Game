__author__ = 'saipc'
from Scene import *

from Corridor import *
from EscapePod import *
from WeaponArmory import *
from random import * # for choice()

# bridge is also a scene
class Bridge(Scene):
    def play(self):
        while True:
            choice = self.get_choice()
            if "Jump" == choice:
                print "Oops, you died"
                return False
            elif "Cross" == choice:
                print "Great, you crossed"
                return True
            else:
                print "Invalid choice"

    def move_next_scene(self, scene = None):
        scene = scene or choice([Corridor, WeaponArmory, EscapePod])
        super(Bridge, self).move_next_scene(scene)

if __name__ == '__main__':
    # tiny bridge test driver
    name = raw_input('Enter your name: ')
    bridge_scene = Bridge(["Jump", "Cross"], name)
    bridge_scene.enter()
    bridge_scene.list_choices()
    bridge_scene.play()
    bridge_scene.move_next_scene()
    print(bridge_scene.next_scene)
