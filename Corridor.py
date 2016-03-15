__author__ = 'saipc'
from Scene import Scene
# from EscapePod import EscapePod
# from WeaponArmory import WeaponArmory
# from Bridge import Bridge
from random import * # for choice()

# corridor is a scene
class Corridor(Scene):

    def __init__(self, choices=None, name=None):
        choices = choices or ["Left", "Right"]
        super(Corridor, self).__init__(choices, name)

    def play(self):
        while True:
            choice = self.get_choice()
            if self.choices[0] == choice:
                print "Well, its not the right choice"
                return False
            elif self.choices[1] == choice:
                print "Great, you move to the next stage"
                return True
            else:
                print "Invalid choice, choose again"

    def get_next_scene(self, scene = None):
        scene = scene or choice([1, 3, 4])
        return scene


if __name__ == '__main__':
    # tiny bridge test driver
    name = raw_input('Enter your name: ')
    corridor_scene = Corridor(["Left", "Right"], name)
    corridor_scene.enter()
    corridor_scene.list_choices()
    corridor_scene.play()
    # corridor_scene.move_next_scene()
    # print(corridor_scene.next_scene)
