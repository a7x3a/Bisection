def bisection(f , a , b ):
    fa = f(a)
    fb = f(b)
   

    if fa * fb > 0:
        print("f(a) and f(b) must be different signs :(")
        return None

    for _ in range(100):  # 100 iteration
        c = (a + b) / 2
        fc = f(c)

        if fc == 0:
            return c
        if fa * fc > 0:
            a = c
            fa = fc
        if fb * fc > 0:
            b = c
            fb = fc

    return c


func = lambda x: x ** 2 - 3 # x^2 - 3

a = 1
b = 2

x = bisection(func, a, b)
print(f"Solution Found : {x}")

