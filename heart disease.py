import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle

data = pd.read_csv('heart.csv')
print(data)
z=data.isnull().sum()
print(z)
d=data.describe()
print(d)
a=data['target'].value_counts()
print(a)
b=data['target'].value_counts()/data.shape[0]*100
print(b)

labels = ['yes', 'No']
values = data['target'].value_counts().values
plt.pie(values, labels=labels, autopct='%1.0f%%')
plt.title('Heart Disease')
plt.show()

#correlataion graph
plt.figure(figsize=(10,10))
x=sns.heatmap(data.corr(), annot=True, fmt='.0%')        
print(x)

g = sns.factorplot("chestpain", col = "ex-angina", col_wrap = 3, data = data[data['target'] == 1], kind = "count")
plt.xticks(np.arange(4), ('typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic'), rotation = 0)
g.fig.suptitle('People without Heart Disease', y = 1.1)
plt.show()

g = sns.factorplot("chestpain", col = "ex-angina", col_wrap = 3, data = data[data['target'] == 2], kind = "count")
plt.xticks(np.arange(4), ('typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic'), rotation = 0)
g.fig.suptitle('People with Heart Disease', y = 1.1)
plt.show()

sns.catplot(x = "slope", y = "oldpeak", hue = "target", data = data)
plt.title('The correlation between oldpeak and slope')
plt.xticks(np.arange(3), ('upsloping', 'flat', 'downsloping'), rotation = 0)
plt.show()

g = sns.catplot(x = 'Mjrvessels', y = 'age', hue = 'target', data = data, kind="swarm")
g.fig.suptitle('The correlation between No.of major vessels colored by flourosopy and age', y = 1.1)
plt.show()

sns.relplot(x = 'age', y = 'heart rate', data = data, hue = 'target', legend="full")
plt.title('The correlation between age and heart rate')
plt.show()

x=data.iloc[:,:-1].values #featuring data
y=data.iloc[:,-1].values #target data
x_train,x_test, y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=1)
def fit_eval_model(model, train_features, y_train, test_features, y_test):  
    
     results={}
     model.fit(train_features, y_train) #training
     
     train_predicted = model.predict(train_features) #testing
     test_predicted = model.predict(test_features)
     
     results['classification_report'] = classification_report(y_test, test_predicted)
     return results
 
svm = SVC(random_state = 1)

results = {}
for cls in [svm]:
    cls_name = cls.__class__.__name__
    results[cls_name] = {}
    results[cls_name] = fit_eval_model(cls,x_train, y_train,x_test, y_test)
    
for result in results:
    print (result)
    
    for i in results[result]:
        print (i, ':')
        print(results[result][i])
        
        
rf = RandomForestClassifier(random_state = 1)      
results = {}
for cls in [rf]:
    cls_name = cls.__class__.__name__
    results[cls_name] = {}
    results[cls_name] = fit_eval_model(cls,x_train, y_train,x_test, y_test)
    
for result in results:
    print (result)  
    for i in results[result]:
        print (i, ':')
        print(results[result][i])
        
forest=RandomForestClassifier(n_estimators=10, criterion='entropy',random_state=1)
forest.fit(x_train,y_train)
model=forest
#Hence the Rf is more precise so we have to check its accuracy 
print('THE ACCURACY OF RF IS =', model.score(x_train,y_train))

with open('heart.pkl', 'wb') as file:
    pickle.dump(rf,file)
    

          

     
        
     