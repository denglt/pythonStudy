# 递归神经网路
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet, UnsupervisedDataSet
from pybrain.structure import LinearLayer
ds = SupervisedDataSet(21, 21)
ds.addSample(list(map(int, '1 2 4 6 2 3 4 5 1 3 5 6 7 1 4 7 1 2 3 5 6'.split())), list(map(
    int, '1 2 5 6 2 4 4 5 1 2 5 6 7 1 4 6 1 2 3 3 6'.split())))
ds.addSample(list(map(int, '1 2 5 6 2 4 4 5 1 2 5 6 7 1 4 6 1 2 3 3 6'.split())), list(map(
    int, '1 3 5 7 2 4 6 7 1 3 5 6 7 1 4 6 1 2 2 3 7'.split())))

net = buildNetwork(21, 20, 21, outclass=LinearLayer,
                   bias=True, recurrent=True)  # recurrent 时间递归神经网络
trainer = BackpropTrainer(net, ds)
trainer.trainEpochs(100)
ts = UnsupervisedDataSet(21,)
ts.addSample(
    list(map(int, '1 3 5 7 2 4 6 7 1 3 5 6 7 1 4 6 1 2 2 3 7'.split())))
[int(round(i)) for i in net.activateOnDataset(ts)[0]]
