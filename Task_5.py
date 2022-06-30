#  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа.
import collections
import random 
def number_list(file_in):
    N = 10
    with open("out.txt", "w") as file:
        for i in range(N):
            file.write(str(random.randint(1,N-1))+ '\n')
    print("Содержимое входящего файла ")
    with open (file_in, 'r') as file:
        for i in file:
            print(str(int(i)) + ' ')
    return
def del_krat(file_in):
    collection_nechet = []
    with open (file_in, 'r') as file:
        for i in file:
            if int(i)%2 !=0: collection_nechet.append(str(i))
    with open (file_in, 'w') as file:
        print("Содержимое выходного  файла ")
        for i in collection_nechet:
            print(str(int(i)) + ' ')
            file.write(str(i))
    return


number_list('out.txt')
del_krat("out.txt")


