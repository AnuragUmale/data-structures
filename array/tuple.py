class TUPLE:
    def __init__(self, elements):
        self.items = elements  

    def __getitem__(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError("Index out of bounds")
        return self.items[index]

    def __len__(self):
        return len(self.items)

    def Count(self, value):
        count = 0
        for item in self.items:
            if item == value:
                count += 1
        return count

    def Index(self, value):
        for i, item in enumerate(self.items):
            if item == value:
                return i
        raise ValueError(f"{value} not found in TUPLE")

    def __contains__(self, value):
        for item in self.items:
            if item == value:
                return True
        return False

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.items):
            result = self.items[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

