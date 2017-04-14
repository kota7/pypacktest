# -*- coding: utf-8 -*-

from argparse import ArgumentParser
import testpack.math

def magic_square():
    parser = ArgumentParser(description='Return a magic square of size 3 or 4')
    parser.add_argument('n', type=int, help='square size')
    args = parser.parse_args()
    
    if args.n in [3,4]:
        x = testpack.math.magic_square(args.n)
        for i in range(len(x)):
            for j in range(len(x[i])):
                print('%3d' % x[i,j], end=' ')
            print('')
    else:
        print('currently only n = 3 or 4 is supported')
        return 
