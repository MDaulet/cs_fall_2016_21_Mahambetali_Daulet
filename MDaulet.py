from functools import reduce
import math
import matplotlib.pyplot as plt
import numpy as np

while True:

    print("Welcome")
    print("1 a)Enter '1.a' or 'Sum 1' to calculate the amount of with for-loop")
    print("  b)Enter '1.b' or 'Sum 2' to calculate the amount of with while-loop")
    print("  c)Enter '1.c' or 'Sum 3' to calculate the amount of with recursion")
    print("2) Enter  '2' or 'Degree' to calculate the power of two, that is no longer your number ")
    print("3) Enter  '3' or 'Arithmetic mean' to calculate the arithmetic mean")
    print("4)Enter '4' or 'Fibonacci number' for the calculation of the number of rooms in the Fibonacci sequence")
    print("5)Enter '5' or 'Factorial' to calculate the factorial")
    print("6)Enter '6' or 'Substitution' to replace the maximum and minimum")
    print("7)Enter the '7' or 'Distance' to find the distance between points ")
    print("8)Enter '8' or 'Schedule' to plot the trajectory of a projectile discharged from the gun on Mars. ")
    print("Enter '0' or 'Exit' to exit the program ")

    user_input = input(":")

    if user_input == "0" or user_input == "Exit":
        break
    elif user_input == "5" or user_input == "Factorial":
        n = int(input("Enter the N number for the factorial:"))
        res = 1
        for z in range(1, n + 1):
            res *= z
        print(res)
    elif user_input == "1.a" or user_input == "Sum 1":
        sum1 = input("Enter the number:")
        sum1 = sum1.split()
        b1 = []
        h = 0
        for i in sum1:
            b1.append(float(i))
        for i in b1:
            h += i

        print(h)
    elif user_input == "1.b" or user_input == "Sum 2":
        lst = input("Enter the number:")
        lst = lst.split()
        x1 = 0
        j = 0
        sum2 = 0
        while True:
            x1 = float(lst[j])
            sum2 += x1
            j += 1
            if j == len(lst):
                break
        print(sum2)
    elif user_input == "1.c" or user_input == "Sum 3":
        lst = input("Enter the number:")
        lst = lst.split()
        h = 0
        k = 0


        def sum3(p, k1=0):
            k1 += float(lst[p - 1])
            if p == 0:
                return 0
            return sum3(p - 1) + k1


        print(sum3((len(lst))))

    elif user_input == "2" or user_input == "Degree":
        n = int(input("Enter the N number:"))
        i = 0
        while 2 ** (i + 1) <= n:
            i += 1
        print("Degree", 2 ** i)
        print("power", i)
    elif user_input == "arithmetic mean" or user_input == "3":
        lst = input("Enter the number:")
        b = []
        lst = lst.split()
        for i in lst:
            b.append(float(i))
        sum1 = reduce(lambda a1, x: a1 + x, b)
        sum2 = float(sum1)
        lent = len(lst)
        am = float(sum2 / lent)
        print(am)
    elif user_input == "number of Fibonacci" or user_input == "4":
        fib = input("Enter the number:")
        fib = fib.split()
        b1 = []
        for i in fib:
            b1.append(float(i))
        h = sum(b1)
        k = 0
        f1 = 1
        f2 = 1
        i = 2
        n = 2
        fib_sum = 0
        while f1 < h:
            f1 += f2
            f2 = f1 - f2
            n += 1
        if f1 == h:
            print(" {0} is ".format(h), n, "number of Fibonacci")
        else:
            print("-1")
    elif user_input == "6" or user_input == "Substitution":
        lst = input("Enter the number:")
        lst = lst.split()
        print("list", lst)
        mn = min(lst)
        mx = max(lst)
        imn = lst.index(mn)
        imx = lst.index(mx)
        lst[imn], lst[imx] = lst[imx], lst[imn]
        print("list with substitution", lst)
    elif user_input == "Distance" or user_input == "7":
        lst = input("Enter the number for x1 x2 y1 y2 :")
        lst = lst.split()
        x1 = float(lst[0])
        x2 = float(lst[1])
        y1 = float(lst[2])
        y2 = float(lst[3])
        s = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print(s)
    elif user_input == "Schedule" or user_input == "8":
        v = input("Enter the initial velocity:")
        fib1 = v.split()
        b1 = []
        for n in fib1:
            b1.append(float(n))
        v = sum(b1)
        g = 3.71
        alpha = input("Enter the angle :")
        fib = alpha.split()
        b1 = []
        for n in fib:
            b1.append(float(n))
        h = sum(b1)
        m = h * math.pi / 180

        t1 = 1; t2 = 1; t3 = 1; t4 = 1
        while t3 > 0:
            t2 = v * math.sin(m) * t1 - (g * t1 ** 2) / 2
            t1 += 0.01
        t = np.arange(0, t1, 0.01);  t3 = (v * math.sin(m) * t - (g * t ** 2) / 2); t4 = v * math.cos(m) * t
        plt.plot(t3, t4)
        plt.axis('equal'); plt.xlabel(r'$S$'); plt.ylabel(r'$H$'); plt.title(r'$Mars$'); plt.grid(True); plt.show();

    else:
        print("Please check the correctness of the entered commands")
