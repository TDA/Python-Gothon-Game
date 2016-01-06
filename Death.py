__author__ = 'saipc'

from Scene import *

# death is a scene
class Death(Scene):
    # death scene doesnt have choices or anything
    # so override
    def list_choices(self):
        pass

    def get_choice(self):
        pass

    def enter(self, name):
        print "Oops, looks like you chose the wrong way :("
        print "Sorry %s, but Game Over" % (name)
        # should also print points
        # print "You scored %d points" % points
        exit(0)
    # does not have a play method

if __name__ == '__main__':
    # tiny bridge test driver
    name = raw_input('Enter your name: ')
    death_scene = Death(None)
    death_scene.enter(name)

