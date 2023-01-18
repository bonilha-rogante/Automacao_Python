from napalm import get_network_driver
import json

driver = get_network_driver("eos")

device = driver(
    hostname="127.0.0.1",
    username="vagrant",
    password="vagrant",
    optional_args={"port": 12443},
)

device.open()

# output = device.get_facts
# output = device.get_interfaces()
output = device.get_interfaces_counters()
print(json.dumps(output, indent=4))
