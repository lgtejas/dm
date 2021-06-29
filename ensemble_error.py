import math


def _combinations(n , k):
    numerator= math.factorial(n)
    denominator = math.factorial(k) * math.factorial(n-k)
    return  numerator/denominator

e = 0.35
end = 25
i = 13
error_eq = 0
while i <= end:
    p = end / i
    c = _combinations(end, i)
    print(f' {end}/{i}  = {p} , c={c}')
    error_eq = error_eq + c * ( pow(e , i) * pow (1-e, end-i))
    i = i +1
print(error_eq)