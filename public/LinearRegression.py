import numpy as np
from DataClass import Data
from DataClass import SlimData

dataset = []
training_sets = []
validation_sets = []


def f(filename):
    d = []
    with open(filename) as file_object:
        for line in file_object.readlines():
            line = line.replace(" ", "")
            a = []
            last = 1
            temp = Data
            for i in range(1, len(line)):
                if line[i] == ',' or line[i] == ']':
                    a.append(float(line[last:i]))
                    last = i + 1
            temp = Data(a)
            d.append(temp)
    day = d[0].date
    amountsum = d[0].amount
    maxprice = 0.0
    minprice = d[0].minPrice
    sprice = d[0].startPrice
    eprice = d[0].endPrice
    global dataset
    count = 0
    for i in d:
        if int(day) == int(i.date):
            maxprice = max(maxprice, i.maxPrice)
            minprice = min(minprice, i.minPrice)
            eprice = i.endPrice
            amountsum += i.amount
            count += 1
        else:
            a = [day, sprice, (maxprice - minprice) ** 2, maxprice - sprice,
                 amountsum * ((maxprice + minprice) / 2 + sprice) / 2]
            temp = SlimData(eprice, a)
            dataset.append(temp)
            amountsum = i.amount
            maxprice = i.maxPrice
            minprice = i.minPrice
            sprice = i.startPrice
            eprice = i.endPrice
            count = 1
            day = i.date

    global training_sets
    global validation_sets
    training_sets, validation_sets = [], []
    for i in dataset:
        training_sets.append(i.cal)
        validation_sets.append(i.endPrice)
    training_sets=np.array(training_sets)
    validation_sets= np.array(validation_sets)
    prediction_set = [0 for i in range(0, 60, 1)]
    right = 0
    wrong = 0
    pred = []
    for i in range(60, len(training_sets)):
        training_set = []
        validation_set = []
        k = 1
        for j in range(i - 60, i):
            temp = training_sets[j,:]
            temp[0] = k
            training_set.append(temp)
            validation_set.append(validation_sets[j])
            k += 1
        training_set = np.array(training_set)
        validation_set = np.array(validation_set)
        #  omega = [1 for i in range(0, 6, 1)]
        #  omega = np.array(omega)
        omega = np.dot(np.dot(np.linalg.pinv(np.dot(training_set.T, training_set)), training_set.T), validation_set)
        current = np.array(training_sets[i])
        day = current[0]
        current[0] = 61
        ans = np.dot(current, omega)
        prediction_set.append(ans)
        if (ans > validation_sets[i - 1]) == (validation_sets[i] > validation_sets[i - 1]):
            right += 1
        else:
            wrong += 1
        pred.append(str([int(day), int(ans)]) + '\n')
        # print('%-s\t%d\t%s\t%.3f' % ("Date : ", int(day), "Prediction : ", ans))
    print('%-s\t%s%.3f%s' % (filename, ": Precision : ", 100 * right / (right + wrong), '%'))

    
    with open("1_" + filename, "w") as file_object:
        for d in reversed(pred):
            file_object.write(d.replace(' ', ''))