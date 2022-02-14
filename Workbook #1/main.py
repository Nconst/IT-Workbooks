# Workbook №1
import os
import openpyxl
import random as r
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import trapz


def task_1_3():
    x = 5 >= 2
    A = {1, 3, 7, 8}
    B = {2, 4, 5, 10, 'apple'}
    C = A & B
    df = 'Антонова антонина', 34, 'ж'
    z = 'type'
    D = [1, 'title', 2, 'content']
    print('x: ', x, '|', type(x))
    print('A: ', A, '|', type(A))
    print('B: ', B, '|', type(B))
    print('C: ', C, '|', type(C))
    print('df: ', df, '|', type(df))
    print('z: ', z, '|', type(z))
    print('D: ', D, '|', type(z))


def task_2_3():
    x = int(input('Enter x: '))
    if x < -5:
        print('X принадлежит [-inf.-5]')
    elif x >= -5 & x <= 5:
        print('X принадлежит [-5,5]')
    else:
        print('X принадлежит [5,+inf]')


def task_3_3_1():
    x = 10
    while x >= 1:
        print(x)
        x -= 3


def task_3_3_2():
    human = ['Пол', 'Рост', 'Вес', 'Цвет глаз', 'Цвет волос']
    for sign in human:
        print(sign)


def task_3_3_3():
    list_1 = range(2, 16, 1)
    print(list(list_1))


def task_3_3_4():
    for i in range(105, 4, -25):
        print(i)


def task_3_3_5():
    x = []
    for i in range(r.randint(2, 10)):
        x.append(r.randint(0, 20))
    print(x)
    x[1::2] = reversed(x[1::2])
    print(x)


def task_4_3_2():
    arr = []
    for i in range(10):
        x = r.randint(1, 15)
        base = np.sqrt(1 + np.power(np.e, np.sqrt(x)) + np.cos(np.power(x, 2)))
        subbase = np.fabs(1 - np.power(np.sin(x), 3))
        arr.append(base / subbase)
    print(arr)
    print('Срез первой половины: ', arr[:5])
    print('График для среза: ')
    plt.scatter(arr[:5], arr[:5])
    plt.show()
    print('График для основного массива: ')
    plt.plot(arr)
    plt.show()


def task_4_3_3():
    x = np.arange(0.0, 10, 1)
    y = np.fabs(np.cos(x * np.power(np.e, np.cos(x) + np.log10(x + 1))))

    plt.grid()
    plt.plot(x, y, c="r")
    plt.fill_between(x, y)
    plt.show()

    area = trapz(y)
    print(area)


def task_4_3_4(filename):
    data = pd.ExcelFile(filename)
    sheet_name = data.sheet_names
    ps = openpyxl.load_workbook(filename)

    dots_y = []
    dots_x = [i for i in range(53)]
    for i in range(len(sheet_name)):
        dots_y.append([])
        sheet = ps[sheet_name[i]]
        for row in range(2, sheet.max_row + 1):
            dots_y[i].append(sheet['B' + str(row)].value)

    for i in range(len(sheet_name)):
        plt.plot(dots_x, dots_y[i], label=sheet_name[i])

    plt.legend()
    plt.ylabel('Стоимость акций (USD)')
    plt.xlabel('Номер недели')
    plt.show()


def task_4_3_5():
    run = True
    while run:
        print('1.(x + y)\n2.(x - y)\n3.(x * y)\n4.(x / y)\n5. e^(x + y)\n'
              '6. sin(x + y)\n7. cos(x + y)\n8. x^y\n9.Завершить работу')
        choice = int(input('Выберите опцию >> '))
        if choice != 9:
            x = int(input('Введите переменные x = '))
            y = int(input('y = '))
        if choice == 1:
            print(x+y)
        elif choice == 2:
            print(x-y)
        elif choice == 3:
            print(x*y)
        elif choice == 4:
            print(x/y)
        elif choice == 5:
            print(np.power(np.e,x+y))
        elif choice == 6:
            print(np.sin(x+y))
        elif choice == 7:
            print(np.cos(x+y))
        elif choice == 8:
            print(np.power(x,y))
        elif choice == 9:
            return
        else:
            os.system('CLS')
        input()

if __name__ == '__main__':
    # task_1_3()
    # task_2_3()
    # task_3_3_1()
    # task_3_3_2()
    # task_3_3_3()
    # task_3_3_4()
    # task_3_3_5()
    # task_4_3_2()
    # task_4_3_3()
    # task_4_3_4('DATA.xlsx')
    # task_4_3_5()
