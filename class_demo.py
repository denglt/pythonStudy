class Student(object):
    # Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
    __slots__ = ('name', 'score')  # 用tuple定义允许绑定的属性名称

    def __init__(self, name, score):
        self.name = name
        self.score = score
        # self.age = 1

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def __len__(self):  # len() 将调用__len__
        return 100


bart = Student('Bart Simpson', 59)
# bart.__name
# bart.__age = 1

print(dir(bart))
# '_Student__name', '_Student__score', '__age', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'print_score']
