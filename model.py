import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        # c: channel size
        # r: receptive field size
        # j: jump
        self.conv1 = nn.Conv2d(1, 32, 3, bias=False) # c=26, r=3, j=1
        self.conv2 = nn.Conv2d(32, 64, 3, bias=False) # c=24, r=5, j=1
        self.pool1 = nn.MaxPool2d(2, stride=2) # c=12, r=6, j=2
        self.conv3 = nn.Conv2d(64, 128, 3, bias=False) # c=10, r=10, j=2
        self.conv4 = nn.Conv2d(128, 256, 3, bias=False) # c=8, r=14, j=2
        self.pool2 = nn.MaxPool2d(2, stride=2) # c=4, r=16, j=4
        self.fc1 = nn.Linear(4*4*256, 50, bias=False)
        self.fc2 = nn.Linear(50, 10, bias=False)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = self.pool1(x)
        x = F.relu(self.conv3(x))
        x = F.relu(self.conv4(x))
        x = self.pool2(x)
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)
