__author__ = 'saipc'
from Scene import *

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

if __name__ == '__main__':
    # tiny bridge test driver
    name = raw_input('Enter your name: ')
    bridge_scene = Bridge(["Jump", "Cross"])
    bridge_scene.enter(name)
    bridge_scene.list_choices()
    bridge_scene.play()
