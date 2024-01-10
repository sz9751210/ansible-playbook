.PHONY: help up-% list-scripts

PYTHON := python3
SCRIPT_PREFIX := gen_
PLAYBOOK_DIR := playbook
UP_PLAYBOOK := gce gcs
DOWN_PLAYBOOK := gce

help:
	@echo "Available commands:"
	@echo "  up/down-<script>: Run the gen_<script>.py script"
	@echo "  list-scripts: List all available up/down-<script> commands"
	@echo "  list-playbooks: List all available playbooks"
	@echo "Allowed up scripts are: $(UP_PLAYBOOK)"
	@echo "Allowed down scripts are: $(DOWN_PLAYBOOK)"
up-%:
	@$(PYTHON) $(SCRIPT_PREFIX)$*.py $(PLAYBOOK_DIR)/create_$*.yml|| echo "Script $(SCRIPT_PREFIX)$*.py does not exist."

down-%:
	@$(PYTHON) $(SCRIPT_PREFIX)$*.py $(PLAYBOOK_DIR)/delete_$*.yml|| echo "Script $(SCRIPT_PREFIX)$*.py does not exist."

list-scripts:
	@echo "Available up-<script> commands:"
	@sh -c "ls $(SCRIPT_PREFIX)*.py | sed 's/$(SCRIPT_PREFIX)\(.*\)\.py/up-\1/'"

list-playbooks:
	@echo "Available playbook identifiers:"
	@find $(PLAYBOOK_DIR) -name 'create_*.yml' | sed -e 's|.*/\(.*\)\.yml|\1|'
	@find $(PLAYBOOK_DIR) -name 'delete_*.yml' | sed -e 's|.*/\(.*\)\.yml|\1|'
