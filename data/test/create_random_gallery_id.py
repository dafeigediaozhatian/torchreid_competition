#coding = utf-8
import numpy as np
import os

# create query_list
# query_b_list = os.listdir('query_b')
# num_query_b = [i for i in range(4768, 4768+3147)]
# print(len(query_b_list))
# print(len(num_query_b))
#
# with open('query_b_list.txt', 'w') as file:
#     for i in range(len(query_b_list)):
#         line = 'query_b/' + str(query_b_list[i]) + ' ' + str(num_query_b[i]) + '\n'
#         file.write(line)





test_img_path = '/home/flyingbird/Documents/reid_competition/test/gallery_b'
test_txt_path = '/home/flyingbird/Documents/reid_competition/test/query_b_list.txt'

querry_id_list = []

with open(test_txt_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        line=line.strip('\n').split(' ')
        #img_id = int(line[1])
        querry_id_list.append(line[1])
        #img_name = line[0].split('/')[1]
print(len(querry_id_list))

gallery_id_list = np.random.choice(querry_id_list, 13099, replace=True)
# print(len(gallery_id_list))
# #print(np.array(gallery_id_list).max())
# #print(np.array(querry_id_list).max())
# print(max(querry_id_list))
# print(max(gallery_id_list))
#
# print(min(querry_id_list))
# print(min(gallery_id_list))

# create fake gallery list
gallery_root = '/home/flyingbird/Documents/reid_competition/test/gallery_b'

gallery_img_list = os.listdir(gallery_root)

save_gallery_txt_name = 'gallery_b_list.txt'

with open(save_gallery_txt_name, 'w') as file:
    #lines = file.readlines()
    for i in range(len(gallery_img_list)):
        #line=line.strip('\n').split(' ')
        #img_id = int(line[1])
        #querry_id_list.append(line[1])
        lines = 'gallery_b/' + gallery_img_list[i] + ' ' + gallery_id_list[i] + '\n'
        file.write(lines)
        #file.close()