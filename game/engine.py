
from game.actor import SpaceShip

class Engine:
    def __init__(self,gui_class):
        self.GUI=gui_class(800,800)
        self.spaceships=SpaceShip()

    def run_game(self):
        while True:
            self.GUI.back_events(self)
            self.GUI.update_frame(self.spaceships)

    def left_down(self):
        self.spaceships.left_move()

    def right_down(self):
        self.spaceships.right_move()

    def up_down(self):
        self.spaceships.up_move()

    def down_down(self):
        self.spaceships.down_move()