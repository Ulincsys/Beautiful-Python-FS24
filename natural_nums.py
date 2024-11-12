def natural_numbers():
    print("created")

    i = 1

    while True:
        print(f"Sending {i}")
        yield i
        print(f"Sent {i}")
        i += 1

n = natural_numbers()

while True:
    print(next(n))
    input("Press enter to continue:")
