class LIST:
    def __init__(self):
        self.items = []

    def Append(self, item):
        self.items += [item]

    def Insert(self, index, item):
        if index < 0 or index > len(self.items):
            raise IndexError("Index out of bounds")
        self.items = self.items[:index] + [item] + self.items[index:]

    def Remove(self, item):
        found = False
        for index in range(len(self.items)):
            if self.items[index] == item:
                self.items = self.items[:index] + self.items[index+1:]
                found = True
                break
        if not found:
            raise ValueError(f"{item} not found in list")

    def Pop(self, index=-1):
        if index < -len(self.items) or index >= len(self.items):
            raise IndexError("Index out of bounds")
        if index == -1:
            index = len(self.items) - 1
        item = self.items[index]
        self.items = self.items[:index] + self.items[index+1:]
        return item

    def __getitem__(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError("Index out of bounds")
        return self.items[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= len(self.items):
            raise IndexError("Index out of bounds")
        self.items[index] = value

    def __delitem__(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError("Index out of bounds")
        self.items = self.items[:index] + self.items[index+1:]

    def __len__(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def __str__(self):
        return str(self.items)


