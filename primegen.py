def primes():
    yield 2

    history = [2]
    current = 3

    while True:
        yield current
        history.append(current)

        current += 2

        while not all(current % x for x in history):
            current += 2

primegen = primes()

while (p := next(primegen)) < 100:
    print(p)
