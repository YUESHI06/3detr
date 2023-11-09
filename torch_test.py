# -*- coding: utf-8 -*-
# @Author  : LG


def test():
    import torch
    print(torch.cuda.is_available())
    print(torch.zeros(1).cuda())

if __name__ == '__main__':
    test()