import getpass
import telnetlib

# HOST = "localhost"  # -> IP da caixa que quero conectar
# user = input("Enter your remote account: ")
# password = getpass.getpass()

# tn = telnetlib.Telnet(HOST)

# tn.read_until(b"login: ")
# tn.write(user.encode('ascii') + b"\n")
# if password:
#     tn.read_until(b"Password: ")
#     tn.write(password.encode('ascii') + b"\n")

# # tn.write(b"ls\n")
# # tn.write(b"exit\n")

# tn.write(b"conf t\n")
# tn.write(b"interface loopback 0 \n")
# tn.write(b"ip address 1.1.1.1 255.255.255.0\n")
# tn.write(b"end\n")
# tn.write(b"exit\n")
# 4

# print(tn.read_all().decode('ascii'))

# # CRIANDO VLANS

# tn.write(b"conf t\n")
# tn.write(b"vlan 2\n")
# tn.write(b"name Sales\n")
# tn.write(b"vlan 3\n")
# tn.write(b"name eng\n")
# tn.write(b"vlan 4\n")
# tn.write(b"name Prod\n")
# tn.write(b"end\n")
# tn.write(b"exit\n")

# # Configurando OSPF

# HOST = "localhost"  # -> IP da caixa que quero conectar
# user = input("Enter your remote account: ")
# password = getpass.getpass()

# tn = telnetlib.Telnet(HOST)

# tn.read_until(b"login: ")
# tn.write(user.encode('ascii') + b"\n")
# if password:
#     tn.read_until(b"Password: ")
# tn.write(password.encode('ascii') + b"\n")


# Criar diversas VLANS através do for


HOST = "localhost"  # -> IP da caixa que quero conectar
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# tn.write(b"ls\n")
# tn.write(b"exit\n")

tn.write(b"conf t\n")

for vlans in range(10, 16):
    tn.write(b"Vlan " + str(vlans).encode('ascii') + b"\n")
    tn.write(b"name Site_ " + str(vLans).encode('ascii') + b"\n")

tn.write(b"interface loopback 0 \n")
tn.write(b"ip address 1.1.1.1 255.255.255.0\n")
tn.write(b"end\n")
tn.write(b"exit\n")


print(tn.read_all().decode('ascii'))

# CRIANDO VLANS


tn.write(b"conf t\n")
tn.write(b"vlan 2\n")
tn.write(b"name Sales\n")
tn.write(b"vlan 3\n")
tn.write(b"name eng\n")
tn.write(b"vlan 4\n")
tn.write(b"name Prod\n")
tn.write(b"end\n")
tn.write(b"exit\n")

# Configurando OSPF

HOST = "localhost"  # -> IP da caixa que quero conectar
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
