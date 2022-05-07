from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.structure import SoftmaxLayer

from pybrain.datasets import SupervisedDataSet, UnsupervisedDataSet


# two dimensional inputs and one dimensional targets.
ds = SupervisedDataSet(2, 1)

ds.addSample((0, 0), (0,))
ds.addSample((0, 1), (1,))
ds.addSample((1, 0), (1,))
ds.addSample((1, 1), (0,))


net = buildNetwork(2, 3, 1, bias=True, hiddenclass=TanhLayer)
trainer = BackpropTrainer(net, ds)


trainer.trainEpochs(epochs=100)


uds = UnsupervisedDataSet(2,)

uds.addSample((0, 0),)
uds.addSample((0, 1),)

net.activateOnDataset(uds)

'''
>>> net.activateOnDataset(uds)
array([[0.33781925],
       [0.47650578]])
'''

# trainer.testOnClassData(dataset=uds)  # throw error


test_data = SupervisedDataSet(2, 1)

test_data.addSample((0, 0), (0,))
test_data.addSample((0, 1), (1,))

net.activateOnDataset(test_data)

'''
>>> net.activateOnDataset(test_data)
array([[0.33781925],
       [0.47650578]])
'''

trainer.testOnClassData(dataset=test_data)
'''
>>> trainer.testOnClassData(dataset=test_data)
[0, 0]
'''
trainer.testOnData(dataset=test_data)
'''
>>> trainer.testOnData(dataset=test_data)
0.11397990385802648
'''

print('完成')