from scipy import optimize

W = 255
n = 15

def fun(x):
    return [2 - x[0] * (1 + W * ((2 * x[1])**5 + (2 * x[1])**4 + (2 * x[1])**3 + (2 * x[1])**2 + (2 * x[1])**1 + (2 * x[1])**0) / (x[1]**5 + x[1]**4 + x[1]**3 + x[1]**2 + x[1]**1 + x[1]**0)),
            1 - x[1] - (1 - x[0])**(n - 1)]

sol = optimize.fsolve(fun, [0.5, 0.5])

print(sol)

print(fun(sol))