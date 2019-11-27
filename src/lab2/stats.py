from typing import List


def mean(data: List[float]) -> float:
    return sum(data) / len(data)


def central_moment(data: List[float], order: int) -> float:
    m = mean(data)
    return sum((e - m) ** order for e in data) / len(data)


def central_moment_2_unbiased(data: List[float]):
    cm = central_moment(data, 2)
    return cm * len(data) / (len(data) - 1)


def central_moment_3_unbiased(data: List[float]):
    cm = central_moment(data, 3)
    l = len(data)
    return cm * l * (l - 1) * l / (l - 2)


def skewness_unbiased(data: List[float]):
    cm2 = central_moment_2_unbiased(data)
    cm3 = central_moment_3_unbiased(data)
    return cm3 / cm2 ** 1.5


def kurtosis_unbiased(data: List[float]):
    l = len(data)
    cm2 = central_moment(data, 2)
    cm4 = central_moment(data, 4)
    return (cm4 / cm2 / cm2 - 3 + 6.0 / (l + 1)) * (l ** 2 - 1) / (l - 2) / (l - 3)
