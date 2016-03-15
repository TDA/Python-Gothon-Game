from Scene import *
# from Bridge import Bridge
# from Corridor import Corridor
# from WeaponArmory import WeaponArmory
from random import *
__author__ = 'saipc'

# EscapePod is the final scene
class EscapePod(Scene):

    def __init__(self, name):
        choices = []
        x = 'Pod' + str(randint(10, 50))
        y = 'Pod' + str(randint(51, 100))
        choices.extend([x, y])
        # choice is from random
        self.right_choice = choice(choices)
        super(EscapePod, self).__init__(choices, name)

    def play(self):
        while True:
            choice = self.get_choice()
            if self.right_choice == choice:
                print "Congrats, you have chosen the right pod"
                return True
            else:
                print "Oops, wrong Pod, gg."
                return False

    def move_next_scene(self, scene = None):
        scene = scene or choice([Corridor, WeaponArmory, Bridge])
        super(EscapePod, self).move_next_scene(scene)

if __name__ == '__main__':
    # tiny bridge test driver
    name = raw_input('Enter your name: ')
    escape_pod_scene = EscapePod(name)
    escape_pod_scene.enter()
    escape_pod_scene.list_choices()
    escape_pod_scene.play()
