import pytest
from solution import BigInt, Digit


@pytest.mark.parametrize(('number', 'expected_list'), [
    (
        1,
        [1]
    ),
    (
        123,
        [3, 2, 1]
    ),
    (
        1000,
        [0, 0, 0, 1]
    )
])
def test_bigint_from_int(number, expected_list) -> None:
    bigint = BigInt.from_int(number)
    assert list(bigint) == expected_list


def test_bigint_to_int() -> None:
    assert BigInt(Digit(1)).to_int() == 1
    assert BigInt(
        Digit(
            3,
            previous=Digit(
                2,
                previous=Digit(1)
            )
        )
    ).to_int() == 123


@pytest.mark.parametrize(('a', 'b'), [
    (0, 0),
    (1, 1),
    (1, 1000000),
    (123, 0),
    (1, 0),
    (0, 1),
    (5, 5),
    (9, 0),
    (0, 9),
    (9, 1),
    (19, 1),
    (18, 3),
    (99, 203),
])
def test_bigint_add(a, b):
    n1 = BigInt.from_int(a)
    n2 = BigInt.from_int(b)
    s = n1 + n2
    assert s.to_int() == a + b
