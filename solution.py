from typing import Any, Optional


class LinkedListNode:
    value: Any
    next: Optional['LinkedListNode']

    def __init__(self, value: Any, next: Optional['LinkedListNode'] = None) -> None:
        self.value = value
        self.next = next

    def __iter__(self) -> 'LinkedListNode':
        return LinkedListIterator(self)


class LinkedListIterator:
    head: Optional[LinkedListNode]

    def __init__(self, head: Optional[LinkedListNode] = None):
        self.head = head

    def __iter__(self) -> 'LinkedListIterator':
        return self

    def __next__(self) -> Any:
        if not self.head:
            raise StopIteration
        value = self.head.value
        self.head = self.head.next
        return value


class BigInt:
    """Целое число, не ограниченное по размеру.

    Работает над связным списком.
    """

    head: LinkedListNode

    def __init__(self, head) -> None:
        self.head = head

    def __iter__(self) -> 'LinkedListNode':
        return LinkedListIterator(self.head)

    @classmethod
    def from_int(cls, num: int) -> 'BigInt':
        """Получить объект BigInt из целого числа.

        :param num: целое число
        """
        head: Optional[LinkedListNode] = None
        prev: Optional[LinkedListNode] = None

        for digit in str(num):
            head = LinkedListNode(int(digit), next=prev)
            prev = head

        return cls(head)

    def to_int(self) -> int:
        """Преобразовать BigInt в int.

        :returns: целое число
        """
        str_list = reversed([str(value) for value in self.head])
        return int(''.join(str_list))

    def __add__(self, other) -> 'BigInt':
        # Написать здесь эффективное решение, работающее над списками
        # вместо этой заглушки:
        return BigInt.from_int(self.to_int() + other.to_int())


if __name__ == '__main__':
    s = BigInt.from_int(100) + BigInt.from_int(99)
    assert s.to_int() == 199
