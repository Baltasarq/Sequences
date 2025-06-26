# Primes (c) 2025 Baltasar MIT License <baltasarq@gmail.com>


import math


def is_prime(x: int) -> bool:
    """Determines whether a number is prime.
        :param x: the number to consider.
        :return: True if it is prime, false otherwise.
    """
    toret = False

    if (x % 2 != 0
      and x % 3 != 0
      and x % 5 != 0):
        toret = True

        for i in range(7, int(math.sqrt(x)) + 1):
            if x % i == 0:
                toret = False
                break
            ...
        ...
    ...

    return toret
...


def primes_seq(n: int) -> list[int]:
    """
        Primes sequence.
        Defined as the sequence of numbers which are only divisible by one and themselves.
            Wikipedia: https://en.wikipedia.org/wiki/List_of_prime_numbers
            OEIS: https://oeis.org/A000040
        :param n: The number of elements to generate.
        :return: A list with the sequence up to n.
    """
    toret = []

    if n > 0:
        match n:
            case 1:
                toret = [2]
            case 2:
                toret = [2, 3]
            case 3:
                toret = [2, 3, 5, 7]
            case 4:
                toret = [2, 3, 5, 7, 11]
            case _:
                toret = [2, 3, 5, 7, 11]

                i = 13
                while len(toret) < n:
                    if is_prime(i):
                        toret.append(i)
                    ...

                    i += 1
                ...
    ...

    return toret
...


if __name__ == "__main__":
    print("Primes sequence")
    print(str.join(", ", (str(x) for x in primes_seq(20))))
...
