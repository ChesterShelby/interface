class Test(str):
    def __init__(self, word) -> None:
        super().__init__()

    def __len__(self) -> int:
        return 25


a = Test('hello')
print(len(a))
