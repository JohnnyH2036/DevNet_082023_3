from netmiko import ConnectHandler

def gather_info(device):
    with ConnectHandler(**device) as ssh:
        output = {}
        output['interface_brief'] = ssh.send_command('show ip interface brief')
        output['ip_route'] = ssh.send_command('show ip route')
    return output

def configure_router(device):
    with ConnectHandler(**device) as ssh:
        ssh.send_config_set([
            'interface Loopback15',
            'ip address 15.16.17.18 255.255.255.0',
            'interface Loopback18',
            'ip address 16.17.18.1 255.255.255.0'
        ])
        ssh.send_config_set(['ip route 0.0.0.0 0.0.0.0 Loopback15'])

if __name__ == "__main__":
    csr_device = {
        'device_type': 'cisco_ios',
        'host': '192.168.56.101',
        'username': 'cisco',
        'password': 'cisco123!',
    }

    initial_info = gather_info(csr_device)
    print("Initial Information:")
    print("Show IP Interface Brief:")
    print(initial_info['interface_brief'])
    print("Show IP Route:")
    print(initial_info['ip_route'])

    configure_router(csr_device)
    print("\nConfiguration Complete!")

    updated_info = gather_info(csr_device)
    print("\nUpdated Information:")
    print("Show IP Interface Brief:")
    print(updated_info['interface_brief'])
    print("Show IP Route:")
    print(updated_info['ip_route'])
