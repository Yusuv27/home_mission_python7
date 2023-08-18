#Первое задание
sum=0
list=[]
Vinni="пара-ра-рам рам-пам-папам па-ра-па-да"
list_1=Vinni.split()
def bukva(sum):
    for i in list_1:
        for i_2 in i:
            if i_2 == "а":
                sum+=1
        list.append(sum)
        sum=0
    return sum
bukva(sum)
print(list)
sum_3=0
sum_4=0
for i in list:
    for y in list:
        if i == y:
            sum_3+=1
            if sum_3==len(list)*3:
                print("Парам пам-пам")
        else:
            sum_4+=1
if sum_4!=0:
    print("Пам парам")
#Второе задание
def print_operation_table(operation, num_rows=6, num_columns=6):
    a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in a:
        print(*[f"{x:>3}" for x in i])

print_operation_table(lambda x, y: x * y)