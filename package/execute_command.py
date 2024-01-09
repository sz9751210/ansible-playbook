import subprocess
import os

def run_ansible_playbook(inventory_file, playbook_file):
    # 設置環境變量
    os.environ['ANSIBLE_HOST_KEY_CHECKING'] = 'False'

    # 構建命令，始終使用 verbose 模式
    command = ['ansible-playbook', '-i', inventory_file, playbook_file, '-vvv']

    # 執行命令
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        print("STDOUT:\n", result.stdout)
        print("STDERR:\n", result.stderr)
    except subprocess.CalledProcessError as e:
        print("錯誤:", e)
