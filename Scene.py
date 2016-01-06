__author__ = 'saipc'

class Scene(object):

    def __init__(self, choices):
        self.choices = choices

    def enter(self, name):
        print 'Welcome %s to the %s. What do you choose?' % (name, self.__class__.__name__)

    # let each scene have choices to make
    def list_choices(self):
        x = 1
        for choice in self.choices:
            print x, '. ', choice
            x += 1

    # this also belongs in the base class
    def get_choice(self):
        choice = raw_input("Enter the choice: ")
        return choice


