from statistics import mean


def mse(real, expected):
    return mean((real - expected) ** 2)


def mape(real, expected):
    return mean(abs(real - expected) / real)


def lad(real, expected):
    return max(abs(real - expected))
