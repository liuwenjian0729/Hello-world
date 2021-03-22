#!/usr/bin/env python                                                                                                                   

print ("start call  so file\n")

from ctypes import *


# dlopen libmath.so file
handle = cdll.LoadLibrary("./lib/libmath.so")

# test inteface
handle.Test()

# caculate algo inteface
add =handle.add
add.argtypes = [c_float, c_float] 
add.restype = c_float

sum = add(1.3, 13.4)
print ('sum = %.1f' % sum)
