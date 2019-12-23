# torchreid_competition
https://www.kesci.com/home/competition/5d90401cd8fc4f002da8e7be/content/2

我用的ｐｙｃｈａｒｍ运行，不是命令行

修改对应路径
１．train.py 119行对应训练模型保存位置
２.inference.py 76/77行修改为对应路径，　112行修改为提交代码保存路径
３．defaults.py 预训练模型路径_C.MODEL.PRETRAIN_PATH修改，各种文件路径修改

运行方法
修改完先运行train.py，之后在运行test.py，报错没关系，找到对应提交代码就行
