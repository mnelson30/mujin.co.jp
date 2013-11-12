#!/usr/bin/env python
from numpy import *
import scipy
A = array(scipy.misc.pilutil.imread('mujin_copyright.png'),uint32)
values = (A[:,:,2]+256*(A[:,:,1]+256*(A[:,:,0]+256*A[:,:,3]))).flat
f=open('watermark','w')
f.write('%d %d '%(A.shape[1],A.shape[0]))
for value in values:
    f.write(str(value) + ' ')
