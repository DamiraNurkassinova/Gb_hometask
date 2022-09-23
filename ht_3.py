#1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from random import*
#n=int(input("Введите количество элементов: "))
#list=[0]*n
#for i in range(n):
#    list[i]=randint(-100,100)
#print(list)
#sum=0
#for i in range(0,len(list),2):   
#    sum+=list[i]
#print(sum)

#2.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import math
#n=int(input("Введите количество элементов: "))
#list=[0]*n
#for i in range(n):
#    list[i]=randint(-100,100)
#print(list)
#p=1
#st=[]
#for i in range(math.ceil(len(list)/2)):
#  p=list[i]*list[len(list)-i-1]
#  st.append(p)
#print(st)

#3.Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#import random
#n=int(input("Введите количество элементов списка: "))
#list=[0]*n
#for i in range(n):
#    list[i]=round(random.uniform(0,10),randint(0,4))
#print(list)
#for i in list:
#    a=''
#    for j in range(len(str(i))):
#        if j>str(i).index('.'):
#            a+=str(i)[j]
#    i=int(a)
#s= max(list)- min(list)
#print(s)

#4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#n=int(input("Введите число: "))
#a=''
#while n/2>0:
#    a=a+str(n%2)
#    n=int((n-n%2)/2)
#a1=''
#for i in range(len(a)-1, -1, -1):
#    a1+=a[i]
#print(a1)

#5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов
n=int(input("Введите число: "))
f=[]
a=0
b=1
for j in range(-n,0):
    b, a = a,b-a
    f.insert(0,a)
a=0
b=1
f.append(a)
f.append(b)
for i in range(n-1):
   a, b = b, a+b
   f.append(b)
print(f)