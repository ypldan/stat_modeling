# 1) (2 балла) Проверить точность моделирования с помощью теста «совпадения моментов» с уровнем
# значимости ε = 0.05.
# 2) (2 балла) Проверить точность моделирования с помощью теста «ковариация» с уровнем
# значимости ε = 0.05. В качестве параметра t выбрать значение 30. Вывести все такие значения лага,
# при котором тест не проходит.
# 3) (3 балла) Проверить точность моделирования с помощью теста «равномерность двумерного
# распределения» с уровнем значимости ε = 0.05. Параметр k выбирать самостоятельно.
# 4) (1 балл) Вычислить выборочные коэффициенты корреляции r τ = corr{a t ,a t+τ }, τ=1,…,30.
# 5) (1 балл) Для выходных данных построить гистограмму с числом столбцов = 10.
# 6) (1 балл) Определить длину периода выходной последовательности для МКМ.

from typing import List
from bisect import bisect_right


BASIC_MID = 1 / 2
BASIC_DISP = 1 / 12


def mean(data: List[float]):
    return sum(data) / len(data)


def disp(data: List[float]):
    m = mean(data)
    return sum(((d - m) ** 2 for d in data)) / (len(data) -1)


def sorted_copy(data: List[float]):
    copy = data.copy()
    copy.sort()
    return copy


def kolmogorov(data: List[float]):
    copy = sorted_copy(data)
    result = 0
    for i, value in enumerate(result):
        f = min(max(value, 0.), 1.0)
        f_hat = (i + 1) / len(copy)
        current = abs(f_hat - f)
        result = max(result, current)
    return result


def calculate_bins(data: List[float], n=10, min_v=0, max_v=1):
    copy = sorted_copy(data)
    result = [0] * n
    stride = (max_v - min_v) / n
    previous = 0
    for i in range(n):
        threshold = stride * (i + 1)
        count = bisect_right(copy, threshold)
        result[i] = count - previous
        previous = count
    return result


def chi_square(data: List[float]):
    bins = calculate_bins(data)
    result = 0
    prob = len(data) / 10
    for count in bins:
        result += (count - prob) ** 2 / prob
    return result
