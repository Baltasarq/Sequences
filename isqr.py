# isqr (c) 2025 Baltasar MIT License <baltasarq@gmail.com>


import math
from typing import Generator


def isqr_seq(n: int) -> Generator[int]:
    """
        isqr sequence.
        Defined as
            isqr(n) = int(sqrt(n)) # The integer part of the square root.
            # Each n appears 2n + 1 times.
            Wikipedia: https://en.wikipedia.org/wiki/Fibonacci_sequence
            OEIS: https://oeis.org/A000196
        :param n: The number of elements to generate.
        :return: A list with the sequence up to n.
    """
    return (int(math.sqrt(x)) for x in range(n + 1))
...


if __name__ == "__main__":
    print("isqr sequence")
    print(str.join(", ", (str(x) for x in isqr_seq(40))))
...
