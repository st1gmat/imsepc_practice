import numpy as np # + matplotlib, plotlyw
# import pandas
import pandas as pd

# print(pandas.__version__)
# dd = pd.Series([1,2,2,2,2,2,2], ['a','b','c','d','e','f','g']) # abc - метки, 1222 значения

# print(dd)

# my_list = [1,2,3] 
# arr = np.array([10,20,30])
# s4 = pd.Series(data=my_list, index=my_list)
# print(s4)


# d = {'a':1, 'b':2, 'c':3} можно юзать словарь
# s4 = pd.Series(d)
# print(d)


# ser1 = pd.Series([2,3,1,4],index=["USA","GERMANY","RUSSIA","JAPAN"])
# print(ser1)

# USA        2  ---> ser1[0] или использовать метку USA --> print(ser1[0]) или print("USA")
# GERMANY    3
# RUSSIA     1
# JAPAN      4
# dtype: int64

# print(ser1 > 2) # можно условыне
# print(ser1.iloc[2]) # iloc - индекс позиция поиск
# print(ser1.loc("USA")) # loc - поиск по метке

# можно производить арифм хрень с таблицами

# print(ser1.values) # на выход получаем список значений из таблицы

#DATA FRAME - полноценная таблица

# df = pandas.DataFrame(
#     data=[[5,True,"x", 2.7]
#           ,[5,True,"y", 3.7]
#           ,[5,True,"z", 4.7]],
#     index=["A","B","C"],
#     columns=['num','bool','str','real']
# )
# print(df)

# Чтение и запись

# df = pd.read_csv(r'C:\\Users\\MSI\Desktop\\PythonMath\\demodata.csv') # импорт

# df.to_csv(filename) # экспорт

# print(df.head()) # первые несколько записей

# df.info() # показываетс так же где пропуски

# print(df.describe()) # дает основную инфу по графику, мин, мах, стандартное отклонение и тд

# df["date"] - поиск столбца 

# print(df.iloc[1:3])# от 1 до 3 походу по индексам

# print(df.loc[1:3]) #тут вроде норм выводится

# print(df[df["gains"] < 0]) # условия
# print(df[(df.weekdays=="Wed") & df.up]) # Только среды
# print(df.query('weekdays == "Wed" and up'))
# res = df.query('weekdays == "Sun" or prices < prices.mean() and gains < 0')

# print(df.sample()) # случайная выборка, без значений по дефолту одна случайная запись
# print(df.sample(n=3))

#df.is_in - че то такое проверяет входит ли или нет

df = pd.read_csv(r'titanic.csv') # импорт

# print("Info of df:\n", df.info(), "\n\n\nMain desccribes of df:\n", df.describe())

# print(df.head())

# df.dillna(0) # заполняет пробелы
# df.dropna() # удаляет пробелы


# print(df[["Age", "Sex"]].head())

# df["Relatives"] = df["SibSp"] + df["Parch"]

# print(df[["SibSp","Parch","Relatives"]].head())
print(len(df[(df['Sex'] =='female') & (df['Survived']== 1)]))
print(len(df[(df['Sex'] =='male') & (df['Survived'] == 1)]))
