# encoding: utf-8
"""
@author:  sherlock
@contact: sherlockliao01@gmail.com
"""
import logging

import torch
import torch.nn as nn
from ignite.engine import Engine

from utils.reid_metric import R1_mAP, R1_mAP_reranking
import os
import json


def create_supervised_evaluator(model, metrics,
                                device=None):
    """
    Factory function for creating an evaluator for supervised models

    Args:
        model (`torch.nn.Module`): the model to train
        metrics (dict of str - :class:`ignite.metrics.Metric`): a map of metric names to Metrics
        device (str, optional): device type specification (default: None).
            Applies to both model and batches.
    Returns:
        Engine: an evaluator engine with supervised inference function
    """
    if device:
        if torch.cuda.device_count() > 1:
            model = nn.DataParallel(model)
        model.to(device)

    def _inference(engine, batch):
        model.eval()
        with torch.no_grad():
            data, pids, camids = batch
            data = data.to(device) if torch.cuda.device_count() >= 1 else data
            feat = model(data)
            return feat, pids, camids

    engine = Engine(_inference)

    for name, metric in metrics.items():
        metric.attach(engine, name)

    return engine


def inference(
        cfg,
        model,
        val_loader,
        num_query
):
    device = cfg.MODEL.DEVICE

    logger = logging.getLogger("reid_baseline.inference")
    logger.info("Enter inferencing")
    if cfg.TEST.RE_RANKING == 'no':
        print("Create evaluator")
        evaluator = create_supervised_evaluator(model, metrics={'r1_mAP': R1_mAP(num_query, max_rank=50, feat_norm=cfg.TEST.FEAT_NORM)},
                                                device=device)
    elif cfg.TEST.RE_RANKING == 'yes':
        print("Create evaluator for reranking")
        evaluator = create_supervised_evaluator(model, metrics={'r1_mAP': R1_mAP_reranking(num_query, max_rank=50, feat_norm=cfg.TEST.FEAT_NORM)},
                                                device=device)
    else:
        print("Unsupported re_ranking config. Only support for no or yes, but got {}.".format(cfg.TEST.RE_RANKING))

    evaluator.run(val_loader)
    cmc, mAP, max_200_indices, num_q, num_g = evaluator.state.metrics['r1_mAP']

    # save 200 img_id
    query_list_path  = '/home/flyingbird/Documents/reid_competition/test/query_a_list.txt'
    gallery_list_path = '/home/flyingbird/Documents/reid_competition/test/gallery_a_list.txt'

    query_list = list()
    with open(query_list_path, 'r') as f:
                # 测试集中txt文件
        lines = f.readlines()
        for i, line in enumerate(lines):
            data = line.split(" ")
            image_name = data[0].split("/")[1]
            #img_file = os.path.join(r'初赛A榜测试集\query_a', image_name)  # 测试集query文件夹
            query_list.append(image_name)

    # gallery_list = [os.path.join(gallery_list_path, x) for x in # 测试集gallery文件夹
    #                 os.listdir(gallery_list_path)]
    gallery_list = list()
    with open(gallery_list_path, 'r') as f:
                # 测试集中txt文件
        lines = f.readlines()
        for i, line in enumerate(lines):
            data = line.split(" ")
            image_name = data[0].split("/")[1]
            #img_file = os.path.join(r'初赛A榜测试集\query_a', image_name)  # 测试集query文件夹
            gallery_list.append(image_name)
    #query_num = len(query_list)

    res_dict = dict()
    for q_idx in range(num_q):
        #print(query_list[q_idx])
        #print(query_list[q_idx].rindex("\\"))
        filename = query_list[q_idx] #[query_list[q_idx].rindex("\\") + 1:]
        #max_200_files = [gallery_list[i][gallery_list[i].rindex("\\") + 1:] for i in max_200_indices[q_idx]]
        max_200_files = [gallery_list[i] for i in max_200_indices[q_idx]]
        res_dict[filename] = max_200_files
        #print(query_list[q_idx], max_200_files)

    save_path = '/home/flyingbird/Documents/reid_competition/test/rerank_submission_A.json'

    with open(save_path, 'w', encoding='utf-8') as f:  # 提交文件
        json.dump(res_dict, f)


    logger.info('Validation Results')
    logger.info("mAP: {:.1%}".format(mAP))
#   for r in [1, 5, 10]:
#        logger.info("CMC curve, Rank-{:<3}:{:.1%}".format(r, cmc[r - 1]))
