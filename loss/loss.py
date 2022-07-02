import torch
import torch.nn as nn

class MSELoss(nn.MSELoss):
    def __init__(self):
        super(MSELoss, self).__init__()
        self.loss=nn.MSELoss()
        self.target=torch.zeros(1).cuda()+0.1

    def forward(self,pred,id):
        l=self.loss(pred[id],self.target)
        return l