# encoding: utf-8
"""
@author:  liaoxingyu
@contact: sherlockliao01@gmail.com
"""

from torch.utils.data import DataLoader

from .collate_batch import train_collate_fn, val_collate_fn
from .datasets import init_dataset, ImageDataset
from .samplers import RandomIdentitySampler, RandomIdentitySampler_alignedreid  # New add by gu
from .transforms import build_transforms
from data.datasets.my_dataset import NewDataset

def make_data_loader(cfg):
    train_transforms = build_transforms(cfg, is_train=True)
    val_transforms = build_transforms(cfg, is_train=False)
    num_workers = cfg.DATALOADER.NUM_WORKERS
    #list_name = cfg.DATASETS.LIST_PATH
    #root_dir = cfg.DATASETS.ROOT_DIR

    #--- modify dataloader ---#

    # if len(cfg.DATASETS.NAMES) == 1:
    #     dataset = init_dataset(cfg.DATASETS.NAMES, root=cfg.DATASETS.ROOT_DIR)
    #     dataset = my_dataset()
    # else:
    #     # TODO: add multi dataset to train
    #     dataset = init_dataset(cfg.DATASETS.NAMES, root=cfg.DATASETS.ROOT_DIR)

    dataset_train, dataset_num_train_pids = NewDataset(cfg.DATASETS.TRAIN_LIST_PATH, cfg.DATASETS.TRAIN_ROOT_DIR)

    # num_classes = dataset.num_train_pids
    # train_set = ImageDataset(dataset.train, train_transforms)

    num_classes = dataset_num_train_pids
    train_set = ImageDataset(dataset_train, train_transforms)
    if cfg.DATALOADER.SAMPLER == 'softmax':
        train_loader = DataLoader(
            train_set, batch_size=cfg.SOLVER.IMS_PER_BATCH, shuffle=True, num_workers=num_workers,
            collate_fn=train_collate_fn
        )
    else:
        train_loader = DataLoader(
            train_set, batch_size=cfg.SOLVER.IMS_PER_BATCH,
            #sampler=RandomIdentitySampler(dataset.train, cfg.SOLVER.IMS_PER_BATCH, cfg.DATALOADER.NUM_INSTANCE),
            sampler=RandomIdentitySampler(dataset_train, cfg.SOLVER.IMS_PER_BATCH, cfg.DATALOADER.NUM_INSTANCE),
            # sampler=RandomIdentitySampler_alignedreid(dataset.train, cfg.DATALOADER.NUM_INSTANCE),      # new add by gu
            num_workers=num_workers, collate_fn=train_collate_fn
        )

    dataset_query, query_num = NewDataset(cfg.DATASETS.TEST_QUERY_LIST_PATH, cfg.DATASETS.TEST_ROOT_DIR)
    dataset_gallery, num = NewDataset(cfg.DATASETS.TEST_GALLERY_LIST_PATH, cfg.DATASETS.TEST_ROOT_DIR)
    #dataset_gallery, num = NewDataset(cfg.DATASETS.TEST_LIST_PATH, cfg.DATASETS.TEST_ROOT_DIR, 'Test')
    #dataset_gallery, dataset_num_pids = NewDataset(cfg.DATASETS.DATA_PATH, root=cfg.DATASETS.ROOT_DIR)
    val_set = ImageDataset(dataset_query + dataset_gallery, val_transforms)
    val_loader = DataLoader(
        val_set, batch_size=cfg.TEST.IMS_PER_BATCH, shuffle=False, num_workers=num_workers,
        collate_fn=val_collate_fn
    )
    return train_loader, val_loader, len(dataset_query), num_classes
