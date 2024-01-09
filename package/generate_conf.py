from jinja2 import Template


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

def setup_configurations(configs):
    for key, (vars, template_path, output_path) in configs.items():
        try:
            generate_config(vars, template_path, output_path)
            print(f"配置文件 {output_path} 生成成功。")
        except Exception as e:
            print(f"生成配置文件時出錯: {e}")

def get_inventory_path(configs):
    return configs['inventory'][2]
