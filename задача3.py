# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ 
# и выведите на экран их сумму.

num = int(input("введите значение k : "))
def main_task(k):
    for i in range (1, k+1):
        result=((1+1/i)**i)
        print(result)
main_task(num)
