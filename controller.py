from venerable.model import Model
from tkinter import *
from venerable.view import View1, View2


class Control:

    def __init__(self, root):
        self.root = root
        self.view1 = View1(root)
        self.model = Model(self.view1)