#Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

num = int(input("введите значение N : "))
def main_task(n):
    result=1
    for i in range (1,n+1):
        result=result*i
        print (result)
main_task(num)

