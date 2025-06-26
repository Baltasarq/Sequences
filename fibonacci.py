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
            case 1:
                toret = [0]
            case 2:
                toret = [0, 1]
            case _:
                toret = fibonacci_seq(n - 1)
                toret += [toret[-1] + toret[-2]]
    ...

    return toret
...


def fibonacci_seq_it(n: int) -> list[int]:
    """
        This is the iterative version of fibonacci_seq.
    """
    toret = []

    if n > 0:
        match n:
            case 1:
                toret = [0]
            case 2:
                toret = [0, 1]
            case _:
                toret = [0, 1]
                sum0 = 0
                sum1 = 1
                while len(toret) < n:
                    toret.append(sum0 + sum1)
                    sum0 = sum1
                    sum1 = toret[-1]
                ...
        ...
    ...

    return toret
...


if __name__ == "__main__":
    print("Fibonacci sequence")
    print(str.join(", ", (str(x) for x in fibonacci_seq_it(20))))
...
