HOST = "localhost"  # -> IP da caixa que quero conectar
user = input("Enter your remote account: ")
password = getpass.getpass()

lista_routers = open('routers-ip')

for ip in lista_routers:
    ip = ip.strip()
    print('Configurando roteador: ' + (ip))
    HOST = ip
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    for interface_loopback in range(4):
        tn.write(b"interface loopback " +
                 str(interface_loopback).encode('ascii') + b"\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")

    print(tn.read.all().decode('ascii'))
