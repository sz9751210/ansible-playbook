import os
from jinja2 import Template
import yaml
import configparser


def generate_config(instance_vars, template_path, output_path):

    # 讀取模板文件
    with open(template_path, 'r') as file:
        template_string = file.read()

    # 使用 Jinja2 渲染模板
    template = Template(template_string)
    rendered_template = template.render(instance_vars)

    # 寫入文件
    with open(output_path, 'w') as file:
        file.write(rendered_template)

    print(f"文件已保存到 {output_path}")

def setup_configurations(configs, default_dir = 'playbook'):
    for key, (content, template_path, output_path) in configs.items():        
        full_template_path = os.path.join(default_dir, template_path)
        full_output_path = os.path.join(default_dir, output_path)
        configs[key] = (content, full_template_path, full_output_path)
        try:
            generate_config(content, full_template_path, full_output_path)
            print(f"配置文件 {output_path} 生成成功。")
        except Exception as e:
            print(f"生成配置文件時出錯: {e}")

def get_inventory_path(configs):
    return configs['inventory'][2]

def load_yaml_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return yaml.load(file, Loader=yaml.FullLoader)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return {}
    except yaml.YAMLError as e:
        print(f"Error loading YAML file '{file_path}': {e}")
        return {}

def read_ini_file(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config

def merge_inventory_files(file_paths, merged_file_path):
    merged_config = configparser.ConfigParser()
    for file in file_paths:
        merged_config.read_dict(file)

    with open(merged_file_path, 'w') as configfile:
        merged_config.write(configfile)

def merge_and_delete_ini_files(ini_files, merged_file_path):
    # Read and store the configurations in a list
    config_list = [read_ini_file(file) for file in ini_files]

    # Merge the configurations into a single INI file
    merge_inventory_files(config_list, merged_file_path)

    # Delete the original INI files except for the merged file
    for file in ini_files:
        if file != merged_file_path:
            os.remove(file)
