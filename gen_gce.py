from package.generate_conf import setup_configurations, get_inventory_path
from package.execute_command import run_ansible_playbook
import sys

if len(sys.argv) != 2:
    print('didn\'t get playbook path')
    sys.exit(1)

playbook_path = sys.argv[1]
default_dir   = 'playbook'
project_id    = 'project-id'
region        = 'asia-east1'

group_vars = {
    'project_id' : project_id,
    'region'     : region,
}

inventory_vars = {
    'group' : 'gce',
    'hosts' : 
    [
        {"hostname": "host2", "IP": "10.128.0.22", "zone": "asia-east1-b"},
    ]
}

instance_vars = {
    'machine_type'   : 'e2-medium',
    'boot_disk_size' : '20',
    'boot_disk_type' : 'pd-standard',
    'scopes'         : 'default',
    'subnet'         : 'projects/project-id/regions/asia-east1/subnetworks/default',
    'labels': {
        'env': 'dev',
    },
    'tags': ['dev', 'test'],
}

monitor_vars = {
    'enabled_node_exporter': 'true',
}

configurations = {
    'group_vars': (group_vars,     'group_vars/all/env.j2',                'group_vars/all/env.yml'),
    'inventory' : (inventory_vars, 'inventory/inventory.instance.j2',      'inventory/inventory.instance.yml'),
    'instance'  : (instance_vars,  'vars/instance/instance_var.j2',        'vars/instance/vars.yml'),
    'monitor'   : (monitor_vars,   'vars/monitor/monitor_var.j2',          'vars/monitor/vars.yml')
}

for key, (content, template_path, output_path) in configurations.items():
    configurations[key] = (content, f"{default_dir}/{template_path}", f"{default_dir}/{output_path}")

setup_configurations(configurations)
inventory_path = get_inventory_path(configurations)

run_ansible_playbook(inventory_path, playbook_path)
