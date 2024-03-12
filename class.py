class num_gen:
    def __init__(self):
        self.output = 0
    def generate(self):
        self.output += 1
        return self.output
    def reset(self):
        return 0
    def mul(self, n):
        self.output = self.output*n
        return self.output

gen1 = num_gen()
gen1.generate()
print(gen1.mul(1))
print(gen1.mul(3))
print(gen1.mul(9))
print(gen1.mul(10))

