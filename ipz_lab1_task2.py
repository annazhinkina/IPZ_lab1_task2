def fibonacci(n):
    if n <= 0:
        return "Число має бути більше 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a + b
        return b

# Введення числа n
n = int(input("Введіть число n для розрахунку n-го числа Фібоначчі: "))
print(f"{n}-е число Фібоначчі: {fibonacci(n)}")