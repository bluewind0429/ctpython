# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 21:51:13 2021

@author: USER
"""
n=int(input("輸入一個範圍的整數:"))
c=2
while c<n:
    if n%c==0:
        print("不是質數")
        break
    c+=1
    print("是質數")

if c==n:
    print('是質數')

print('_'*30)

a=int(input("輸入一個範圍的整數:"))

for i in range(1,a):
    if i%4==0: 
        print(i,"是4的倍數")



    
    
    

    

       
       