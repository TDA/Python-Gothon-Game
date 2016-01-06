__author__ = 'saipc'

class Scene(object):
    def enter(self, name):
        print 'Welcome', name, 'What do you choose?'

    # let each scene have choices to make
    def list_choices(self, choices):
        x = 1
        for choice in choices:
            print x, '. ', choice

    # this also belongs in the base class
    def get_choice(self):
        choice = raw_input("Enter the choice number")
        return choice


