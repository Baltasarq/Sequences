# Padovan (c) 2025 Baltasar MIT License <baltasarq@gmail.com>


def padovan_seq(n: int) -> list[int]:
    """
        Padovan sequence.
        Defined as
            #0: 1,
            #1: 1,
            #2: 1,
            ...
            f(n) = f(n - 2) + f(n - 3).
            Wikipedia: https://en.wikipedia.org/wiki/Padovan_sequence
            OEIS: https://oeis.org/A000931
        :param n: The number of elements to generate.
        :return: A list with the sequence up to n.
    """
    toret = []

    if n > 0:
        match n:
            case 0:
                toret = [1]
            case 1:
                toret = [1, 1]
            case 2:
                toret = [1, 1, 1]
            case _:
                toret = padovan_seq(n - 1)
                toret += [toret[-2] + toret[-3]]
    ...

    return toret
...


if __name__ == "__main__":
    print("Padovan sequence")
    print(str.join(", ", (str(x) for x in padovan_seq(20))))
...
