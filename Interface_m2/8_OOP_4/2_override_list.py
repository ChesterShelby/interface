class Test(list):
    def append(self, object) -> None:
        for i in range(len(self)):
            self[i] **= object


a = Test([1, 2, 3])
print(a)
a.append(2)
print(a)

print()
b = [1, 2, 3]
print(b)
b.append(2)
print(b)
