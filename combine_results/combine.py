#把准确率最高的放到第一个
#如果都只出现一次就按准确率最高的
#否则则按照次数最多的

import json
import os
import pandas as pd
from tqdm import tqdm

# select best files
with open('/home/flyingbird/Documents/reid_competition/combine_results/resnet152_ibn_best_model_epoch_150_submission_B.json','r') as json_max:
    json_dict_max = json.load(json_max)

# read fusion file
with open('/home/flyingbird/Documents/reid_competition/combine_results/ans.json','r') as json_max:
    json_dict_ans = json.load(json_max)


# select all other files
all_files = os.listdir('b_results')
#print(all_files)

create_variable = locals()

for i in range(len(all_files)):
    #create_variable['json_file_name_%i'%i]
    root = '/home/flyingbird/Documents/reid_competition/combine_results/b_results'
    path = os.path.join(root, all_files[i])
    with open(path, 'r') as json_file:
        create_variable['json_file_name_%i'%i] = json.load(json_file)


# loop static
for key in json_dict_max.keys():
    print(" ")
    print(key)
    
    #for j in tqdm(range(0,200)):
    key_num_list = []
    key_vote_list = []
    # read best files
    key_num_list += json_dict_max[key]

    # read all other files
    for num in range(len(all_files)):
        key_num_list += create_variable.get('json_file_name_'+str(num))[key]



        #json_file_name = exec('json_file_name_{}'.format(num))
        #print(json_file_name)
        #json_file_name = 'json_file_name_%i' % num
        # root = '/home/flyingbird/Documents/reid_competition/combine_results/all_submission_files'
        # path = os.path.join(root, all_files[num])
        # with open(path, 'r') as json_file:
        #     json_file_name = json.load(json_file)
        #file_name = 'json_file_name_%i'%num
        #print(create_variable.get('json_file_name_'+str(num)))
        #key_num_list.append(create_variable.get('json_file_name_'+str(num))[key][j])

    # stastic results
    counts_num_series = pd.value_counts(key_num_list)

    # find same id higher 1
    for i in range(len(counts_num_series)):
        if counts_num_series.values[i] > 1:
            key_vote_list.append(counts_num_series.index[i])

    print(len(key_vote_list))
    print(counts_num_series)

    # 200
    if len(key_vote_list) >= 200:
        key_vote_list = key_vote_list[:200]

    else:
        while len(key_vote_list) != 200:
            for i in json_dict_max[key]:
                if i not in key_vote_list:
                    key_vote_list.append(i)

    print(len(key_vote_list))

    # default
    json_dict_ans[key] = key_vote_list



    # if pd.value_counts(key_num_list).values[0] == 1:
    #     json_dict_ans[key] = json_dict_max[key][j]
    # else:
    #     json_dict_ans[key] = pd.value_counts(key_num_list).index[0]

with open('/home/flyingbird/Documents/reid_competition/combine_results/vote_best_results_b.json', 'w') as ans:
    json.dump(json_dict_ans, ans)


# with open('/home/flyingbird/Documents/reid_competition/combine_results/best_results.json', 'w') as ans:
#     json.dump(json_dict_max, ans)
    
