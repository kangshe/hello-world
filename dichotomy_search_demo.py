def search(L, e):
    """假设L是列表，其中元素按升序排列。
       如果e是L中的元素，则返回True，否则返回False"""

    def dSearch(L, e, low, high):
        if high == low:
            print(L[high] == e)
            return L[high] == e
        mid = (high + low) // 2
        if L[mid] == e:
            print("True")
            return True
        elif L[mid] > e:
            if low == mid:
                print("False")
                return False
            else:
                return dSearch(L, e, low, mid - 1)
        else:
            return dSearch(L, e, mid + 1, high)

    if len(L) == 0:
        print("False")
        return False
    else:
        return dSearch(L, e, 0, len(L) - 1)


search([1, 2, 3, 4, 5, 8, 9, 10], 5)
