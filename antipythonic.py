
# Is this Pythonic?
def my_super_complicated_function(
        i: int = 0,
        x: float = 0.0,
        y: float = 0.0,
        z: float = 0.0
) -> tuple[float, float, float]:
    if type(i) is not int:
        return None
    
    elif type(x) != type(y) != type(z) != float:
        return None
    
    return x + i, y + i, z + i

print(my_super_complicated_function(13, 2.5, 9.1, 6.6))
