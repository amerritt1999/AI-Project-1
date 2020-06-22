import pandas as pd
from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import CategoricalNB
import json
import numpy as np 
import os

regions = ['Light World','Hyrule Castle','Eastern Palace' , 'Desert Palace' ,
           'Death Mountain' , 'Tower Of Hera' , 'Castle Tower' , 'Dark World','Dark Palace' , 
               'Swamp Palace' , 'Skull Woods' , 'Thieves Town','Ice Palace' , 'Misery Mire' , 
               'Turtle Rock' , 'Ganons Tower' , 'Special']
junkData = ['PieceOfHeart', 'HeartContainer', 'BossHeartContainer', 'OneRupee', 'FiveRupees', 'TwentyRupees', 
           'FiftyRupees', 'OneHundredRupees', 'ThreeBombs', 'TenBombs', 'TenArrows', 'BugCatchingNet',
           'ProgressiveShield']

counter2 = 0
arr2 = np.matrix('1,2;3,4')
fp = open("proj1.json")
data = json.load(fp)
for i in regions:
    li = list(data[i].items())
    counter2+=len(data[i].items())
    if li[0][1].split(':')[0] in junkData:
        arr = np.matrix(['junk', li[0][0].split(':')[0]])
    else:
        arr = np.matrix([li[0][1].split(':')[0], li[0][0].split(':')[0]])
    for j in range(1,len(li)):
        if li[j][1].split(':')[0] in junkData:
            arr = np.append(arr , [['junk', li[j][0].split(':')[0]]] , axis = 0)
        else:
            arr = np.append(arr , [[li[j][1].split(':')[0], li[j][0].split(':')[0]]] , axis = 0)
    for item in arr:
        arr2 = np.append(arr2, item, axis = 0)
arr4 = arr2[2:]

counter = 0
counter3 = 0
matrix = np.empty(shape=(25000*counter2,2),dtype='object')
for item in os.listdir('AI Data'):
    fp = open('AI Data/'+item)
    data = json.load(fp)
    for i in regions:
        li = list(data[i].items())
        for j in range(0,len(li)):
            if li[j][1].split(':')[0] in junkData:
                matrix[counter3][0] = 'junk'
                matrix[counter3][1] = li[j][0].split(':')[0]
            else:
                matrix[counter3][0] = li[j][1].split(':')[0]
                matrix[counter3][1] = li[j][0].split(':')[0]
            counter3+=1
    if counter == 24999:
        break
    counter+=1 

test = pd.DataFrame(matrix)
test2 = pd.DataFrame(arr4)

test.columns = ['Item', 'Location']
test2.columns = ['Item', 'Location']

oe = preprocessing.OrdinalEncoder()
le = preprocessing.LabelEncoder()

items = list(test.Item.values)
locations = list(test.Location.values)

test.Item = oe.fit_transform(test.Item.values.reshape(-1,1))
test.Location = le.fit_transform(test.Location.values)

counter = 0
dict1 = {}
for i in items:
    dict1[i] = test.Item.values[counter]
    counter+=1
    
counter = 0
dict2 = {}
for i in locations:
    dict2[str(test.Location.values[counter])] = i
    counter+=1
    
counter = 0
dict3 = {}
for i in dict2:
    dict3[str(counter)] = dict2[i]
    counter+=1

inputs = test.Item.values.reshape(-1,1)
target = test.Location.values

clf = CategoricalNB()

clf.fit(inputs, target)

list0 = []

for i in dict1:
    if i != 'junk':
        list0.append(i)

list2 = []
for i in list0:
    list2.append([dict1[i]])

list1 = clf.predict_proba(list2)

list3 = ['Turtle Rock Medallion', 'Misery Mire Medallion', 'Waterfall Bottle', 'Pyramid Bottle']

dict4 = {}
j = 0
for j in range(len(list1)):
    top_idx = np.argsort(list1[j])[-len(list1[j]):]
    top_values = [list1[j][i] for i in top_idx]
    counter = 0
    totalPercent = 0
    for i in top_idx[::-1]:
        if dict3[str(i)] not in list3:
            if dict3[str(i)] in test2.loc[test2['Item'] == 'unknown'].values:
                if dict3[str(i)] not in dict4:
                    dict4[dict3[str(i)]] = str(top_values[len(list1[j])-counter-1]*100)
                else:
                    if float(dict4[dict3[str(i)]]) < top_values[len(list1[j])-counter-1]*100:
                        dict4[dict3[str(i)]] = str(top_values[len(list1[j])-counter-1]*100)
                totalPercent+=top_values[len(list1[j])-counter-1]*100
                counter+=1
    j+=1

counter = 0
for i in dict4:
    print(i+": "+str(dict4[i])+"%")
    if counter == 10:
        break
    counter+=1
print('Done')