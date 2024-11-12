
from typing import Any


class MyClass:
    def __init__(self, x = 0) -> None:
        print("Created class")
        self.the_attribute = x

    def __call__(self) -> Any:
        print("Called class with value:", self.the_attribute)

    def __int__(self) -> int:
        return int(self.the_attribute)

if __name__ == "__main__":
    c = MyClass()

    c.the_attribute = input("Enter a number: ")

    c()

    print(int(c))
