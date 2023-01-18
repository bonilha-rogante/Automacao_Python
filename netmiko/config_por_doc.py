from netmiko import ConnectHandler

# Just pick an 'invalid' device_type
r1 = {
    "device_type": "nome do tipo de caixa",
    "host": "ip",
    "username": "pyclass",
    "password": "invalid"
}

r2 = {
    "device_type": "nome do tipo de caixa",
    "host": "ip",
    "username": "pyclass",
    "password": "invalid"
}

r3 = {
    "device_type": "nome do tipo de caixa",
    "host": "ip",
    "username": "pyclass",
    "password": "invalid"
}

with open('config-router-file') as file:
    config_line = file.read().splitlines()

lista_routers = [r1, r2, r3]

for router in lista_routers:
    connect = ConnectHandler(**routers)
    configure = connect.send_config_set(config_line)
    print(configure)
    connect.disconnect()

print('Script finalizado')
