from subprocess import Popen, PIPE

"""Given no input on invocation, `cat` will
read from stdin until EOF is reached. Here
we are capturing stdin and stdout for the
subprocess.
"""
c = Popen(["cat"], stdin=PIPE, stdout=PIPE)

# This is the content we will send to `cat`
s = input("Enter a prompt: ")

"""Popen.communicate will send our input string
(as bytes) to the process, followed by EOF. It
then waits for the subprocess to exit, and
returns a tuple containing (stdout, stderr) from
the process, also as bytes.
"""
# This is a BLOCKING CALL!!!
out = c.communicate(s.encode())

print(f"Output was: {out}")
