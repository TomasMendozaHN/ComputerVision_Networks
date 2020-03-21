import torch

class ResidualBlock(torch.nn.module):
    def __init__(self):
        super(ResidualBlock, self).__init__()

        self.conv_1 = torch.nn.Conv2d()



class ResNet(torch.nn.module):
    def __init__(self, stride=1, n_classes=1000):
        super(ResNet, self).__init__()
