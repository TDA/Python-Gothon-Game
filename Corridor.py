__author__ = 'saipc'
from Scene import *
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

if __name__ == '__main__':
    # tiny bridge test driver
    name = raw_input('Enter your name: ')
    corridor_scene = Corridor(["Left", "Right"])
    corridor_scene.enter(name)
    corridor_scene.list_choices()
    corridor_scene.play()
