from random import*
from math import*
#from keyboard import*
print("- Проверка знаний по математкие! -".center(80,"¤"))
tase=int(input("Выбери сложность: 1/2/3 >>> "))
tries=0
while tase not in [1,2,3]:
    try:
        tase=int(input("Выбери сложность: 1/2/3 >>> "))
    except :
        print("ВЫБЕРИ ТОЛЬКО МЕЖДУ 1/2/3 !!!!!!!!!!!!!!!!")
if tase==1:
    min=2
    max=10
    tehed=["+","-"]
elif tase==2:
    min=5
    max=15
    tehed=["+","-","*"]
elif tase==3:
    min=10
    max=20
    tehed=["+","-","*","//"]
while True:
        print("Продолжаем? esc - нет / space - да")
        if v=="e":
            break
        else:
            a=randint(min,max)
            b=randint(min,max)
            tehe=choice(tehed) #choise работает только с рандом
            print(f"{a}{tehe}{b}=", end="")
            vaja=round(eval(str(a)+tehe+str(b)))
            vastus=int(input("="))
            if vastus=int(vaja):
                print("Молодец, правильно!")
            else:
                print("Неверно! Т_Т")
