__author__ = 'saipc'

from Scene import *
from random import *

# EscapePod is a scene
class EscapePod(Scene):

    def __init__(self, choices = None):
        choices = []
        x = 'Pod' + str(randint(10, 50))
        y = 'Pod' + str(randint(51, 100))
        choices.extend([x, y])
        # choice is from random
        self.right_choice = choice(choices)
        super(EscapePod, self).__init__(choices)

    def play(self):
        while True:
            choice = self.get_choice()
            if self.right_choice == choice:
                print "Congrats, you have chosen the right pod"
                return True
            else:
                print "Oops, wrong Pod, gg."
                return False

if __name__ == '__main__':
    # tiny bridge test driver
    name = raw_input('Enter your name: ')
    escape_pod_scene = EscapePod()
    escape_pod_scene.enter(name)
    escape_pod_scene.list_choices()
    escape_pod_scene.play()
