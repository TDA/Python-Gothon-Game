__author__ = 'saipc'

from Scene import *

# WeaponArmory is a Scene
class WeaponArmory(Scene):
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

if __name__ == '__main__':
    # tiny bridge test driver
    name = raw_input('Enter your name: ')
    weapon_armory_scene = WeaponArmory(["Sword", "Gun"])
    weapon_armory_scene.enter(name)
    weapon_armory_scene.list_choices()
    weapon_armory_scene.play()
