def fib(n):
    """假设n是正整数
       返回第n个斐波那契数列的值"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fastFib(n, memo={}):
    """假设n是正整数,memo只进行递推调用
       返回第n个斐波那契数列的值"""
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n - 1, memo) + fastFib(n - 2, memo)
        memo[n] = result
        return result

#print(fib(120))
print(fastFib(120))
