
class SpaceShip:
    def __init__(self):
        self.radius=12
        self.x=400
        self.y=400
        self.angle=90
        self.move_step=10

    def get_xy(self):
        return self.x,self.y

    def get_angle(self):
        return self.angle

    def left_move(self):
        self.angle=180
        self.x-=self.move_step

    def right_move(self):
        self.angle=0
        self.x+=self.move_step

    def up_move(self):
        self.angle=90
        self.y-=self.move_step

    def down_move(self):
        self.angle=-90
        self.y+=self.move_step