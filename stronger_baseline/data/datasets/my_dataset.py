import sys
import os
import os.path as osp
import random

#from data.datasets.dataset_loader import ImageDataset
#from torchreid.data import ImageDataset

def NewDataset(list_name, root):
    #dataset_dir = 'my_dataset'
    #def __init__(self, dataset_train_list_dir, dataset_query_list_dir, dataset_gallery_list_dir, root='', **kwargs):

    #def init__(self, dataset_train_list_name, root='', **kwargs):
        # self.root = osp.abspath(osp.expanduser(root))
        # self.dataset_train_list_dir = osp.join(self.root, dataset_train_list_name)
        #self.dataset_query_list_dir = osp.join(self.root, dataset_query_list_dir)
        #self.dataset_gallery_list_dir = osp.join(self.root, dataset_gallery_list_dir)

        # All you need to do here is to generate three lists,
        # which are train, query and gallery.
        # Each list contains tuples of (img_path, pid, camid),
        # where
        # - img_path (str): absolute path to an image.
        # - pid (int): person ID, e.g. 0, 1.
        # - camid (int): camera ID, e.g. 0, 1.
        # Note that
        # - pid and camid should be 0-based.
        # - query and gallery should share the same pid scope (e.g.
        #   pid=0 in query refers to the same person as pid=0 in gallery).
        # - train, query and gallery share the same camid scope (e.g.
        #   camid=0 in train refers to the same camera as camid=0
        #   in query/gallery).
        #train = ...
        #query = ...
        #gallery = ...
        #super(NewDataset, self).__init__(train, query, gallery, **kwargs)

    #root = osp.abspath(osp.expanduser(root))
    dataset_list_dir = osp.join(root, list_name)

    all_list = []
    all_id_list = []

    #train_list = []
    #val_list = []
    # if mode == 'Train':
    #     img_root = '/home/flyingbird/Documents/reid_competition/train/train_set'
    # else:
    #     img_root = '/home/flyingbird/Documents/reid_competition/test'

    with open(dataset_list_dir, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(' ')
            train_pid = int(line[1])
            all_id_list.append(train_pid)
            cam_id = 0
            #if mode == 'Train':
            img_name = line[0]
            #else:
            #    img_name = line[0]
            img_path = os.path.join(root,img_name)
            img_data = (img_path, train_pid, cam_id)
            all_list.append(img_data)

    num_train_pids = len(set(all_id_list))

    return all_list, num_train_pids