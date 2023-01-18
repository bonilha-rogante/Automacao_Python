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


for routers in (r1, r2, r3):
    net_connect = ConnectHandler(**routers)
    print(connect.find_prompt())
    net_connect.disconnect()

print('Script finalizado')
