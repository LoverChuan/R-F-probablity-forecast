import numpy as np
import math
from DataClass import Data
from DataClass import SlimData

"""逻辑回归预测"""

training_sets, validation_sets = [], []
training_set, validation_set = [], []
x_cur = []

omega, omega_new = [], []


def mle_function():
    """极大似然后的单峰函数"""
    global training_set, validation_set, omega
    f, t = 0.0, 0.0
    for index in range(0, 60, 1):
        x = np.array(training_set[index])
        t = np.dot(omega, x.T)
        f += -1.0 * validation_set[index] * t + math.log(1 + math.exp(t))
    return f


def partial_derivative(j):
    global training_set, validation_set, omega, x_cur
    f, t = 0.0, 0.0
    for index in range(0, 60):
        x = np.array(training_set[index])
        t = np.dot(omega, x_cur.T)
        f += -1.0 * validation_set[index] * x_cur[j] + x_cur[j] * math.exp(t) / (1 + math.exp(t))
    return f


def future_scaling():
    global training_set, x_cur
    maxn = training_set[:, 0:-1].max(axis=0)
    minn = training_set[:, 0:-1].min(axis=0)
    meann = training_set[:, 0:-1].mean(axis=0)
    gap = maxn - minn
    for i in range(0, 60):
        training_set[i, 0:-1] = (training_set[i, 0:-1] - meann) / gap
    x_cur[0] = 61
    x_cur[0:-1] = (x_cur[0:-1] - meann) / gap
    # x_cur的特征缩放并不知道是否正确


def gradient_decent(alpha):
    """梯度下降法"""
    global training_set, validation_set, x_cur
    global omega, omega_new
    delta, down, ss = 1.0, 0, 0.0
    omega = [1 for i in range(0, len(x_cur), 1)]
    omega = np.array(omega)
    omega_new = omega

    former = mle_function()

    while abs(delta) > 0.0001:
        # 求偏导
        for i in range(0, len(x_cur), 1):
            omega_new[i] = partial_derivative(i)
        omega_new = np.array(omega_new)
        omega = omega - alpha * omega_new
        print(omega)
        print(omega_new)
        current = mle_function()
        delta = current - former
        if abs(delta) < abs(former - current):
            down += 1
        else:
            down = 0
        if down >= 10:
            break
        print(former, current)
        former = current
    if down < 8:
        ss = 1 - (1 / (1 + math.exp(np.dot(omega, x_cur.T))))
    else:
        ss = gradient_decent(alpha / 3)
    return ss


def logistic_regression(filename):
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
            temp = SlimData(eprice, a)
            dataset.append(temp)
            amountsum = 0.0
            maxprice = i.maxPrice
            minprice = i.minPrice
            sprice = i.startPrice
            eprice = i.endPrice
            count = 1
            former = i

    global training_sets
    global validation_sets
    training_sets = [dataset[0].cal]
    validation_sets = [1]
    last_price = dataset[0].endPrice
    for i in dataset[1:]:
        training_sets.append(i.cal)
        if i.endPrice > last_price:
            validation_sets.append(1)
        else:
            validation_sets.append(0)
        last_price = i.endPrice

    prediction_set = [0.0 for i in range(0, 60, 1)]
    right = 0
    wrong = 0

    for i in range(60, len(training_sets) - 3):
        global training_set
        global validation_set
        global x_cur
        training_set, validation_set = [], []
        k = 1
        for j in range(i - 60, i):
            temp = training_sets[j]
            temp[0] = k
            training_set.append(temp)
            validation_set.append(validation_sets[j])
            k += 1
        training_set = np.array(training_set)
        validation_set = np.array(validation_set)
        x_cur = np.array(training_sets[i])
        # =======================================
        future_scaling()
        # print(training_set)
        ss = gradient_decent(1.0)
        prediction_set.append(ss)
        print(ss)
        if (ss >= 0.5 and validation_sets[i] == 1) or (ss < 0.5 and validation_sets[i] == 0):
            right += 1
        else:
            wrong += 1
        break
# print('%.3f' % (right / (right + wrong)))
