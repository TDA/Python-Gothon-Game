from random import choice

__author__ = 'saipc'

from Scene import Scene

# WeaponArmory is a Scene
class WeaponArmory(Scene):

    def __init__(self, choices=None, name=None):
        choices = choices or ["Sword", "Gun"]
        super(WeaponArmory, self).__init__(choices, name)

    def play(self):
        while True:
            choice = self.get_choice()
            if self.choices[0] == choice:
                print "Well, lets proceed"
                return True
            elif self.choices[1] == choice:
                print "Ouch, you need to work better"
                return False
            else:
                print "Invalid choice, choose again"


    def get_next_scene(self, scene = None):
        scene = scene or choice([1, 2, 4])
        return scene

if __name__ == '__main__':
    # tiny bridge test driver
    name = raw_input('Enter your name: ')
    weapon_armory_scene = WeaponArmory(["Sword", "Gun"], name)
    weapon_armory_scene.enter()
    weapon_armory_scene.list_choices()
    weapon_armory_scene.play()
