__author__ = 'saipc'
from Scene import *
from EscapePod import *
from WeaponArmory import *
from random import * # for choice()
from Bridge import *
# corridor is a scene
class Corridor(Scene):
    def play(self):
        while True:
            choice = self.get_choice()
            if "Left" == choice:
                print "Well, lets proceed"
                return False
            elif "Right" == choice:
                print "Great, you move to the next stage"
                return True
            else:
                print "Invalid choice"

    def move_next_scene(self, scene = None):
        scene = scene or choice([Bridge, WeaponArmory, EscapePod])
        super(Corridor, self).move_next_scene(scene)

if __name__ == '__main__':
    # tiny bridge test driver
    name = raw_input('Enter your name: ')
    corridor_scene = Corridor(["Left", "Right"], name)
    corridor_scene.enter()
    corridor_scene.list_choices()
    corridor_scene.play()
    corridor_scene.move_next_scene()
    print(corridor_scene.next_scene)
