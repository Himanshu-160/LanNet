import torch
import torch.nn as nn
import torch.nn.functional as F



class LanNet(nn.Module):
    def __init__(self, num_language):
        super(LanNet,self).__init__()
        
        self.C1 = nn.Conv2d(1,16,kernel_size=(3,3),stride=(1,1), padding=(2,2))
        self.C2 = nn.Conv2d(16,32,kernel_size=(3,3),stride=(1,1) , padding=(2,2))
        self.C3 = nn.Conv2d(32,64,kernel_size=(3,3),stride=(1,1), padding=(2,2))
        self.C4 = nn.Conv2d(64,128,kernel_size=(3,5), padding=(2,3))
        self.C5 = nn.Conv2d(128,256,kernel_size=(3,5), padding=(2,3))
         
        self.maxpool1 = nn.MaxPool2d((2,3),(2,2))
        self.maxpool2 = nn.MaxPool2d((1,5),(1,5))
        self.avgpool1= nn.AvgPool2d((3,3),(3,3))
        
        self.fc1 = nn.Linear(1024,64)
        self.fc2 = nn.Linear(64,num_language)
        self.dropout = nn.Dropout(0.25)

        
    def forward(self,x):
        
        x = self.maxpool1(F.relu(self.C1(x)))
        x = self.maxpool1(F.relu(self.C2(x)))
        x = self.maxpool1(F.relu(self.C3(x)))
        x = self.maxpool1(F.relu(self.C4(x)))
        x = self.maxpool1(F.relu(self.C5(x)))
        x = self.avgpool1(x)
    
        x = x.view(-1,1024)
        
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        
        return x