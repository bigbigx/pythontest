# -*- coding: utf-8 -*-

print("multiplication Table")

with open('data.txt','w') as f:    #设置文件对象
       
 for i in range(1,10):
    for j in range(1,i+1):
       
       num= str(i*j)
   
       f.write('i*j = '+ num )
   
  