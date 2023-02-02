class MyClass:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        x = self.start
        while x < self.stop:
            yield x
            x += self.step


nums = MyClass(0.0, 1.0, 0.1)
for x in nums:
    print(x)

"""
    Итерируемый объект — это объект с методом __iter__, который возвращает итератор.
    
    Итератор — это объект с методом __iter__, который возвращает самого себя, и методом __next__, 
        который возвращает следующий элемент.
        
    Итераторы также являются итерируемыми объектами. Однако они “исчерпываются”, а итерируемые объекты — нет.
"""