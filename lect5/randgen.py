# x_{n+1} = (a * x_n + c) % m

class LCG:
    def __init__(self, seed=1, a=1103515245, c=12345, m=2**31):
        self.a = a
        self.c = c
        self.m = m
        self.seed = seed

    def next(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

    def random(self):
        return self.next() / self.m

class Random:
    def __init__(self, seed=1, rndclass=LCG):
        self.rnd = rndclass(seed)

    def randint(self, a, b):
        return a + self.rnd.next() % (b - a + 1)

# def lcg(x, a=1103515245, c=12345, m=2**31):
#     x = (a * x + c) % m
#     return x, x / m

r = Random()
for _ in range(10):
    print(r.randint(10, 20))
