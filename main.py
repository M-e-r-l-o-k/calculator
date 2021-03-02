# -*- coding: utf8 -*-
import math

## Режим - для дробей

def drob():
    print('\n1) Сократить дробь\n'
          '2) Сложить дроби\n'
          '3) Вычесть дроби\n'
          '4) Разделить дробь на число\n'
          '5) Привести дроби к общему знаменателю\n'
          '6) Привести дроби к общему числителю\n'
          '7) Найти часть от целого\n'
          '8) Смешанное число в дробь\n'
          '9) Дробь в смешанное число\n'
          '10) Сложить смешанные числа\n'
          '11) Вычитать смешанные числа')
    x = str(input())
    print()
    if x == '0':
        kalculator()
    elif x == '1':
        sokratit_drob()
    elif x == '2':
        slozit_drobi()
    elif x == '3':
        vichitanie_drobey()
    elif x == '4':
        ymnozh()
    elif x == '5':
        obshiy_zn()
    elif x == '6':
        obshiy_ch()
    elif x == '7':
        chast_ot_celogo()
    elif x == '8':
        smesh_chislo_to_drob()
    elif x == '9':
        drob_to_smesh_chislo()
    elif x == '10':
        slozhit_smesh_drobi()
    elif x == '11':
        vichitat_smesh_drobi()
    elif x == '00':
        print('Завершение работы\n'
              '©Kalita Georgy 2021')
        exit()
    else:
        print('Такого варианта не существует')

## Режим - перестановки

