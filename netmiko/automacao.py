from netmiko import ConnectHandler

# Just pick an 'invalid' device_type
nome_variavel = {
    "device_type": "nome do tipo de caixa",
    "host": "ip",
    "username": "pyclass",
    "password": "invalid"
}

net_connect = ConnectHandler(**nome_variavel)

# Configurar caixa
loopback13 = ['interface loopback 13']

configurar = connect.send_config_set(loopback13)

output = net_connect.send_command("show ip int brief")
