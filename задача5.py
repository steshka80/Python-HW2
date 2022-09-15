# Реализуйте алгоритм перемешивания списка.

import random

my_list=[5, 4 , -17, 41, 0, 99, -27, 6, 1, -14]
for i in range (0, len(my_list)**2):
    a=random.randint(0, len(my_list)-1)
    b=random.randint(0, len(my_list)-1)
    temp=my_list[a]
    my_list[a]=my_list[b]
    my_list[b]=temp
print(my_list)

