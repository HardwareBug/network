import sys
from scipy import optimize

def main():
	(_, arg1, arg2) = sys.argv
	D = int(arg1)
	n = int(arg2)
	TDATA = 8 * 10**(-6) + 8 * 10**(-6) + 4 * 10**(-6) + ((16 + 28 * 8 + D * 8 + 6) / 96) * 4 * 10**(-6)
	TI = 9 * 10**(-6)
	TS = TDATA + 28 * 10**(-6) + 16 * 10**(-6) + 34 * 10**(-6) + 2 * 0.1 * 10**(-6)
	TC = TDATA + 34 * 10**(-6) + 0.1 * 10**(-6)
	with open('test.txt','w') as f:
		for i in range(255):
			W = i + 1
			def fun(x):
				return [2 - x[0] * (1 + W * ((2 * x[1])**5 + (2 * x[1])**4 + (2 * x[1])**3 + (2 * x[1])**2 + (2 * x[1])**1 + 1) / (x[1]**5 + x[1]**4 + x[1]**3 + x[1]**2 + x[1]**1 + 1)),
                        1 - x[1] - (1 - x[0])**(n - 1)]
			sol = optimize.fsolve(fun, [0, 0])
			print(sol)
			PI = (1 - sol[0])**n
			PS = n * sol[0] * (1 - sol[0])**(n-1)
			PC = 1 - PI - PS
			S = (PS * D * 8) / (PI * TI + PS * TS + PC * TC)
			f.write(str(S * 10**(-6)) + '\t')

if __name__ == '__main__':
    main()