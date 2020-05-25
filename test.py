#this will take 90 files and will create a data matrix #
#just create a folder with the files in present working directory and edit the path will work fine for you.
# 
# we just need naive bayes working on this data.

from sklearn import datasets
import json
import  numpy as np
import os

li=[]

fc = 0

fp = open('proj1.json')

data = json.load(fp)

li = list(data['Equipped'].items())

arr = np.array([li[0]])


for i in range(1,3):
    arr = np.append(arr,[li[i]] , axis = 0)




regions = ['Equipped','Light World' , 'Hyrule Castle','Eastern Palace' , 'Desert Palace' ,
           'Death Mountain' , 'Tower Of Hera' , 'Castle Tower' , 'Dark World','Dark Palace' , 'Swamp Palace' , 'Skull Woods' , 'Thieves Town','Ice Palace' , 'Misery Mire' , 'Turtle Rock' , 'Ganons Tower' , 'Special']


for f in os.listdir('/home/aaaaaaaa/AI/fd'):
   # print(f)
    fp = open('./fd' + '/'+f)
    data = json.load(fp)
    fc = fc + 1
    if(fc >90):
        break

    for i in regions:
        temp = list(data[i].items())
        for j in range(0,len(temp)):
            arr = np.append(arr , [temp[j]] , axis = 0)
    
print(arr.shape)














