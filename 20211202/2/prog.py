class C:
    field: int = 42
    def __init__(self, value: int = 2):
        self.field = value

    def string(self, level: int = 1) -> str:
        return f"{'<'*level}{self.field}{'>'*level}"

c = C()
print(c.string())
