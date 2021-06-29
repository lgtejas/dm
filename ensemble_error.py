import math


def _combinations(n, k):
    numerator = math.factorial(n)
    denominator = math.factorial(k) * math.factorial(n - k)
    return numerator / denominator

def _ensemble_error(e, i, end):
    error = 0
    while i <= end:
        p = end / i
        c = _combinations(end, i)
        error = error + c * (pow(e, i) * pow(1 - e, end - i))
        i = i + 1
    return  round(error,3)


if "__main__" == __name__:
    e = float(input('Please enter the error rate : '))
    end = int(input('Please enter the total ensemble elements ='))
    i = math.ceil(float(end) / 2)
    error = _ensemble_error(e, i, end)
    print(f'Ensemble error = {error}')
