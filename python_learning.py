import numpy as np
import matplotlib.pyplot as plt

# def add1(x):
#     return x+1

# add1_for_np=np.frompyfunc(add1, 1, 1)

# data=np.ones((3, 3))
# print(data)
# print(add1_for_np(data))

# data2=np.array([1, 2, 3, 4, 5, 6])
# print(data2.reshape(2, 3))

# data3=np.matmul(np.array([[0, 1, 2, 3]]).T, np.array([[1, 1, 1, 1]]))
# print(np.array([[0, 1, 2, 3]]).T)
# print(np.array([[0, 1, 2, 3]]))
# print(data3)
# print(data3.T)
# print(np.where(data3!=np.nan))
# for x, y in zip(range(0, 3), range(0, 3)):
#     print("x={}, y={}".format(x, y))
# print()
# for x, y in zip(np.arange(0, 3), np.arange(0, 3)):
#     print("x={}, y={}".format(x, y))

# print([(x, y) for x in range(-1, 2) for y in range(-1, 2) if (x!=0 or y!=0)])
# print((1, 2)[1])
# a=np.arange(0, 9).reshape((3, 3))
# print(a)
# print(a[1, 2])
# print(a[1][2])
# print(a[[1, 2]])

# print(np.array([(x, y) for x in range(-1, 2) for y in range(-1, 2) if (x!=0 or y!=0)]))
# print()
# # print(np.array([(x, y) for x in range(-1, 2) for y in range(-1, 2) if (x!=0 or y!=0)])[0])
# L=[10, 2, 0.5]
# L.append(55)
# print(L)
# for i in range(0, 3):
#     L[i]=L[i] % 10
# print(L)
# L=np.array(L)
# print(L**2)
# print(np.sum(L))

# print(np.random.choice(np.array(['A', 'B', 'C', 'D']), p=np.array([0.1, 0.5, 0.2, 0.2])))
# print(np.random.choice(5, size=2, replace=False))
# print(len(np.array(['A', 'B', 'C', 'D'])))

figure_list=[]
figure_list.append(plt.figure())
figure_list[0].add_subplot(1, 2, 1)
# a3=figure.add_subplot(2, 2, 3)
figure_list.append(plt.figure())
figure_list[1].add_subplot(1, 2, 1)
# figure_list[1].add_subplot(1, 2, 2)
figure_list[0].add_subplot(1, 2, 2)
print(figure_list)
plt.show()
# plt.show()
# a=np.array(np.random.randint(0, 2, (2, 2)))
# print(a)
# print(np.ma.masked_where(a==1, a))

# print(np.array([x for x in range(0, 5)]))
# print(np.array([[x for x in range(0, 5)]]).T @ np.ones((1, 5)))