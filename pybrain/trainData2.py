### 跟 tainnData.py 的区别，不进行One-Hot编码

from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import numpy as np
from sklearn.metrics import f1_score



print('正在读取训练数据并进行转化......')

X = np.load("./data/dataset.npy")
y = np.load("./data/class.npy", allow_pickle=True)
y = np.asarray(y,np.int64)
y = y.reshape(y.shape[0], 1)

onehotFlag = True
if (onehotFlag):
    print('正在对训练结果数据并进行One-Hot编码......')
    #  进行 One-hot 编码
    # False代表不生成稀疏矩阵
    onehot = OneHotEncoder(sparse=False)  # One-Hot编码，又称为一位有效编码
    y = onehot.fit_transform(y)


print('正在将数据集切割成训练集和测试集......')
x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=14)


# 创建  pybrain 的 DataSet

train_data = SupervisedDataSet(x_train.shape[1], y.shape[1])
test_data = SupervisedDataSet(x_test.shape[1], y.shape[1])

for i in range(x_train.shape[0]):
    train_data.addSample(x_train[i], y_train[i])
for i in range(x_test.shape[0]):
    test_data.addSample(x_test[i], y_test[i])


# X.shape[1]代表属性的个数，100代表隐层中神经元的个数，
net = buildNetwork(X.shape[1], 100, y.shape[1], bias=True)

# 反向传播(BP)算法
trainer = BackpropTrainer(net, train_data, learningrate=0.01, weightdecay=0.01)

print('开始进行深度学习......')
trainer.trainEpochs(epochs=100)  # epochs也就是训练集被训练遍历的次数


from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader

print('开始保存深度学习训练模型......')

if (onehotFlag):
    NetworkWriter.writeToFile(net, './data/trainModel2_onehot.xml')
else:    
    NetworkWriter.writeToFile(net, './data/trainModel2.xml')



print('正在对训练模型进行预测')
if (onehotFlag):
    # 使用test_data 进行预测
    predictions = trainer.testOnClassData(dataset=test_data)
    y_test_arry = y_test.argmax(axis=1)
    print("F-score: {0:.2f}".format(f1_score(predictions,y_test_arry, average='micro'))) # F-score: 0.87
    predictions_2 = net.activateOnDataset(test_data)
    predictions_2 = predictions_2.argmax(axis=1)
    print("F-score: {0:.2f}".format(f1_score(predictions_2,y_test_arry, average='micro')))    # F-score: 0.87

else:
    # 使用test_data 进行预测
    predictions = trainer.testOnClassData(dataset=test_data)
    print("F-score: {0:.2f}".format(f1_score(predictions,y_test, average='micro')))    # F-score: 0.10

    predictions_2 = net.activateOnDataset(test_data)
    predictions_2 = np.round(predictions_2)
    print("F-score: {0:.2f}".format(f1_score(predictions_2,y_test, average='micro')))    # F-score: 0.45

#  One-Hot编码与否的预测结果差这么大，why?

'''
修改narray
for x in np.nditer(predictions_2, op_flags=['readwrite']): 
    x[...]=2*x

'''
'''
>>> y[100]
array([5])
>>> aNumPic = X[100]
>>> net.activate(aNumPic)
array([5.18579342])
>>> aNumPic = X[0]
>>> net.activate(aNumPic)
array([3.59858229])
>>> y[0]
array([5])
>>> test_data.clear()
>>> test_data.addSample(aNumPic,y[0])
>>> trainer.testOnClassData(dataset=test_data)
[0]
>>> trainer.testOnData(dataset=test_data)
0.9819857927781355
>>> net.activateOnDataset(test_data)
array([[3.59858229]])
'''
