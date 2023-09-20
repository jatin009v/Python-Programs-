def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def series_sum(x, n):
    result = 0
    for i in range(n):
        term = (-1) ** i * (x ** (i + 1) / factorial(i + 1))
        result += term
    return result

try:
    x = float(input("Enter the value of x: "))
    n = int(input("Enter the number of terms in the series: "))
    sum_of_series = series_sum(x, n)
    print(f"The sum of the series is: {sum_of_series:.4f}")
except ValueError:
    print("Please enter valid numeric inputs.")