def perestanovki():
    print('\nФормулы:\n'
          '1) Перестановки (N!)\n'
          '2) Размещения (A из n по k)\n'
          '3) Сочетания (C из n по k)\n'
          '4) Метод шаров и перегородок')
    inpud = int(input())
    if inpud == 1:
        print('введите N')
        n = int(input())
        print(faktorial(n))
    elif inpud == 2:
        print('введите n и k, где n-кол-во мест и k-кол-во человек. ПОРЯДОК ВАЖЕН')
        n, k = [int(i) for i in input().split()]
        f1 = faktorial(n)
        f2 = faktorial(n-k)
        print(f1 // f2)
    elif inpud == 3:
        print('введите n и k, где n-кол-во мест и k-кол-во человек. ПОРЯДОК НЕ ВАЖЕН')
        n, k = [int(i) for i in input().split()]
        f1 = faktorial(n)
        f2 = faktorial(n - k)
        f12 = f1//f2
        f3 = faktorial(k)
        print(f2*f3)
    elif inpud == 4:
        print('введите n и k, где n-кол-во шаров и k-кол-во групп.')
        n, k = [int(i) for i in input().split()]
        print('введите 0, если 0 дать НЕЛЬЗЯ или 1, если 0 дать МОЖНО')
        ab = int(input())
        if ab == 0:
            n1 = n
            k1 = k
            n = n1 - 1
            k = k1 - 1
            f1 = faktorial(n)
            f2 = faktorial(n - k)
            f1 = f1//f2
            f3 = faktorial(k)
            print(f1 // f3)
        elif ab == 1:
            n = n + k - 1
            k = k - 1
            f1 = faktorial(n)
            f2 = faktorial(n - k)
            f3 = faktorial(k)
            f2f3 = f2 * f3
            print(f1 // f2f3)
    elif inpud == 00:
        print('Завершение работы\n'
              '©Kalita Georgy 2021')
        exit()
    else:
        print('Такого варианта не существует')

## Режим - калькулятор

def kalculator():
    print("\nКaлькулятор:\n"
          "1) +\n"
          "2) -\n"
          "3) *\n"
          "4) :\n"
          "5) ^\n"
          "6) !\n"
          "7) Найти НОД\n"
          "8) Найти НОК\n"
          "9) Найти квадратный корень\n"
          "10) Расположить числа в порядке убывания\n"
          "11) Расположить числа в порядке возрастания\n"
          "12) Разложить число на простые множители")
    a = int(input())
    if a == 00:
        print('Завершение работы\n'
              '©Kalita Georgy 2021')
        exit()
    print("Введите числа через пробел, чтобы выполнить эту операцию")
    s = [int(i) for i in input().split()]
    print('Ответ:', end=' ')
    if a == 1:
        x = 0
        for i in s:
            x = x + i
        print(x)
    elif a == 2:
        print(s[0] - s[1])
    elif a == 3:
        x = 1
        for i in s:
            x = x * i
        print(x)
    elif a == 4:
        print(s[0] / s[1])
    elif a == 5:
        x = s[0]
        for i in range(1, len(s)):
            x = x ** s[i]
        print(x)
    elif a == 6:
        print(faktorial(s[0]))
    elif a == 7:
        NOD_neskolkih(s)
    elif a == 8:
        NOK_neskolkih(s)
    elif a == 9:
        a = s[0]
        print(math.sqrt(a))
    elif a == 10:
        s.sort(reverse=True)
        print(*s)
    elif a == 11:
        s.sort(reverse=False)
        print(*s)
    elif a == 12:
        razlozhit(s)
    else:
        print('Такого варианта не существует')
    print()

# Найти факториал

def faktorial(s):
    n = 1
    for i in range(1, s + 1):
        n = n * i
    return n

# найти НОД (подпрограмма)

def NOD_mini(a, b):
    a1 = a
    b1 = b
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# найти НОК (подпрограмма)

def NOK_mini(a, b):
    s = a * b // math.gcd(a, b)
    return s

# смешанное число в дробь

def smesh_chislo_to_drob():
    print('Введите смешанное число')
    a = str(input()).split()
    s = int(a[0])
    s_ch = int(str(a[1]).split('/')[0])
    s_zn = int(str(a[1]).split('/')[1])
    ans_ch = s * s_zn + s_ch
    ans_zn = s_zn
    print(str(ans_ch)+'/'+str(ans_zn))
    print()

# смешанное число в дробь (подпрограмма)

def smesh_chislo_to_drob_mini(a1):
    a = str(a1).split()
    s = int(a[0])
    s_ch = int(str(a[1]).split('/')[0])
    s_zn = int(str(a[1]).split('/')[1])
    ans_ch = s * s_zn + s_ch
    ans_zn = s_zn
    print(str(ans_ch)+'/'+str(ans_zn))
    print()

# дробь в сменанное число

def drob_to_smesh_chislo():
    print('Введите дробь')
    a = str(input())
    s_ch = int(str(a).split('/')[0])
    s_zn = int(str(a).split('/')[1])
    ans = s_ch//s_zn
    s_ch -= s_ch//s_zn * s_zn
    print(str(ans)+' '+str(s_ch)+'/'+str(s_zn))
    print()

# дробь в сменанное число (подпрограмма)

def drob_to_smesh_chislo_mini(a1):
    a = str(a1)
    s_ch = int(str(a).split('/')[0])
    s_zn = int(str(a).split('/')[1])
    ans = s_ch//s_zn
    s_ch -= s_ch//s_zn * s_zn
    return str(ans)+' '+str(s_ch)+'/'+str(s_zn)

# сложить дроби

def slozit_drobi():
    print('Введите дроби, которые нужно сложить через пробел')
    s = str(input()).split()
    a = 0
    xx = s[0]
    for i in range(1, len(s)):
        xx = slozit_drobi_mini(xx, s[i])
    for i in range(0, len(s)-1):
        print(str(s[i])+' + ',end='')
    print(str(s[len(s)-1]), end='')
    print(' = ')
    print('= ', end='')
    zn = int(xx.split('/')[1])
    for i in range(0, len(s)-1):
        ymnozh = zn // int(s[i].split('/')[1])
        i_zn = int(s[i].split('/')[1])
        i_ch = int(s[i].split('/')[0])
        print(str(i_ch * ymnozh) + '/' + str(i_zn * ymnozh) + ' + ', end='')
    ymnozh = zn // int(s[len(s) - 1].split('/')[1])
    i_zn = int(s[len(s) - 1].split('/')[1])
    i_ch = int(s[len(s) - 1].split('/')[0])
    print(str(i_ch * ymnozh) + '/' + str(i_zn * ymnozh), end='')
    print(' = ')
    print('= ', end='')
    print(xx, '= ')
    print('= ', end='')
    print(drob_to_smesh_chislo_mini(xx))
    print()

# сложить дроби (подпрограмма)

def slozit_drobi_mini(input11, input22):
    input1 = str(input11)
    input2 = str(input22)
    a = int(str(input1).split('/')[0])
    b = int(str(input1).split('/')[1])
    c = int(str(input2).split('/')[0])
    d = int(str(input2).split('/')[1])
    NOK_b_d = int(b * d // math.gcd(b, d))
    drob_1_ch = int(a * (NOK_b_d/b))
    drob_1_zn = int(NOK_b_d)
    drob_2_ch = int(c * (NOK_b_d/d))
    drob_2_zn = int(NOK_b_d)
    ans_ch = drob_1_ch + drob_2_ch
    ans_zn = drob_1_zn
    return str(ans_ch)+'/'+str(ans_zn)

# найти часть от целого

def chast_ot_celogo():
    print('Введите дробь и через пробел число')
    inputt = str(input()).split()
    chislo = int(inputt[1])
    chast_ch = int(str(inputt[0]).split('/')[0])
    chast_zn = int(str(inputt[0]).split('/')[1])
    print(int(chislo/chast_zn*chast_ch))
    print()

# сократить дробь

def sokratit_drob():
    print('Введите дробь')
    a = str(input()).split('/')
    a_ch = int(a[0])
    a_zn = int(a[1])
    k = math.gcd(a_ch, a_zn)
    print(str(a_ch // k)+'/'+str(a_zn // k))
    print()

# сократить дробь (подпрограмма)

def sokratit_drob_mini(a_ch, a_zn):
    k = math.gcd(a_ch, a_zn)
    s = str(a_ch // k)+'/'+str(a_zn // k)
    return s

# найти общий знаминатель

def obshiy_zn():
    print('Введите дроби, для которых надо найти общий знаменатель через пробел')
    s = str(input()).split()
    n = []
    for i in range(0, len(s)):
        n.append(int(s[i].split('/')[1]))
    zn = int(NOK_neskolkih_mini(n))
    for i in range(0, len(s) - 1):
        ymnozh = zn // int(s[i].split('/')[1])
        i_zn = int(s[i].split('/')[1])
        i_ch = int(s[i].split('/')[0])
        print(str(i_ch * ymnozh) + '/' + str(i_zn * ymnozh) + ', ', end='')
    ymnozh = zn // int(s[len(s) - 1].split('/')[1])
    i_zn = int(s[len(s) - 1].split('/')[1])
    i_ch = int(s[len(s) - 1].split('/')[0])
    print(str(i_ch * ymnozh) + '/' + str(i_zn * ymnozh))
    print()

# найти общий знаминатель (подпрограмма)

def obshiy_zn_mini(input11, input22):
    input1 = str(input11)
    input2 = str(input22)
    a = int(str(input1).split('/')[0])
    b = int(str(input1).split('/')[1])
    c = int(str(input2).split('/')[0])
    d = int(str(input2).split('/')[1])
    NOK_b_d = int(b * d // math.gcd(b, d))
    drob_1_ch = int(a * (NOK_b_d / b))
    drob_1_zn = int(NOK_b_d)
    drob_2_ch = int(c * (NOK_b_d / d))
    drob_2_zn = int(NOK_b_d)
    return str(drob_1_ch) + '/' + str(drob_1_zn) + ' ' + str(drob_2_ch) + '/' + str(drob_2_zn)

# найти общий числитель

def obshiy_ch():
    print('Введите дроби, для которых надо найти общий числитель через пробел')
    s = str(input()).split()
    n = []
    for i in range(0, len(s)):
        n.append(int(s[i].split('/')[0]))
    ch = int(NOK_neskolkih_mini(n))
    for i in range(0, len(s) - 1):
        ymnozh = ch // int(s[i].split('/')[0])
        i_zn = int(s[i].split('/')[1])
        i_ch = int(s[i].split('/')[0])
        print(str(i_ch * ymnozh) + '/' + str(i_zn * ymnozh) + ', ', end='')
    ymnozh = ch // int(s[len(s) - 1].split('/')[0])
    i_zn = int(s[len(s) - 1].split('/')[1])
    i_ch = int(s[len(s) - 1].split('/')[0])
    print(str(i_ch * ymnozh) + '/' + str(i_zn * ymnozh))
    print()

# найти общий числитель (подпрограмма)

def obshiy_ch_mini(input11, input22):
    input1 = str(input11)
    input2 = str(input22)
    a = int(str(input1).split('/')[0])
    b = int(str(input1).split('/')[1])
    c = int(str(input2).split('/')[0])
    d = int(str(input2).split('/')[1])
    NOK_a_c = int(a * c // math.gcd(a, c))
    drob_1_zn = int(b * (NOK_a_c / a))
    drob_1_ch = int(NOK_a_c)
    drob_2_zn = int(d * (NOK_a_c / c))
    drob_2_ch = int(NOK_a_c)
    return str(drob_1_ch) + '/' + str(drob_1_zn) + ' ' + str(drob_2_ch) + '/' + str(drob_2_zn)

# сложить смешанные дроби

def slozhit_smesh_drobi():
    print('Введите два смешанного числа, сумму которых надо найти, каждое с новой строчки')
    a1 = str(input()).split()
    s1 = int(a1[0])
    a = int(str(a1[1]).split('/')[0])
    b = int(str(a1[1]).split('/')[1])
    b1 = str(input()).split()
    s2 = int(b1[0])
    c = int(str(b1[1]).split('/')[0])
    d = int(str(b1[1]).split('/')[1])
    ans1 = s1 + s2
    NOK_b_d = int(b * d // math.gcd(b, d))
    drob_1_ch = int(a * (NOK_b_d / b))
    drob_1_zn = int(NOK_b_d)
    drob_2_ch = int(c * (NOK_b_d / d))
    drob_2_zn = int(NOK_b_d)
    ans_drob_ch = drob_1_ch + drob_2_ch
    ans_drob_zn = drob_1_zn
    ans2 = ans_drob_ch // ans_drob_zn
    ans_drob_ch -= (ans_drob_ch // drob_1_zn) * drob_1_zn
    print(str(s1) + ' ' + str(a) + '/' + str(b) + ' + ' + str(s2) + ' ' + str(c) + '/' + str(d) + ' = ' + str(ans1) + ' + ' + str(drob_1_ch) + '/' + str(drob_1_zn) + ' + ' + str(drob_2_ch) + '/' + str(drob_2_zn) + ' = '  + str(ans1) + ' + ' + str(ans2) + ' + ' + str(ans_drob_ch) + '/' + str(ans_drob_zn) + ' = '  + str(ans1 + ans2) + ' ' + str(sokratit_drob_mini(ans_drob_ch, ans_drob_zn)))
    print()

# Найти НОК несколькои чисел

def NOK_neskolkih(a):
    s = a[0]
    for i in range(1, len(a)):
        s = NOK_mini(s, a[i])
    print(s)
    print()

# Найти НОК несколькои чисел (подпрограмма)

def NOK_neskolkih_mini(a):
    s = a[0]
    for i in range(1, len(a)):
        s = NOK_mini(s, a[i])
    return int(s)

# Найти НОД несколькои чисел

def NOD_neskolkih(a):
    s = a[0]
    for i in range(1, len(a)):
        s = NOD_mini(s, a[i])
    print(s)
    print()

# Найти НОД несколькои чисел (подпрограмма)

def NOD_neskolkih_mini(a):
    s = a[0]
    for i in range(1, len(a)):
        s = NOD_mini(s, a[i])
    return int(s)

# вычитание дробей

def vichitanie_drobey():
    print('Введите 2 дроби, кадую с новой строки')
    input1 = str(input()).split('/')
    input2 = str(input()).split('/')
    a = int(input1[0])
    b = int(input1[1])
    c = int(input2[0])
    d = int(input2[1])
    NOK_b_d = int(b * d // math.gcd(b, d))
    drob_1_ch = int(a * (NOK_b_d / b))
    drob_1_zn = int(NOK_b_d)
    drob_2_ch = int(c * (NOK_b_d / d))
    drob_2_zn = int(NOK_b_d)
    ans_ch = drob_1_ch - drob_2_ch
    ans_zn = drob_1_zn
    print(str(a) + '/' + str(b) + ' - ' + str(c) + '/' + str(d) + ' = ' + str(drob_1_ch) + '/' + str(drob_1_zn) + ' - ' + str(drob_2_ch) + '/' + str(drob_2_zn) + ' = ' + str(ans_ch) + '/' + str(ans_zn))
    print()

# вычитание дробей (подпрограмма)

def vichitanie_drobey_mini(input11, input22):
    input1 = str(input11).split('/')
    input2 = str(input22).split('/')
    a = int(input1[0])
    b = int(input1[1])
    c = int(input2[0])
    d = int(input2[1])
    NOK_b_d = int(b * d // math.gcd(b, d))
    drob_1_ch = int(a * (NOK_b_d / b))
    drob_1_zn = int(NOK_b_d)
    drob_2_ch = int(c * (NOK_b_d / d))
    drob_2_zn = int(NOK_b_d)
    ans_ch = drob_1_ch - drob_2_ch
    ans_zn = drob_1_zn
    return str(ans_ch) + '/' + str(ans_zn)

# вычитать смешанные дроби

def vichitat_smesh_drobi():
    print('Введите два смешанных числа, разность которых надо найти, каждое с новой строки')
    a1 = str(input()).split()
    s1 = int(a1[0])
    a = int(str(a1[1]).split('/')[0])
    b = int(str(a1[1]).split('/')[1])
    a_save = int(a)
    b_save = int(b)
    b1 = str(input()).split()
    s2 = int(b1[0])
    c = int(str(b1[1]).split('/')[0])
    d = int(str(b1[1]).split('/')[1])
    if a == 0:
        s1 -= 1
        b = int(d)
        a = int(b)
    else:
        s1 -= 1
        a += b
    drob1 = str(a) + '/' + str(b)
    drob2 = str(c) + '/' + str(d)
    ob_zn = obshiy_zn_mini(drob1, drob2).split()
    ans = vichitanie_drobey_mini(drob1, drob2)
    ans_smesh = drob_to_smesh_chislo_mini(ans)
    ans_chislo = ans_smesh.split()[0]
    ans_drob = ans_smesh.split()[1]
    print(str(s1+1) + ' ' + str(a_save) + '/' + str(b_save) + ' - ' + str(s2) + ' ' + str(c) + '/' + str(d) + ' = ' + '\n'
          + '= ' + str(s1) + ' ' + str(ob_zn[0]) + ' - ' + str(s2) + ' ' + str(ob_zn[1]) + ' = ' + '\n'
          + '= ' + str(s1 - s2) + ' + ' + str(ans) + ' = ' + '\n'
          + '= ' + str(s1 - s2 + int(ans_chislo)) + ' + ' + str(ans_drob) + ' = ' + '\n'
          + '= ' + str(int(ans_chislo) + s1 - s2) + ' ' + str(ans_drob))
    print()

# умоножение смеш числа на n

def ymnozh():
    print('Введите смеш. число и с новой строчки делитель')
    mn2 = str(input()).split()
    mn1 = int(input())
    mn2_celoe = int(mn2[0])
    mn2_ch = int(mn2[1].split('/')[0])
    mn2_zn = int(mn2[1].split('/')[1])
    mn2_ch += mn2_celoe * mn2_zn
    mn2_zn = mn2_zn * mn1
    ans_dr = str(mn2_ch)+'/'+str(mn2_zn)
    ans = drob_to_smesh_chislo_mini(ans_dr)
    ans_drob = ans.split()[1]
    ans_celoe = ans.split()[0]
    ans_dr_ch = int(str(ans_drob).split('/')[0])
    ans_dr_zn = int(str(ans_drob).split('/')[1])
    ans_drob = sokratit_drob_mini(ans_dr_ch, ans_dr_zn)
    ans_ans = str(ans_celoe)+' '+str(ans_drob)
    print(ans_ans)

# Разложить число на простые множители

def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans

def razlozhit(a):
    a = int(a[0])
    s = Factor(a)
    n = list(set(s))
    ans = [str(a) + ' =']
    for i in range(len(n)-1):
        x = str(n[i]) + '^' + str(s.count(n[i])) + ' *'
        ans.append(x)
    i = len(n)-1
    x = str(n[i]) + '^' + str(s.count(n[i]))
    ans.append(x)
    print(*ans)

print('© Kalita Georgy 2021')

while True:
    print('\nВыберете режим:\n'
          '1) Режим калькулятора\n'
          '2) Режим для дробей\n'
          '3) Режим для подсчета кол-ва перестановок')
    a = input()
    if len(a) == 1:
        a = int(a)
    if a == 1:
        kalculator()
    elif a == 2:
        drob()
    elif a == 3:
        perestanovki()
    elif a == '00':
        print('Завершение работы\n'
              '©Kalita Georgy 2021')
        exit()
    else:
        print('Такого варианта не существует')

## Режим только для дробей
# while True:
#     drob()

## Режим только для калькулятора
# while True:
#     kalculator()

## Режим только для перестановок
# while True:
#     perestanovki()
