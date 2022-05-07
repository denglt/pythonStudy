### 跟 tainnData.py 的区别，不进行One-Hot编码

from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import numpy as np
from sklearn.metrics import f1_score



X = np.load("./data/dataset.npy")
y = np.load("./data/class.npy", allow_pickle=True)
y = np.asarray(y,np.int64)
y = y.reshape(y.shape[0], 1)

# 将数据集切割成训练集和测试集。
x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=14)


# 创建  pybrain 的 DataSet

train_data = SupervisedDataSet(x_train.shape[1], y.shape[1])
test_data = SupervisedDataSet(x_test.shape[1], y.shape[1])

for i in range(x_train.shape[0]):
    train_data.addSample(x_train[i], y_train[i])
for i in range(x_test.shape[0]):
    test_data.addSample(x_test[i], y_test[i])


# X.shape[1]代表属性的个数，100代表隐层中神经元的个数，
net = buildNetwork(X.shape[1], 100, 1, bias=True)

# 反向传播(BP)算法
trainer = BackpropTrainer(net, train_data, learningrate=0.01, weightdecay=0.01)


trainer.trainEpochs(epochs=100)  # epochs也就是训练集被训练遍历的次数


from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader

NetworkWriter.writeToFile(net, './data/trainModel2.xml')

# 使用test_data 进行预测
predictions = trainer.testOnClassData(dataset=test_data)


print("F-score: {0:.2f}".format(f1_score(predictions,y_test, average='micro')))    # F-score: 0.88


'''
使用下面数据测试
>>> y[100]
'5'
>>> aNumPic = X[100]
>>> net.activate(aNumPic)
array([7.17412375])
>>> aNumPic = X[0]
>>> net.activate(aNumPic)
array([3.88733284])
>>> y[0]
'5'
'''

