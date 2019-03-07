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


testGreedys()
