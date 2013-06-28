import socket,os
IP = socket.gethostbyname(socket.gethostname())
addcode = """
def __PSP__():
    import socket
    if socket.gethostbyname(socket.gethostname()) != {0}:
        import sys
        sys.exit()
__PSP__()
""".format(IP)
new = addcode
with open("oldcode.py") as f:
    for line in f:
        new =  new + line.strip()
n = open("newcode.py:","w")
n.write(new)
os.remove("oldcode.py")
os.system("python setup.py install")#assumes py2exe's setup file is there
