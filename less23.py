# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# data = [int(i) for i in input("Введите числа: ").split()]
# count = 0
# for i in range(len(data) - 1):
#     if data[i + 1] > data[i]:
#         count += 1
# print(count)

data = [int(i) for i in input("Введите числа: ").split()]
data = [int(data[i + 1] > data[i]) for i in range(len(data) - 1)]
print(data)
print(sum(data))