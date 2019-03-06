def merge(left, right, compare):
    """假设left和right是两个有序列表，compare定义了一个列表的元素的排序规则。
       返回一个新的列表（按照compare定义的顺序），其中包含了与（left+right）相同的元素"""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def mergeSort(L, compare=lambda x, y: x < y):
    """假设L是列表，compare定义了L中元素的比较规则，返回一个具有L中相同元素的有序序列"""
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L) // 2
        left = mergeSort(L[:mid], compare)
        right = mergeSort(L[mid:len(L)], compare)
        return merge(left, right, compare)


L = [4, 3, 7, 2, 4, 3, 9, 1, 7]
print(mergeSort(L))
