from sys import argv

def primesearch(start, stop, query):
    cursor = start if start % 2 else start + 1
    
    if not query % 2:
        return 1
    
    while cursor < stop:
        if not query % cursor:
            return cursor
        cursor += 2
    
    return 0


if __name__ == "__main__":
    try:
        start, stop, query = (int(x) for x in argv[1:])
    except Exception as e:
        print("Must pass start: int, stop: int, query: int")
        raise e from None
    
    print(f"Prime_Worker({start}, {stop}, {query})")
    result = primesearch(start, stop, query)
    print(f"Found factor: {result}")
    
    exit(1 if result else 0)
