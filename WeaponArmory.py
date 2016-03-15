__author__ = 'saipc'

from Scene import Scene
from Corridor import Corridor
from EscapePod import EscapePod
from Bridge import Bridge

# WeaponArmory is a Scene
class WeaponArmory(Scene):
    def play(self):
        while True:
            choice = self.get_choice()
            if self.choices[0] == choice:
                print "Well, lets proceed"
                return True
            elif self.choices[1] == choice:
                print "Ouch, you need to work better"
                return True
            else:
                print "Invalid choice"


    def move_next_scene(self, scene = None):
        scene = scene or choice([Bridge, Corridor, EscapePod])
        super(WeaponArmory, self).move_next_scene(scene)

if __name__ == '__main__':
    # tiny bridge test driver
    name = raw_input('Enter your name: ')
    weapon_armory_scene = WeaponArmory(["Sword", "Gun"], name)
    weapon_armory_scene.enter()
    weapon_armory_scene.list_choices()
    weapon_armory_scene.play()
