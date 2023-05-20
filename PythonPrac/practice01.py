# a, *b = [1,2,3]
# a, *b = 'hello'
# print(a, b, type(b))

import numpy as np

import matplotlib.pyplot as plt
from numpy import random
# numpy == мат лаб
# numpy ndarray => ndarray.ndim, shape, size, dtype, itemsize
A = np.array([0,1,2,3,4,5,6,7,8,9])
# print(A, type(A))

B = np.array([[1,2], [3,4]])
# print(B, type(B))

# print(A.shape)
# print(B.shape)

# np.arange == range
# print(np.arange(5, 15, 0.9))
# 0.9 - шаг
# правая граница не включ

# print(np.linspace(3, 15, 10))
# 10 - кол-во точек

# r = np.random.rand(5,5)
# print(r) 


# def myFunc(i,j):
#     return (i+1)*(j+4-i)  #просто какое-то выражение

# a = np.fromfunction(myFunc, (3,6))
# #print(a, type(a))

# A = np.arange(0,15,1)
# print(A)
# print(A[3:8:2]) #начало:конец:шаг


# A = np.array([[n+m*10 for n in range(5)] for m in range (5)])
# # print(A)
# # print(A*A) # поэлементно
# # print(np.dot(A,A))

# M = np.matrix(A)
# print(type(M))
# print(M*M) # матричное умножение



# lambda arguments: expression

# f = lambda x,y: x*y
# print(f(7,2))

# L = [1,2,3,4]
# a = list(map(lambda x:x**2,L)) #map => к каждому аргументу примернить
# print(a)

# print(list(filter(lambda x: x%2 == 0, [1,3,2,5, 20, 21]))) #список четных чисел из массива


# fig = plt.figure()
# ax = fig.add_subplot(1,1,1) # оси

# fig.set(facecolor = 'green')
# ax.set(facecolor = 'red')

# ax.set_xlim([-10,10])
# ax.set_ylim([-2,2])

# ax.set_xlabel('Абцисс (Х)')
# ax.set_ylabel('Ординат (У)')

# plt.show()


# fig, ax = plt.subplots()
# x = [-3,-2,-1,0,1,2,3]
# y = [9,4,1,0,1,4,9]
# ax.plot(x,y) # оси для графика
# plt.show()


# fig, (ax1, ax2) = plt.subplots(
#     nrows = 1, ncols = 2, figsize = (8,4) # делим окно
# ) 



# gridsize = (3,2) # сетка
# fig = plt.figure(figsize = (12,8))
# ax1 = plt.subplot2grid(gridsize, (0,0), colspan = 2, rowspan = 2)
# ax2 = plt.subplot2grid(gridsize, (2,0))
# ax3 = plt.subplot2grid(gridsize, (2,1))

# plt.show()



# 3D гРаФиКа
from mpl_toolkits.mplot3d import axes3d
# fig = plt.figure()
# ax = fig.add_subplot(111, projection = '3d')
fig, ax = plt.subplots(subplot_kw = {"projection" : "3d"})

x = np.arange(-1, 1, 0.01)
y = np.arange(-1, 1, 0.01)
X, Y = np.meshgrid(x,y)
Z = X**2 - Y**2

s = ax.plot_wireframe(X, Y, Z, rstride = 20, cstride = 15)
s = ax.plot_surface(X, Y, Z, rstride = 20, cstride = 15)
plt.show()
