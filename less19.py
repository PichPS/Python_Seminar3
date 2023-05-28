# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# data = [int(i) for i in input("Введите числа: ").split()]
# for i in range((-1) * len(data), 0, +1):
#     print(data[i], i)

data = [int(i) for i in input("Введите числа: ").split()]
step = int(input("Введите кол-во сдвигов: "))
step = step % len(data)
data = [data[i - step] for i in range(len(data))]
print(data)

#  0  1  2  3  4
# [1, 2, 3, 4, 5]
# -5  -4 -3 -2 -1
# k = 3
# [3, 4, 5, 1, 2]
#  2  3  4  0  1


# 0 - 3 = -3
# 1 - 3 = -2