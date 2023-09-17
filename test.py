import timeit
import matplotlib.pyplot as plt

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)

def f2(n):
    arr = [0, 1]
    for i in range(2, n+1):
        arr.append(arr[i-1]+arr[i-2])
    return arr[n]

i_values = list(range(21))
time_values = []
time_values2 = []

print('Наивный:')
for i in i_values:
    med = 0
    for j in range(10000):
        med += timeit.timeit(lambda: f(i), number=1)
    med /= 10000
    time_values.append(med)
    print(med)

print('\nКэшированный:')
for i in i_values:
    med = 0
    for j in range(0, 10000):
        med += timeit.timeit(lambda: f2(i), number=1)
    med /= 10000
    time_values2.append(med)
    print(med)

plt.plot(i_values, time_values, linestyle='-')
plt.plot(i_values, time_values2, linestyle='-')
plt.xlabel('Номер числа фибоначчи')
plt.ylabel('Среднее время выполнения (секунды)')
plt.title('Зависимость времени выполнения от номера числа')
plt.xticks(i_values)
plt.grid(False)
plt.show()
