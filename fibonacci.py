# Fibonacci (c) 2025 Baltasar MIT License <baltasarq@gmail.com>


def fibonacci_seq(n: int) -> list[int]:
    """
        Fibonacci sequence.
        Defined as
            #0: 0,
            #1: 1,
            ...
            f(n) = f(n - 1) + f(n - 2).
            Wikipedia: https://en.wikipedia.org/wiki/Fibonacci_sequence
            OEIS: https://oeis.org/A000045
        :param n: The number of elements to generate.
        :return: A list with the sequence up to n.
    """
    toret = []

    if n >= 0:
        match n:
            case 0:
                toret = [0]
            case 1:
                toret = [0, 1]
            case _:
                toret = fibonacci_seq(n - 1)
                toret += [toret[-1] + toret[-2]]
    ...

    return toret
...


if __name__ == "__main__":
    print("Fibonacci sequence")
    print(str.join(", ", (str(x) for x in fibonacci_seq(20))))
...
