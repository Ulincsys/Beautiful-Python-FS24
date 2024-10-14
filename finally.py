try:
    x = 0
    print(5 / x)
except ValueError as e:
    print("Unreachable code")
finally:
    print("This still runs!")

print("This does NOT run")
