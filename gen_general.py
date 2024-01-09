from package.generate_conf import setup_configurations, get_inventory_path
from package.execute_command import run_ansible_playbook

group_vars = {
    'project_id': 'project-id',
    'region': 'asia-east1',
}

inventory_vars = {
    'group': 'general',
    'hosts': [
    {"hostname": "host2", "IP": "10.128.0.22", "zone": "asia-east1-b"},
    ]
}

instance_vars = {
    'labels': {
        'env': 'dev',
    },
    'subnet': 'projects/project-id/regions/asia-east1/subnetworks/default',
    'tags': ['dev', 'test'],
    'machine_type': 'e2-medium',
    'boot_disk_size': '20',
    'boot_disk_type': 'pd-standard',
    'scopes': 'default'
}

configurations = {
    'group_vars': (group_vars,     'group_vars/all/env.j2',           'group_vars/all/env.yml'),
    'inventory' : (inventory_vars, 'inventory/inventory.instance.j2',  'inventory/inventory.instance.yml'),
    'instance'  : (instance_vars,  'vars/instance/instance_var.j2',   'vars/instance/instance_var.yml')
}

setup_configurations(configurations)
inventory_path = get_inventory_path(configurations)
playbook_path = 'create_general_instance.yml'

run_ansible_playbook(inventory_path, playbook_path)
