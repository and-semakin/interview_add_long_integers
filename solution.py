from typing import Any, Optional, Iterable


class Digit: 
    def __init__(self, value, previous=None):
        self.value = value
        self.previous = previous

class BigInt:
    """Целое число, не ограниченное по размеру.

    Работает над связным списком.
    """

    tail: Digit

    def __init__(self, tail) -> None:
        self.tail = tail

    @classmethod
    def from_int(cls, num: int) -> 'BigInt':
        """Получить объект BigInt из целого числа.

        :param num: целое число
        """
        tail = None 
        for digit in str(num):
            tail = Digit(int(digit), tail)
        return cls(tail)

    def __iter__(self) -> Iterable[int]:
        cur = self.tail
        while cur.previous:
            yield cur.value
            cur = cur.previous
        yield cur.value

    def to_int(self) -> int:
        """Преобразовать BigInt в int.

        :returns: целое число
        """
        return int(
            ''.join(
                reversed(
                    [str(digit) for digit in self]
                )
            )
        )

    def __add__(self, other) -> 'BigInt':
        # Написать здесь эффективное решение, работающее над списками
        # вместо этой заглушки:
        return BigInt.from_int(self.to_int() + other.to_int())


if __name__ == '__main__':
    s = BigInt.from_int(100) + BigInt.from_int(99)
    assert s.to_int() == 199
