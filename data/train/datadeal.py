#coding = utf-8

import os

train_img_path = '/home/flyingbird/Documents/reid_competition/train/train_set'
train_txt_path = '/home/flyingbird/Documents/reid_competition/train/train_list.txt'
# test_img_path = '/home/zx/zxfile/contest/deep-person-reid-master/torchreid/data/contestdata/query'
# test_txt_path = '/home/zx/zxfile/contest/deep-person-reid-master/torchreid/data/contestdata/query_a_list.txt'
num=0
with open(train_txt_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        line=line.strip('\n').split(' ')
        #img_id = int(line[1])
        img_id = line[1].zfill(4)
        img_name = line[0].split('/')[1]
        cam_id = 'c1'
        src = os.path.join(os.path.abspath(train_img_path),img_name)
        dst = os.path.join(os.path.abspath(train_img_path),format(str(img_id),'0>4s')+'_'+cam_id+'_'+img_name[:-4]+'.png')

        try:
            os.rename(src,dst)
            num+=1
            print('convert %s to %s..' % (src, dst))
        except:
            continue

print ('total %d to rename ' % (num))

