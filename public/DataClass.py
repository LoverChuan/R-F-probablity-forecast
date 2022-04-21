"""存储数据"""


class Data:
    """存储数据"""
    def __init__(self, a):
        """初始化"""
        self.date = int(a[0])
        self.timePoint = a[1]
        self.startPrice = a[2]
        self.maxPrice = a[3]
        self.minPrice = a[4]
        self.endPrice = a[5]
        self.amount = a[6]
        self.feature = a[7]
        a.pop(7)
        a.pop(1)
        self.dataset = a[:]

    def output(self):
        """打印"""
        print(self.date,self.timePoint,self.startPrice,self.maxPrice,self.minPrice,self.endPrice,self.amount,self.feature)


class SlimData:
    """存储简化数据"""

    def __init__(self, ep, temp=[]):
        self.cal = temp[:]
        self.cal.append(1)
        self.endPrice = ep

    def output(self):
        print(self.cal)

