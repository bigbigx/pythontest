# -*- coding: utf-8 -*-

print("multiplication Table")
for i in range(1,10):
    for j in range(1,i+1):
        print(j,"*",i,"=",i*j,"\t",end='')
    print(" ")