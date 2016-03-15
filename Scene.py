__author__ = 'saipc'

class Scene(object):

    def __init__(self, choices, name):
        self.choices = choices
        self.name = name

    def enter(self):
        # this will automatically print the name of the class of which its an instance :D
        print 'Welcome to the %s, %s. What do you choose?' % (self.__class__.__name__, self.name)

    # let each scene have choices to make
    def list_choices(self):
        x = 1
        for choice in self.choices:
            print x, '. ', choice
            x += 1

    def move_next_scene(self, scene):
        self.next_scene = scene

    # this also belongs in the base class
    def get_choice(self):
        choice = raw_input("Enter the choice: ")
        return choice


