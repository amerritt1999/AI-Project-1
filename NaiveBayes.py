from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import CategoricalNB
from sklearn import preprocessing
from sklearn import datasets
import json
import  numpy as np 
from pathlib import Path

# List all files in directory using pathlib
basepath = Path('AI Data/')
files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
arr2 = np.matrix('1,2;3,4')
regions = ['Light World','Hyrule Castle','Eastern Palace' , 'Desert Palace' ,
           'Death Mountain' , 'Tower Of Hera' , 'Castle Tower' , 'Dark World','Dark Palace' , 
               'Swamp Palace' , 'Skull Woods' , 'Thieves Town','Ice Palace' , 'Misery Mire' , 
               'Turtle Rock' , 'Ganons Tower' , 'Special']
junkData = ['PieceOfHeart', 'HeartContainer', 'BossHeartContainer', 'OneRupee', 'FiveRupees', 'TwentyRupees', 
           'FiftyRupees', 'OneHundredRupees', 'ThreeBombs', 'TenBombs', 'TenArrows', 'BugCatchingNet',
           'ProgressiveShield']
for item in files_in_basepath:
    fp = open(item)
    data = json.load(fp)
    for i in regions:
        li = list(data[i].items())
        arr = np.matrix([li[0][1].split(':')[0], li[0][0].split(':')[0].split(" - ")[0]])
        for j in range(1,len(li)):
            if li[j][1].split(':')[0] in junkData:
                arr = np.append(arr , [['junk', li[j][0].split(':')[0].split(' - ')[0]]] , axis = 0)
            else:
                arr = np.append(arr , [[li[j][1].split(':')[0], li[j][0].split(':')[0].split(' - ')[0]]] , axis = 0)
        for item in arr:
            arr2 = np.append(arr2, item, axis = 0)
    
arr3 = arr2[2:]
#print(arr3)
#arr3 should contain items and loctions
test = pd.DataFrame(arr3)
test.columns = ['Item', 'Location']

oe = preprocessing.OrdinalEncoder()
le = preprocessing.LabelEncoder()

items = list(test.Item.values)
locations = list(test.Location.values)

test.Item = oe.fit_transform(test.Item.values.reshape(-1,1))
test.Location = le.fit_transform(test.Location.values)

counter = 0
dict1 = {}
dict4 = {}
for i in items:
    dict1[str(test.Item.values[counter])] = i
    dict4[i] = test.Item.values[counter]
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

X_train, X_test, y_train, y_test = train_test_split(inputs,target,test_size=0.2)

clf = CategoricalNB()

clf.fit(X_train, y_train)

list1 = clf.predict_proba([[dict4['Hammer']], [dict4['Lamp']]])

j = 0
for j in range(len(list1)):
    top_idx = np.argsort(list1[j])[-len(list1[j]):]
    top_values = [list1[j][i] for i in top_idx]
    counter = 0
    totalPercent = 0
    for i in top_idx[::-1]:
        if dict3[str(i)] in test2.loc[test2['Item'] == 'unknown'].values:
            print(dict3[str(i)]+": "+str(top_values[len(list1[j])-counter-1]*100)+"%")
            totalPercent+=top_values[len(list1[j])-counter-1]*100
            counter+=1
        if counter == 10:
            break
    print("Total Percent: "+str(totalPercent)+"%")
    print()
    j+=1
