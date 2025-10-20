#1 номер
s=input("Введите строчку: ")
x=0
for y in s.split():
    if y[0]=="е" or y[0]=="Е":
        x+=1
print(x)
#2 номер
s=input("Введите строчку: ")
x=0
while ":" in s:
    s=s.replace(":", "%", 1)
    x+=1
print(x)
#3 номер
s=input("Введите строчку: ")
x=0
while "." in s:
    s = s.replace(".", "", 1)
    x += 1
print(x)
#4 номер
s=input("Введите строчку: ")
x=0
while "а" in s:
    s = s.replace("а", "о", 1)
    x += 1
print(x, len(s))
#5 номер
s=input("Введите строчку: ")
print(s.lower())
#6 номер
s=input("Введите строчку: ")
x=0
while "а" in s:
    s = s.replace("а", "", 1)
    x += 1
print(x)
#7 номер
s=input("Введите строчку: ")
z=len(s)//2
while "п" in s[0:z]:
    s = s.replace("п", "*", 1)
print(s)
# 8 номер
s=input("Введите строчку: ")
print(len(s.split()))
#9 номер
s=input("Введите строчку: ")
s1=input("Слово для подсчета: ")
print(s.split().count(s1))
#10 номер
s=input("Введите строчку: ")
print(s.title())
#11 номер

s=input("Введите строчку: ")
x=0
z=0
for u in s:
    if u=="н":
        x+=1
    else:
        z=max(x,z)
        x=0
z=max(x,z)
print(z, s.replace("!", "."))
#12 номер

s=input("Введите строчку: ")
for u in s.split():
    if u[-1]=="я":
        print(u)
#13 номер
s=input("Введите строчку: ")
print(s.split("(")[1].split(")")[0])
#14 номер
s=input("Введите строчку: ")
for u in s.split():
    if u[-1]=="я" or u[0]=="а":
        print(u)
#15 номер
s=input("Введите строчку: ")
print(s.count("т"))