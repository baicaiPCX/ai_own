import torch
import torch.nn as nn

class Brain(nn.Module):
    def __init__(self,input_dim,output_dim,num_hidden_layers=3,hidden_layer_dim=5):
        super(Brain, self).__init__()
        self.nets=nn.ModuleList()
        tmp_input_dim=input_dim
        for i in range(num_hidden_layers):
            sub_net=nn.Sequential(
                nn.Linear(tmp_input_dim,hidden_layer_dim),
                nn.ReLU(True)
            )
            self.nets.append(sub_net)
            tmp_input_dim=hidden_layer_dim
        self.nets.append(nn.Sequential(
            nn.Linear(hidden_layer_dim,output_dim),
            nn.Softmax(dim=1)
        ))

    def forward(self,input):
        x=self.nets[0](input)
        for net in self.nets[1:]:
            x=net(x)
        return x