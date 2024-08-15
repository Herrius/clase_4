import pandas as pd

edad=pd.Series(range(1,11))
print(edad)

bacteria=pd.Series(range(1,21,2),index=range(1,11))
print(bacteria)
print(bacteria.values,bacteria.index)
print(bacteria.describe())

bacteria_dict = pd.DataFrame({'a': [10, 11, 12], 'b': [20, 21, 22], 'c': [30, 31, 32], 'd': [40, 41, 42], 'e': [50, 51, 52]})
print(bacteria_dict)
print(bacteria_dict.values,bacteria_dict.index)
print(bacteria_dict.describe())
print(bacteria_dict.sum())
bacteria_dict=pd.DataFrame(list(bacteria_dict.items()),columns=['indice','valores'])
bacteria_dict=bacteria_dict['valores'].explode().astype('int')
print(bacteria_dict.sum())