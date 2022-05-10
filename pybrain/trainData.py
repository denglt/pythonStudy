from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
import numpy as np
from sklearn.metrics import f1_score



X = np.load("./data/dataset.npy")
y = np.load("./data/class.npy", allow_pickle=True)

y_2 = np.load("./data/class.npy", allow_pickle=True)


# False代表不生成稀疏矩阵
onehot = OneHotEncoder(sparse=False)  # One-Hot编码，又称为一位有效编码
# 首先将y转成行长为7000，列长为1的矩阵，然后再进行转化。
y = onehot.fit_transform(y.reshape(y.shape[0], 1))


# 将数据集切割成训练集和测试集。
x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=14)


# 创建  pybrain 的 DataSet

train_data = SupervisedDataSet(x_train.shape[1], y.shape[1])
test_data = SupervisedDataSet(x_test.shape[1], y.shape[1])

for i in range(x_train.shape[0]):
    train_data.addSample(x_train[i], y_train[i])
for i in range(x_test.shape[0]):
    test_data.addSample(x_test[i], y_test[i])


# X.shape[1]代表属性的个数，100代表隐层中神经元的个数，y.shape[1]代表输出
net = buildNetwork(X.shape[1], 100, y.shape[1], bias=True)

# 反向传播(BP)算法
trainer = BackpropTrainer(net, train_data, learningrate=0.01, weightdecay=0.01)


trainer.trainEpochs(epochs=100)  # epochs也就是训练集被训练遍历的次数


# 使用test_data 进行预测
predictions = trainer.testOnClassData(dataset=test_data)


# 然后使用F1值进行验证

# 取每一行最大值的索引。
y_test_arry = y_test.argmax(axis=1)

print("F-score: {0:.2f}".format(f1_score(predictions,y_test_arry, average='micro')))    # F-score: 0.88

from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader

NetworkWriter.writeToFile(net, './data/trainModel.xml')

'''
使用下面数字进行测试
>>>aNumPic = X[100]
>>> net.activate(aNumPic)
array([ 0.02222398,  0.01921927,  0.20139154, -0.12385399, -0.05486116,
        0.38219321,  0.05215461, -0.01020365,  0.12281588,  0.43281935])   # 预测结果是9
>>> y_2[100]
'5'                       #实际是5

>>>test_data.clear()
>>>test_data.addSample(aNumPic,y[100])
>>>trainer.testOnClassData(dataset=test_data)
>>> trainer.testOnClassData(dataset=test_data)
[9]

### 从文件恢复训练模型
>>> net2 = NetworkReader.readFrom('./data/trainModel.xml')
>>> net2.activate(aNumPic)
array([ 0.02222398,  0.01921927,  0.20139154, -0.12385399, -0.05486116,
        0.38219321,  0.05215461, -0.01020365,  0.12281588,  0.43281935])

>>> trainer2 = BackpropTrainer(net2)
>>> trainer2.testOnClassData(dataset=test_data)
[9]

'''
