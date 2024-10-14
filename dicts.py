d = {
    "key1": 1,
    "key2": 2,
    "key3": 3
}

# You can retrieve values
print(d["key2"])
print(d.get("key2"))
# What's the difference?

# You can add or replace keys
# Just use []
d["key4"] = 4
d["key1"] = "one"

# You can set a value 
# only if it doesn't exist
d.setdefault("key4", 0)
# This returns the default value
# Or the current value, if already set

d.items()

# defined using []
l = [ 1, 2, "three", 4 ]

# You can add items
l.append(5)

# You can merge them
l += [ 6, 7, 8 ]

# You can sort them (assuming they contain comparable objects!)
l.sort()
# What's the difference?
sorted(l)
