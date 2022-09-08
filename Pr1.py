import math

def f1():
    
    print('Введите данные для треугольника (только целые числа!):\n')
    a = int(input('Сторона a: \n'))
    b = int(input('Сторона b: \n'))
    c = int(input('Сторона c: \n'))
    p = (a + b + c) / 2
    res_of_triangle = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('Площадь треугольника по формуле Герона: ', res_of_triangle , '\n')
    print('Введите данные для радиуса круга (только целые числа!): \n')
    r = int(input('Радиус r: \n'))
    res_of_circle = math.pi * r ** 2
    print('Площадь круга по формуле: ', res_of_circle , '\n')
    print('Введите данные для прямоугольника (только целые числа!): \n')
    g = int(input('Сторона g: \n'))
    q = int(input('Сторону q: \n'))
    res_of_rectangl = g * q
    print('Площадь прямоугольника по формуле: ', res_of_rectangl , '\n')
    dict = {'Треугольник': res_of_triangle,
            'Круг': res_of_circle, 'Прямоугольник': res_of_rectangl}
    print(dict, type(dict))
f1()

print ('\n')


def f2():
        
        play = ['+', '-', '*', '/', '**', '//']
        while play != None:
                print('Введите два числа или введите СТОП, чтобы закончить: \n')
                a = input()
                b = input()
                if a == 'СТОП' or b == 'СТОП':
                    break
                else:
                    a = float(a)
                    b = float(b)
                    print('Выбирите действие или введите СТОП, чтобы закончить: ', play, '\n')
                    x = input()
                    print('\n')
                    print('Ваши числа: ', a, ',', b, '\n')
                    if x == '+':
                        play.remove(x)
                        print('Результат операции сложения:', a + b, '\n')
                    elif x == '-':
                        play.remove(x)
                        print('Результат операции вычитания: ', a - b, '\n')
                    elif x == '*':
                        play.remove(x) 
                        print('Результат операции умножения: ', a * b, '\n')
                    elif x == '/':
                        play.remove(x)
                        print('Результат операции деления: ', a / b, '\n')
                    elif x == '**':
                        play.remove(x)
                        print('Результат операции возведения в степень: ', a ** b, '\n')
                    elif x == '//':
                        play.remove(x)
                        print('Результат операции целочисленного деления: ', a // b, '\n')
                    elif x == 'СТОП':
                        print('Конец программы')
                        break           
f2()

print ('\n')


def f3():

    print('Данный пункт рассчитывает площадь треугольника по формуле Герона. Реализация использует вешественные числа. \n\n')
    e = 2.718281828459045
    w = -2.34
    i = 5.0
    print('Наши числа: ', e, w, i, '\n')
    per = (e + w + i) / 2
    geron = math.sqrt(per * (per - e) * (per - w) * (per - i))
    print('Площаль равна: ', geron, '\n')


f3()
