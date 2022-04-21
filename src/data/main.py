import math
import numpy as np
import os

filenames = ["ag_15m.txt", "al_15m.txt", "au_15m.txt", "bu_15m.txt",
             "cf_15m.txt", "cu_15m.txt", "dci_15m.txt", "dcp_15m.txt",
             "fg_15m.txt", "jm_15m.txt", "j_15m.txt", "ma_15m.txt",
             "ni_15m.txt", "pb_15m.txt", "rb_15m.txt", "sn_15m.txt",
             "sr_15m.txt", "zn_15m.txt"]

class Data:
    """存储数据"""
    def __init__(self, a):
        """初始化"""
        self.date = int(a[0])
        self.timePoint = [1]
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
        print(self.dataset)


class SlimData:
    """存储简化数据"""

    def __init__(self, ep, temp=[]):
        self.cal = temp[:]
        self.cal.append(1)
        self.endPrice = ep

    def output(self):
        print(self.cal)

def sigmoid(x):
    if (x > 10000):
        return 1
    if (x < -10000):
        return 0
    return 1.0 / (1.0 + math.exp(-x))

def uniforma(x):
    return sigmoid(x) - 0.5

def f(filename):
    d = []
    with open(filename) as file_object:
        for line in file_object:
            a = []
            last = 1
            temp = Data
            for i in range(1, len(line)):
                if line[i] == ',' or line[i] == ']':
                    a.append(float(line[last:i]))
                    last = i + 1
            d.append(temp(a))

    filename = '0_' + filename
    datastring = ''
    former = d[0]
    amountsum = 0.0
    maxprice = 0.0
    minprice = former.minPrice
    sprice = 0.0
    eprice = 0.0
    dataset = []
    count = 0
    for i in d:
        if former.date == i.date:
            maxprice = max(maxprice, i.maxPrice)
            minprice = min(minprice, i.minPrice)
            sprice += i.startPrice
            eprice = i.endPrice
            amountsum += i.amount
            count += 1
        else:
            a = [former.date, sprice / count, maxprice, minprice, amountsum]
            b = [former.date, former.startPrice, i.endPrice, maxprice, minprice, amountsum]

            st = ''.join(str(int(v)) + ',' for v in b)
            st = '[' + st[0:-1] + ']' + '\n'
            datastring = st + datastring
            
            temp = SlimData(eprice, a)
            dataset.append(temp)
            amountsum = 0.0
            maxprice = i.maxPrice
            minprice = i.minPrice
            sprice = i.startPrice
            eprice = i.endPrice
            count = 1
            former = i

    with open(filename, 'w') as file_object:
        file_object.write(datastring)

    training_sets = []
    validation_sets = []
    dataset.pop()
    for i in dataset:
        training_sets.append(i.cal)
        validation_sets.append(i.endPrice)

    prediction_set = [0 for i in range(0, 60, 1)]
    right = 0
    wrong = 0
    for i in range(60, len(training_sets) - 3):
        training_set = []
        validation_set = []
        k = 1
        for j in range(i - 60, i):
            temp = training_sets[j]
            temp[0] = k
            training_set.append(temp)
            validation_set.append(validation_sets[j])
            k += 1
        training_set = np.array(training_set)
        validation_set = np.array(validation_set)
        #  omega = [1 for i in range(0, 6, 1)]
        #  omega = np.array(omega)
        omega = np.dot(np.dot(np.linalg.inv(np.dot(training_set.T, training_set)), training_set.T), validation_set)
        current = np.array(training_sets[i])
        ans = np.dot(current, omega)
        prediction_set.append(ans)
        if (ans > validation_sets[i - 1]) == (validation_sets[i] > validation_sets[i - 1]):
            right += 1
        else:
            wrong += 1
    print('%-s\t%s%.3f%s' % (filename, ": Precision : ", 100 * right / (right + wrong), '%'))

if __name__ == '__main__':
    for filename in filenames:
        f(filename)