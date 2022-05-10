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


train_data = SupervisedDataSet(x_train.shape[1], y.shape[1])
test_data = SupervisedDataSet(x_test.shape[1], y.shape[1])

for i in range(x_train.shape[0]):
    train_data.addSample(x_train[i], y_train[i])
for i in range(x_test.shape[0]):
    test_data.addSample(x_test[i], y_test[i])

from pybrain.tools.customxml.networkreader import NetworkReader    

net = NetworkReader.readFrom('./data/trainModel2.xml')


trainer = BackpropTrainer(net)

# 使用test_data 进行预测
predictions = trainer.testOnClassData(dataset=test_data)


print("F-score: {0:.2f}".format(f1_score(predictions,y_test, average='micro')))   



predictions_2 = net.activateOnDataset(test_data)
predictions_2 = np.round(predictions_2)
print("F-score: {0:.2f}".format(f1_score(predictions_2,y_test, average='micro')))    # F-score: 0.45