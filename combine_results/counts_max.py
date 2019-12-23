# a = [1, 2, 3, 4, 4, 2, 4, 3]
#
# import pandas as pd
#
# print(pd.value_counts(a).values[0])
# print(pd.value_counts(a).index[0])
# print(type(pd.value_counts(a)))

# createVar = locals()
# listTemp = range(1,10)
# for i,s in enumerate(listTemp):
#     createVar['a'+str(i)] = s
# b = [a1, a2, a3]
# print(b[0])

import json

path = '/home/flyingbird/Documents/reid_competition/combine_results/vote_best_results_b.json'

with open(path, 'r', encoding='utf-8') as ans:
    best_results = json.load(ans)

key_list = []
for i in best_results.keys():
    #print(i)
    if len(best_results[i]) != len(set(best_results[i])):
        print(i)

print('game over!')
    #print(len(best_results[i]))
    #print(len(set(best_results[i])))
# print(key_list)
# print(len(key_list))
# print(len(set(key_list)))
# print(best_results.keys())
# print(len(best_results.keys()))
# print(len(set(best_results.keys())))