__author__ = 'saipc'
from Scene import *

# bridge is also a scene
class Bridge(Scene):
    def enter(self, name):
        super(Bridge, self).enter(name)
        choices = []

