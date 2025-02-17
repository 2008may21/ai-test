from netaddr import IPNetwork, IPSet

def find_unused(supernet, used_subnets):
    supernet_network = IPNetwork(supernet)
    used_networks = IPSet([IPNetwork(subnet) for subnet in used_subnets])
    
    unused_networks = IPSet(supernet_network) - used_networks
    largest_unused_subnets = [str(subnet) for subnet in unused_networks.iter_cidrs()]
    
    return largest_unused_subnets

# Example usage:
# supernet = '192.168.0.0/16'
# used_subnets = ['192.168.1.0/24', '192.168.2.0/24']
# print(find_unused(supernet, used_subnets))
