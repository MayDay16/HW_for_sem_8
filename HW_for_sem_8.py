import random
from random import randint

# # Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу. 
# # Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.


def GetRandomArray(M):
    RandomArray = [0]*M
    for i in range(len(RandomArray)):
        colum = random.randint(20, 30)
        RandomArray[i] = list(random.randint(1, 5) for _ in range(colum))
    return RandomArray

def GetBestGroup (group):
    rat = [0]*(len(group))
    for row in range(len(group)): 
        for colum in range(len(group[row])):
            rat[row] += group[row][colum]
        rat[row] = rat[row]/(len(group[row]))
    print(rat)
    print("Лучшая группа : ", (rat.index(max(rat)) + 1))

N = int(input("Ведите количество групп:"))

rating = GetRandomArray(N)
print("Оценки по группам : ")
for row in rating: print(row)

GetBestGroup(rating)

# # Задача 2. Дана квадратная матрица, заполненная случайными числами. 
# # Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

def GetRandomArray(M):
    RandomArray = [0]*M
    for i in range(len(RandomArray)):
        RandomArray[i] = list(random.randint(0, 10) for _ in range(M))
    return RandomArray

def GetMaxLine(matrix):
    SumGeneralDiag = 0
    for i in range(len(matrix)): SumGeneralDiag += matrix[i][i]

    print("Сумма главной диагонали: ",SumGeneralDiag)

    for i in range(len(matrix)):
        if SumGeneralDiag < sum(matrix[i]): print("Строка № :", i)


N = int(input("Ведите размерность квадратной матрицы:"))

Matrix = GetRandomArray(N)

for row in Matrix: print(row , ":", sum(row))

GetMaxLine(Matrix)

# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. 
# Каждому месяцу соответствует своя строка. 
# Определите самый жаркий и самый холодный 7-дневный промежуток этого периода. Выведите его даты.

size = 5
matrix = [0] * size

for i in range(len(matrix)):
    matrix[i] = list(randint(10, 30) for x in range(30))

all_days_temp = []
for row in matrix:
    for i in row:
        all_days_temp.append(i)

periods_temp_sum = []
for i in range(len(all_days_temp) - 7):
    periods_temp_sum.append(sum(all_days_temp[i: i+7]))

index_max_period = periods_temp_sum.index(max(periods_temp_sum))
index_min_period = periods_temp_sum.index(min(periods_temp_sum))


def get_date(index):
    month = index // 30
    print(f'day: {(index + 1) - month * 30}, month: {month + 5}')


print('Самый жаркий период: ')
for i in range(0, 6):
    get_date(index_max_period + i)

print('Самый холодный период: ')
for i in range(0, 6):
    get_date(index_min_period + i)