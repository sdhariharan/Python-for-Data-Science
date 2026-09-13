class UserForLoop:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):

        if self.start < self.end:
            value = self.start
            self.start += 1
            return value

        raise StopIteration


numbers = UserForLoop(1, 11)

for i in numbers:
    print(i)