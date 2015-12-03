#!/bin/python3

import sys

t = int(input().strip())
a = {0:(0,0), 1:(-3,2), 2:(-1,1), 3:(1,0), 4:(-2,2), 
     5:(0,1), 6:(2,0), 7:(-1,2), 8:(1,1), 9:(3,0),
     10:(0,2), 11:(2,1), 12:(4,0), 13:(1,2), 14:(3,1)}

for a0 in range(t):
    n = int(input().strip())
    if n in (1, 2, 4, 7):
        print('-1')
    else:
        remainder = n % 15
        quotient = int(n / 15)
        
        b, c = a[remainder]
        b += quotient*5
        
        
        print ('{}{}'.format('555'*b, '33333'*c))
