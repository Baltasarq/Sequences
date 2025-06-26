# Tribonacci (c) 2025 Baltasar MIT License <baltasarq@gmail.com>


def tribonacci_seq(n: int) -> list[int]:
    """
        Tribonacci sequence.
        Defined as
            #0: 0,
            #1: 1,
            #2: 1,
            ...
            f(n) = f(n - 1) + f(n - 2) + f(n - 3).
            Wikipedia: https://en.wikipedia.org/wiki/Generalizations_of_Fibonacci_numbers#Tribonacci_numbers
            OEIS: https://oeis.org/A000073
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
            case 3:
                toret = [0, 1, 1]
            case _:
                toret = tribonacci_seq(n - 1)
                toret += [toret[-1] + toret[-2] + toret[-3]]
    ...

    return toret
...


def tribonacci_seq_it(n: int) -> list[int]:
    """This is an iterative version of tribonacci_seq()."""
    toret = []

    if n >= 0:
        match n:
            case 1:
                toret = [0]
            case 2:
                toret = [0, 1]
            case 3:
                toret = [0, 1, 1]
            case _:
                toret = [0, 1, 1]
                sum0 = 0
                sum1 = 1
                sum2 = 1

                while len(toret) < n:
                    toret.append(sum0 + sum1 + sum2)
                    sum0 = sum1
                    sum1 = sum2
                    sum2 = toret[-1]
                ...
        ...
    ...

    return toret
...


if __name__ == "__main__":
    print("Tribonacci sequence")
    print(str.join(", ", (str(x) for x in tribonacci_seq_it(20))))
...
