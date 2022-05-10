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


test_data = SupervisedDataSet(x_test.shape[1], y_test.shape[1])

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


onehot = OneHotEncoder(sparse=False)  # One-Hot编码，又称为一位有效编码
y_test_onehot = onehot.fit_transform(y_test)

test_data_onehot = SupervisedDataSet(x_test.shape[1], y_test_onehot.shape[1])

for i in range(x_test.shape[0]):
    test_data_onehot.addSample(x_test[i], y_test_onehot[i])

net_onehot = NetworkReader.readFrom('./data/trainModel2_onehot.xml')
trainer_onehot = BackpropTrainer(net_onehot)
predictions = trainer_onehot.testOnClassData(dataset=test_data_onehot)
y_test_arry = y_test_onehot.argmax(axis=1)
print("F-score: {0:.2f}".format(f1_score(predictions,y_test_arry, average='micro'))) # F-score: 0.87
predictions_2 = net_onehot.activateOnDataset(test_data_onehot)
predictions_2 = predictions_2.argmax(axis=1)
print("F-score: {0:.2f}".format(f1_score(predictions_2,y_test_arry, average='micro')))    # F-score: 0.87