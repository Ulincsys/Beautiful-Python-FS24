if True:
    x = 5

if "x" in globals():
    # x DEFINITELY exists
    print(x)

# Global scope
x = 5

def func():
    # Local scope
    x = 2

# Back to global scope
func()
print(x)

def outer():
    # Local scope
    def inner():
        # Also local?
        pass

