class MyClass:
    def __init__(self):
        self.data = bytearray()
        self.linecount = 0

    def send(self, part):
        self.linecount += part.count(b'\n')
        self.data.extend(part)
        if self.linecount > 0:
            index = self.data.index(b'\n')
            line = bytes(self.data[:index + 1])
            self.data = self.data[index + 1:]
            self.linecount -= 1
            return line
        else:
            return None


r = MyClass()
print(r.send(b'hello'))
print(r.send(b'world\nit '))
print(r.send(b'works!'))
print(r.send(b'\n'))
