# Titanic
# importar librerias
import pandas as pd
from matplotlib import pyplot as plt

#Leer dataset
titanic=pd.read_csv('titanic.csv')
# exploracion inicial
print(titanic.head())
print(titanic.describe())
print(titanic.dtypes)
#
print(titanic['Sex'].value_counts())
print(titanic['Age'].isnull().sum())

df=pd.read_csv('titanic.csv',usecols=['PassengerId',"Survived","Pclass","Sex"])
print(df.head())

print(df.shape)

import matplotlib
df.hist(column='Survived',by='Pclass',grid=False,layout=[1,3],figsize=[10,3])
plt.show()

df.hist('Survived',by='Sex',grid=False,layout=[1,2],figsize=[10,3])
plt.show()