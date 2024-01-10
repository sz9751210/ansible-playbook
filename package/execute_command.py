import pexpect
import os

def run_ansible_playbook(inventory_file, playbook_file):
    # 環境變量
    env = os.environ.copy()
    env['ANSIBLE_HOST_KEY_CHECKING'] = 'False'

    # 構建命令
    command = f"ansible-playbook -i {inventory_file} {playbook_file} -v"

    # 使用 pexpect.spawn 執行命令，並傳入環境變量
    child = pexpect.spawn(command, encoding='utf-8', env=env, timeout=None)

    # 持續讀取輸出直到進程結束
    while True:
        try:
            line = child.readline()
            if not line:
                break
            print(line, end='')
        except pexpect.EOF:
            break

    # 等待子進程結束
    child.wait()

    # 確認進程是否成功完成
    if child.exitstatus != 0:
        print(f"Ansible playbook 執行失敗，返回碼: {child.exitstatus}")
