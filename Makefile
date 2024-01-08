.PHONY: up-general

up-general:
	ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i inventory/inventory.instance.create.yml create_general_instance.yaml -v
