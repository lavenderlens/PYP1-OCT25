class Calculator:
    def __init__(self):
        self.total = 0
    def add(self, num):
        self.total += num
    def sub(self, num):
        self.total -= num
    def mul(self, num):
        self.total *= num
    def div(self, num):
        if num != 0:
            self.total /= num
    def equals(self):
        snapshot_total = self.total
        self.total = 0
        return snapshot_total
