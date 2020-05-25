from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import datasets
import json
import  numpy as np 
from pathlib import Path

# List all files in directory using pathlib
basepath = Path('AI Data/')
files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
arr2 = np.matrix('1,2;3,4')
for item in files_in_basepath:
    fp = open(item)
    data = json.load(fp)
    regions = ['Light World','Hyrule Castle','Eastern Palace' , 'Desert Palace' ,
           'Death Mountain' , 'Tower Of Hera' , 'Castle Tower' , 'Dark World','Dark Palace' , 
               'Swamp Palace' , 'Skull Woods' , 'Thieves Town','Ice Palace' , 'Misery Mire' , 
               'Turtle Rock' , 'Ganons Tower' , 'Special']
    
    for i in regions:
        li = list(data[i].items())
        arr = np.matrix([li[0][1].split(':')[0], li[0][0].split(':')[0]])
        for j in range(1,len(li)):
            arr = np.append(arr , [[li[j][1].split(':')[0], li[j][0].split(':')[0]]] , axis = 0)
        for item in arr:
            arr2 = np.append(arr2, item, axis = 0)
    
arr3 = arr2[2:]
#print(arr3)
#arr3 should contain items and loctions
test = pd.DataFrame(arr3)
test.columns = ['Item', 'Location']
test.head()

#X_train, X_test, y_train, y_test = train_test_split(inputs,target,test_size=0.2)
#model = MultinomialNB()
#model.fit(X_train, y_train)
#print(model.predict_proba(X_test[:10]))