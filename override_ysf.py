from pandas.util._decorators import Appender

class Mylist:
    def __init__(self, iterable=()):
        self.__data = list(iterable)
 
    def __repr__(self):
        return 'Mylist(%s)' % self.__data
 
    def __add__(self, lst):       
        '''此方法用来制定self + other的规则'''
        print('__add__被调用')
        return Mylist(self.__data + lst.__data)
 
    def __mul__(self, rhs):
        # rhs为int类型,不能用rhs.data
        print('__mul__被调用')
        return Mylist(self.__data * rhs)

    def __rmul__(self, lhs):
        print("__rmul__被调用")
        return Mylist(self.__data * lhs)

    def __neg__(self):   # - self           负号
        g = (-x for x in self.__data)
        return Mylist(g)
 
    def __pos__(self):   # + self           正号
        g = (abs(x) for x in self.__data)
        return Mylist(g)

    def __contains__(self, e):
        '''
        in / not in 返回布尔值 True / False
            当重载了__contains__后,in和not in运算符都可用
        '''
        return True if e in self.__data else False


    def __getitem__(self, i):
        '索引取值,i绑定[]内的元素'
        print('i的值', i)
        return self.__data[i]  # 返回data绑定列表中的第i个元素
 
    def __setitem__(self, i, v):
        '''此方法可以让自定义的列表支持索引赋值操作'''
        print('__setitem__被调用,i = ', i, 'v = ', v)
        self.__data[i] = v
 
    def __delitem__(self, i):
        if type(i) is int:
            print('用户正在用索引取值')
            del self.__data[i]  # self.__data.pop(i)
        elif type(i) is slice:
            print('用户正在用切片取值')
            print('切片的起点是:', i.start)
            print('切片的终点是:', i.stop) 
            print('切片的步长是:', i.step)
            self.__data[i]
        elif type(i) is str:
            print('用户正在用字符串进行索引操作')
            raise KeyError
        return self

    # 使class具有可迭代性
    def __iter__(self):
        return self

    def __next__(self):
    	# 获取下一个数
        if self.count < len(self.item):
            result = self.item[self.count]
            self.count += 1
            return result
        else:
        # 遍历结束后，抛出异常，终止遍历
            raise StopIteration

    @Appender(
        """
          myfun 3
        """  
        )
    @Appender("myfun 2")
    def myfun(self):
        """
          myfun 1
        """
        return 1    
    
help(Mylist.myfun)
L1 = Mylist([1, 2, 3])
L2 = Mylist([4, 5, 6])
L3 = 3 * L1
print(L3)
L1 += L2
print(L1)
L2 = L2 * 3
print(L2)

L2["dddd"]

'''
 算术运算符的重载:
            方法名                  运算符和表达式      说明
            __add__(self,rhs)        self + rhs        加法
            __sub__(self,rhs)        self - rhs         减法
            __mul__(self,rhs)        self * rhs         乘法
            __truediv__(self,rhs)   self / rhs          除法
            __floordiv__(self,rhs)  self //rhs          地板除
            __mod__(self,rhs)       self % rhs       取模(求余)
            __pow__(self,rhs)       self **rhs         幂运算

 反向运算符的重载
        当运算符的左侧为内建类型时,右侧为自定义类型进行算术匀算符运算时会出现TypeError错误,因为无法修改内建类型的代码          实现运算符重载,此时需要使用反向运算符的重载
        反向算术运算符的重载:
            方法名                  运算符和表达式       说明
            __radd__(self,lhs)       lhs + self       加法
            __rsub__(self,lhs)       lhs - self       减法
            __rmul__(self,lhs)       lhs * self       乘法
            __rtruediv__(self,lhs)   lhs / self       除法
            __rfloordiv__(self,lhs)  lhs // self      地板除
            __rmod__(self,lhs)       lhs % self       取模(求余)
            __rpow__(self,lhs)       lhs ** self      幂运算 

复合赋值算术运算符的重载
        以复合赋值算术运算符 x += y为例,此运算符会优先调用x.__iadd__(y)方法,如果没有__iadd__方法时,则会将复合赋值算术运          算拆解为:x = x + y
        然后调用x = x.__add__(y)方法,如果再不存在__add__方法则会触发TypeError类型的错误异常

        复合赋值算术运算符的重载:
        方法名                  运算符和表达式      说明
        __iadd__(self,rhs)       self += rhs        加法
        __isub__(self,rhs)       self -= rhs         减法
        __imul__(self,rhs)       self *= rhs         乘法
        __itruediv__(self,rhs)   self /= rhs        除法
        __ifloordiv__(self,rhs)  self //=rhs        地板除
        __imod__(self,rhs)       self %= rhs     取模(求余)
        __ipow__(self,rhs)       self **=rhs       幂运算   

比较算术运算符的重载
        比较算术运算符的重载:
        方法名                  运算符和表达式      说明
        __lt__(self,rhs)       self < rhs        小于
        __le__(self,rhs)       self <= rhs       小于等于
        __gt__(self,rhs)       self > rhs        大于
        __ge__(self,rhs)       self >= rhs       大于等于
        __eq__(self,rhs)       self == rhs       等于
        __ne__(self,rhs)       self != rhs       不等于
位运算符重载

            方法名              运算符和表达式        说明
        __and__(self,rhs)       self & rhs           位与
        __or__(self,rhs)        self | rhs              位或
        __xor__(self,rhs)       self ^ rhs             位异或
        __lshift__(self,rhs)    self <<rhs            左移
        __rshift__(self,rhs)    self >>rhs            右移 

 反向位运算符重载

              方法名            运算符和表达式       说明
        __and__(self,lhs)       lhs & rhs             位与
        __or__(self,lhs)         lhs | rhs               位或
        __xor__(self,lhs)       lhs ^ rhs               位异或
        __lshift__(self,lhs)    lhs <<rhs              左移
        __rshift__(self,lhs)    lhs >>rhs              右移   

 复合赋值位相关运算符重载
            方法名              运算符和表达式        说明
        __iand__(self,rhs)       self & rhs          位与
        __ior__(self,rhs)        self | rhs              位或
        __ixor__(self,rhs)       self ^ rhs            位异或
        __ilshift__(self,rhs)    self <<rhs           左移
        __irshift__(self,rhs)    self >>rhs           右移

        

一元运算符的重载

     方法名              运算符和表达式        说明
     __neg__(self)         - self           负号
     __pos__(self)         + self           正号
     __invert__(self)      ~ self           取反     

in/not in 运算符重载
        格式:
            def __contains__(self,e):
                语句
            注: in / not in 返回布尔值 True / False
            当重载了__contains__后,in和not in运算符都可用
            not in 运算符的返回值与 in相反 
索引和切片运算符重载方法:
        方法名                  运算符和表达式              说明
        __getitem__(self,i)     x = self[i]          索引/切片取值
        __setitem__(self,i,v)   self[i] = v          索引/切片赋值
        __delitem__(self,i)     del self[i]          del语句删除索引/切片                                                           
'''


