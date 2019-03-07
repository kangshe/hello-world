# coding:utf-8
import matplotlib as plt
import pylab

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

pylab.figure()
principal = 10000  # 初始投资
years = 20
interrestRate = 0.05
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal * interrestRate

print(values[-1])
pylab.plot(values)
pylab.title(u'年复合增长率为5%')
pylab.xlabel(u'总年数')
pylab.ylabel(u'本金价值')
pylab.show()
