#1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#n=float(input("Введите число: "))
#if n<0:
#    n=-n
#while n%1>0:
#    n*=10
#sum=0    
#while n>0:
#    sum+=n%10
#    n=(n-n%10)/10
#print(int(sum))   

#2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#n=int(input("Введите число: "))
#a=1
#for i in range(1,n+1):
#    print(a)
#    a=i*(i+1)



#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#n=int(input("Введите число: "))
#sum=0
#for i in range(1, n+1):
#    n=(1+1/i)**i
#    sum+=n
#print(sum)

#4.Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
#from random import randint

#n=int(input("Введите число: "))
#s=[0]*n
#for i in range(n):
#    s[i]=randint(-n,n)
#print(s)
#path='pos.txt'
#a=open(path,'w')
#f=[0]*randint(0,n-1)
#for i in range(len(f)):
#    f[i]=randint(0,n-1)
#    a.writelines(str(f[i]))
#    a.write('\n')
#a.close()
#p=1
#a=open(path,'r')
#for i in a.readlines():
#    i=int(i)
#    p=p*s[i]
#print(p)

#5.Реализуйте алгоритм перемешивания списка
import random
from random import randint


n=int(input("Введите число: "))
s=[0]*n
for i in range(n):
    s[i]=randint(-n,n)
print(s)
random.shuffle(s)
print(s)