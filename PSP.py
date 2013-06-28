import socket
IP = socket.gethostbyname(socket.gethostname())
f = open(raw_input("File:"))
addcode = """
def __PSP__():
    import socket
    if socket.gethostbyname(socket.gethostname()) != {0}:
        import sys
        sys.exit()
__PSP__()
""".format(IP)
new = addcode
with open(raw_input("File:")) as f:
    for line in f:
        new =  new + line.strip()
n = open(raw_input("New file:"),"w")
n.write(new)
