from sklearn import datasets
import json
import  numpy as np 

li=[]

fp = open('proj1.json')

data = json.load(fp)

li = list(data['Equipped'].items())

arr = np.array([li[0]])
#pi = list(data['Light World'].items())
#hc = list(data['Hyrule Castle'].items())
#ep = list(data['Eastern Palace'].items())

#print(len(li))
#print(len(pi))
#print(len(hc))
#print(len(ep))

regions = ['Light World' , 'Hyrule Castle','Eastern Palace' , 'Desert Palace' ,
           'Death Mountain' , 'Tower Of Hera' , 'Castle Tower' , 'Dark World','Dark Palace' , 'Swamp Palace' , 'Skull Woods' , 'Thieves Town','Ice Palace' , 'Misery Mire' , 'Turtle Rock' , 'Ganons Tower' , 'Special']

for i in regions:
    temp = list(data[i].items())
    for j in range(0,len(temp)):
        arr = np.append(arr , [temp[j]] , axis = 0)


print(arr)














