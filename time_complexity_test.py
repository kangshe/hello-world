def f(x):
    ans = 0
    for i in range(1000):
        ans += 1
    print("for循环1结束：ans=", ans)
    for i in range(x):
        ans += 1
    print("for循环2结束：ans=", ans)
    for i in range(x):
        for j in range(x):
            ans += 1
            ans += 1
    print("for循环3结束：ans=", ans)


f(10000)
