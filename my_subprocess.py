from subprocess import run, Popen

# Run the `echo` command, with args ["hello", "world!"]
run(["echo", "hello", "world!"])

print("Sleeping")
run(["sleep", "5"])
print("Slept")

# Popen(["bash", "-c", "sleep 5 && echo test"])

print("sleeping")
p = Popen(["sleep", "5"])
p.wait()
print("slept")

