class Calcer:

    def do_calc(self):
        return 5

    def factorial(self, n):
        res = 1
        for i in range(n+1):
            res *= i
        return res

    def factorial_diff(self, n):
        return self.factorial(n) - self.factorial(n - 1)
