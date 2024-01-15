from package.generate_conf import setup_configurations, get_inventory_path, merge_and_delete_ini_files
from package.execute_command import run_ansible_playbook

default_dir   = 'playbook'
project_id    = 'project-id'
region        = 'asia-east1'

group_vars = {
    'project_id' : project_id,
    'region'     : region,
}

master_inventory_vars = {
    'group' : 'elastic_master',
    'hosts' : 
    [
        {"hostname": "master", "IP": "10.140.0.28", "zone": "asia-east1-b", "node_name": "master", "node_role": "hot"},
    ]
}

slave_inventory_vars = {
    'group' : 'elastic_slave',
    'hosts' : 
    [
        {"hostname": "slave2", "IP": "10.140.0.30", "zone": "asia-east1-b", "node_name": "slave2", "node_role": "warm"},
        {"hostname": "slave1", "IP": "10.140.0.29", "zone": "asia-east1-b", "node_name": "slave1", "node_role": "warm"},
    ]
}

instance_vars = {
    'machine_type'    : 'e2-medium',
    'boot_disk_size'  : '20',
    'boot_disk_type'  : 'pd-standard',
    'attach_disk_size': '20',
    'attach_disk_type': 'pd-standard',
    'mount_path'      : '/home/elasticsearch',
    'scopes'          : 'default',
    'subnet'          : 'projects/project-id/regions/asia-east1/subnetworks/asia-east1',
    'labels': {
        'env': 'dev',
    },
    'tags': ['dev', 'test'],
}

elasticsearch_vars = {
    'cluster_name' : 'elk',
    'master_ip'    : '10.140.0.28',
    'ilm_policy'   : 'elk',
    'elastic_port' : 9200,
}

monitor_vars = {
    'enabled_node_exporter': 'true',
}

configurations = {
    'group_vars'       : (group_vars,            'group_vars/all/env.j2',                   'group_vars/all/env.yml'),
    'master_inventory' : (master_inventory_vars, 'inventory/inventory.j2',                  'inventory/master_inventory.yml'),
    'slave_inventory'  : (slave_inventory_vars,  'inventory/inventory.j2',                  'inventory/slave_inventory.yml'),
    'elasticsearch'    : (elasticsearch_vars,    'vars/elasticsearch/elasticsearch_var.j2', 'vars/elasticsearch/vars.yml'),
    'instance'         : (instance_vars,         'vars/instance/instance_var.j2',           'vars/instance/vars.yml'),
    'monitor'          : (monitor_vars,          'vars/monitor/monitor_var.j2',             'vars/monitor/vars.yml')
}

setup_configurations(configurations)
inventory_list = ['master_inventory','slave_inventory']
file_list = [configurations[config][2] for config in inventory_list]
inventory_path = f'{default_dir}/inventory/inventory.yml'
merge_and_delete_ini_files(file_list, inventory_path)

master_playbook_path = f'{default_dir}/create_elastic_master_gce.yml'
slave_playbook_path = f'{default_dir}/create_elastic_slave_gce.yml'
run_ansible_playbook(inventory_path, master_playbook_path)
run_ansible_playbook(inventory_path, slave_playbook_path)
