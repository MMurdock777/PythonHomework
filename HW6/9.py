class Counter:

    def __init__(
            self,
    ):
        self.count = 0

    def increment(self, num: float):
        self.count += num

    def decrement(self, num: float):
        new_count = self.count - num
        if new_count < 0:
            print("Counter cannot go lower than 0")
        else:
            self.count = new_count

    def get_count(self):
        return self.count


a = Counter()
print(a.get_count())
a.increment(5)
print(a.get_count())
a.decrement(4)
print(a.get_count())
