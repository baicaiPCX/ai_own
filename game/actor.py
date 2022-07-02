from model.model import Brain
from loss.loss import MSELoss
import torch
from torch.optim.adam import Adam

import numpy as np

class SpaceShip:
    def __init__(self):
        self.radius=30
        self.x=400
        self.y=400
        self.angle=90
        self.move_step=10

        self.radar_range=50
        self.wind_width=800
        self.wind_height=800

        self.is_collision=False
        self.distances=None

        # learn
        self.brain=Brain(4,4,num_hidden_layers=3,hidden_layer_dim=10).cuda()
        self.loss=MSELoss().cuda()
        self.opt=Adam(self.brain.parameters(),lr=0.002)
        self.brain.train()

    def update_frame(self):
        if self.is_collision:
            self.x=400
            self.y=400
            self.distances = None
            self.is_collision = False
            print("has collision, distance:",self.distances)
            return True # has collision currently.
        if self.distances is None:
            self.distances=self.radar_detect()
        distances=self.distances
        input=np.array([distances]).astype(np.float32)
        input_tensor=torch.from_numpy(input).cuda()
        output_tensor=self.brain(input_tensor)[0]
        output=output_tensor.cpu().detach().numpy()
        next_id=np.argmax(output)

        func_move = [self.left_move, self.right_move, self.up_move, self.down_move]
        func_move[next_id]()
        distances = self.radar_detect()
        self.distances=distances
        id_collision=self.collision_detect(*distances)
        if id_collision is None:
            return False
        self.is_collision=True
        print("brain learning...")

        loss=self.loss(output_tensor,id_collision)
        self.opt.zero_grad()
        loss.backward()
        self.opt.step()

        return False



    def get_xy(self):
        return self.x,self.y

    def get_angle(self):
        return self.angle

    def radar_detect(self):
        # detect distance to bound
        l_d=self.x if self.x<self.radar_range else self.radar_range
        r_d=self.radar_range if self.wind_width-self.x > self.radar_range else self.wind_width-self.x
        u_d=self.y if self.y<self.radar_range else self.radar_range
        d_d=self.radar_range if self.wind_height-self.y > self.radar_range else self.wind_height-self.y

        return l_d,r_d,u_d,d_d

    def collision_detect(self,ld,rd,ud,dd):
        if ld<self.radius:
            return 0 # return id of side collision with ship
        if rd<self.radius:
            return 1
        if ud<self.radius:
            return 2
        if dd<self.radius:
            return 3
        return None


    def left_move(self):
        print("move left")
        self.angle=180
        self.x-=self.move_step

    def right_move(self):
        print("move right")
        self.angle=0
        self.x+=self.move_step

    def up_move(self):
        print("move up")
        self.angle=90
        self.y-=self.move_step

    def down_move(self):
        print("move down")
        self.angle=-90
        self.y+=self.move_step