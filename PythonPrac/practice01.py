# a, *b = [1,2,3]
# a, *b = 'hello'
# print(a, b, type(b))
# недостаток в том, что если пользоваться кортеж., списками, нужна циклы, а это не очень ибо например 
# range только на целый шаг и тд и тп, циклы работают медленно

import numpy as np

import matplotlib.pyplot as plt
from numpy import random
# numpy аналог мат лаба, модульная система. 
# numpy ndarray - основные атрибуты ndarray.ndim, shape, size, dtype, itemsize
A = np.array([0,1,2,3,4,5,6,7,8,9])
# print(A, type(A))

B = np.array([[1,2], [3,4]])
# print(B, type(B))

# print(A.shape)
# print(B.shape)
# кортеж занимает меньше места, и возрвращается все в виде кортежа, чтобы сэкономить места в памяти

# np.arange (аналог range) генерирует массив numpy со значениями в укаазнном диапазоне
# print(np.arange(5, 15, 0.9))
# прелесть в последней переменной (это тип шаг) МОЖЕТ БЫТЬ НЕ ЦЕЛЫМ
# ПРАВАЯ ГРАНИЦА НЕ ВКЛЮЧАЕТСЯ, 15 НЕ БУДЕТ!! 14.9 последним будет

# print(np.linspace(3, 15, 10))
# последнее это кол-во точек, а не шаг

# r = np.random.rand(5,5)
# print(r) 


# def myFunc(i,j):
#     return (i+1)*(j+4-i)  #просто какое-то выражение

# a = np.fromfunction(myFunc, (3,6))
# #print(a, type(a)) #будет сразу массив numpy

# # начинаем с 0, правая граница не учитывается

# A = np.arange(0,15,1)
# print(A)
# print(A[3:8:2]) #start:stop:step


# A = np.array([[n+m*10 for n in range(5)] for m in range (5)])
# # print(A)
# # print(A*A) #умножает поэлементно!!
# # print(np.dot(A,A)) #как надо 

# M = np.matrix(A)
# print(type(M))
# print(M*M) # матричное умножение, т.к М это класс матрица!!



# lambda arguments: expression (в одну строку))(синтаксис)

# f = lambda x: x*x
# print(f(5))

# f = lambda x,y: x*y
# print(f(7,2))

# L = [1,2,3,4]
# a = list(map(lambda x:x**2,L)) #map дает возможность применять переданную функцию к каждому элементу
# print(a)

# print(list(filter(lambda x: x%2 == 0, [1,3,2,5, 20, 21]))) #выдаст список четных чисел из переданного массива


# fig = plt.figure() # создали область figure
# ax = fig.add_subplot(1,1,1) # добавляем оси (строка, столбец, к кому обращаюсь) можно fig.add_axes (если один график)

# fig.set(facecolor = 'green')
# ax.set(facecolor = 'red') #оси красные

# ax.set_xlim([-10,10])
# ax.set_ylim([-2,2])

# ax.set_xlabel('ось абцисс (Х)')
# ax.set_ylabel('ось ординат (У)')

# plt.show()


# fig, ax = plt.subplots()
# x = [-3,-2,-1,0,1,2,3]
# y = [9,4,1,0,1,4,9]
# ax.plot(x,y) # На этих осях хочу график
# plt.show()


# fig, (ax1, ax2) = plt.subplots(
#     nrows = 1, ncols = 2, figsize = (8,4) #1 строчка, 2 столбца (просто тип делю окно как в октаве сабплот)
# ) 
# и дальше могу на оси ax1 например нарисовать синус, а на ax2 косинус и все кайф либо на ax1 плот, а на ax2 гистограмму


# gridsize = (3,2) # сетка 3 на 2
# fig = plt.figure(figsize = (12,8))
# ax1 = plt.subplot2grid(gridsize, (0,0), colspan = 2, rowspan = 2) # объединяю 4 ячейки
# ax2 = plt.subplot2grid(gridsize, (2,0))
# ax3 = plt.subplot2grid(gridsize, (2,1))

# plt.show()



# 3хмерная графика
from mpl_toolkits.mplot3d import axes3d
# fig = plt.figure()
# ax = fig.add_subplot(111, projection = '3d')
fig, ax = plt.subplots(subplot_kw = {"projection" : "3d"})

x = np.arange(-1, 1, 0.01)
y = np.arange(-1, 1, 0.01)
X, Y = np.meshgrid(x,y)
Z = X**2 - Y**2

s = ax.plot_wireframe(X, Y, Z, rstride = 20, cstride = 15) # rstride это тип шаг по строкам (насколько часто рисуем)
# wireframe не залито
s = ax.plot_surface(X, Y, Z, rstride = 20, cstride = 15)
plt.show()
