# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt  в одной строке одно число.

n = int(input("введите значение n : "))
str = (input("введите два значения через пробел : "))
my_list = []
def fill_my_list(n):
    for i in range (n+1):
        my_list.append(i)
    return(my_list)

print(fill_my_list(n))
str=str.split()
result=1
for i in str:
    result=result*my_list[int(i)]
print(f"Результат умножения элементов  = {result}")

