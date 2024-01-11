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
    'group' : 'gcs',
    'hosts' : [
        {"hostname": "bucket-name", "location": "ASIA"},
    ]
}

bucket_vars = {
    'storage_class': 'standard',
}

configurations = {
    'group_vars': (group_vars,     'group_vars/all/env.j2',  'group_vars/all/env.yml'),
    'inventory' : (inventory_vars, 'inventory/inventory.j2', 'inventory/inventory.yml'),
    'bucket'    : (bucket_vars,    'vars/gcs/gcs_var.j2',    'vars/gcs/vars.yml')
}

for key, (content, template_path, output_path) in configurations.items():
    configurations[key] = (content, f"{default_dir}/{template_path}", f"{default_dir}/{output_path}")

setup_configurations(configurations)
inventory_path = get_inventory_path(configurations)

# run_ansible_playbook(inventory_path, playbook_path)
