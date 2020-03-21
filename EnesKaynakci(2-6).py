# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 13:16:05 2020

@author: enes_
"""


#part1
import numpy as np
mymatx= np.arange(1,201)
mymatx= mymatx[mymatx%2==0].reshape(10,10)



#part2
def arraygen(height,width):
    array= np.zeros((height,width))
    array[:,0]=1
    array[:,width-1]=1
    array[0,:] = 1
    array[height-1,:] = 1
    return array
    
            





    