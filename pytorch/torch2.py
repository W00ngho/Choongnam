import torch1
from torch1 import Torch

class PyTorch(Torch):
    def __init__(self, name):
        super().__init__(name)
        self.pyname = 'py최수길'

    def __str__(self):
        return print('파이네임: ' + self.pyname + '\n이름은 :' + self.name)

    def __gt__(self, value):
        return self.pyname == value.pyname



def main():
    # t = torch1.Torch('최수길')
    t = Torch('최수길')
    t2 = PyTorch('최마우개')
    t3 = PyTorch('최마우개')
    t.print()

    t2.print()
    print(t2)
    # print(isinstance(t, object))
    # 비교연산자 __eq__ -> == 
    print(t2 == t3)
    # 비교연산자 __gt__ -> [ 크다 < ],  __le__ -> [ 작다 > ],  __ne__ ->  




if __name__ == '__main__':
    main()