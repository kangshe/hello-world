class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        return '<物品：' + str(self.name) + ',价值：' + str(self.value) + ',重量：' + str(self.weight) + '>'


def value(item):
    return item.getValue()


def weightInverse(item):
    return 1.0 / item.getWeight()


def density(item):
    return item.getValue() / item.getWeight()


# 0/1背包问题之“贪婪算法”
def greedy(items, maxWeight, keyFunction):
    """假设Items是列表，maxWeight>=0
       keyFunctions将物品元素映射为数值"""
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalWeight = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if totalWeight + itemsCopy[i].getWeight() <= maxWeight:
            result.append(itemsCopy[i])
            totalWeight += itemsCopy[i].getWeight()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)


def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items


def testGreedy(items, maxWeight, keyFunction):
    taken, val = greedy(items, maxWeight, keyFunction)
    print("带走的总物品价值是：", val)
    for item in taken:
        print(' ', item)


def testGreedys(maxWeight=20):
    items = buildItems()
    print('Use greedy by 价值 to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, value)
    print('\nUse greedy by 重量 to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, weightInverse)
    print('\nUse greedy by 性价比 to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, density)


# testGreedys()

def getBinaryRep(n, numDigits):
    """假设n和numDigits为非负整数
       返回一个长度为numDigits的字符串，为n的二进制表示"""
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    if len(result) > numDigits:
        raise ValueError('not enough digits')
    for i in range(numDigits - len(result)):
        result = '0' + result
    return result


def genPowerset(L):
    """假设L是列表
       返回一个列表，包含L中元素所有可能的集合。例如，如果L=[1, 2]，则返回的列表包含元素[]、[1]、[2]和[1,2]"""
    powerset = []
    for i in range(0, 2 ** len(L)):
        binStr = getBinaryRep(i, len(L))
        subset = []
        for j in range(len(L)):
            if binStr[j] == '1':
                subset.append(L[j])
        powerset.append(subset)
    return powerset


# add：0/1背包问题最优解之“暴力解决法（穷举）”
def chooseBest(pset, maxWeight, getV, getW):
    bestSet, bestVal = None, 0.0
    for items in pset:
        itemsVal = 0.0
        itemsWeight = 0.0
        for item in items:
            itemsVal += getV(item)
            itemsWeight += getW(item)
        if itemsWeight <= maxWeight and itemsVal > bestVal:
            bestVal = itemsVal
            bestSet = items
    return (bestSet, bestVal)


def testBest(maxWeight=20):
    items = buildItems()
    pset = genPowerset(items)
    taken, val = chooseBest(pset, maxWeight, Item.getValue, Item.getWeight)
    print('Total value of items taken is', val)
    for item in taken:
        print(item)


testBest()
