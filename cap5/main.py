import pandas as pd

labels = ['a', 'b', 'c']

data = [10, 20, 30]

s = pd.Series(data, index=labels)

print(s)

s1 = pd.Series({'a': 10, 'b': 20, 'c': 30})
s2 = pd.Series({'a': 100, 'c': 200, 'd': 300})
print(s1.add(s2, fill_value=0))


print(s1[s1/2 >10])