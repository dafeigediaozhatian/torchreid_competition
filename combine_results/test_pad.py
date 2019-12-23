import pandas as pd

a = [1, 2, 3, 3, 4, 2, 1, 5, 1]
b = [7, 5, 4]

c = pd.value_counts(a)
print(pd.value_counts(a))
for i in range(len(pd.value_counts(a))):
    if c.values[i] > 1:
        print(c.index[i])
