.PHONY: help up-% list-scripts

PYTHON := python3
SCRIPT_PREFIX := gen_

help:
	@echo "Available commands:"
	@echo "  up-<script>: Run the gen_<script>.py script"
	@echo "  list-scripts: List all available up-<script> commands"

up-%:
	@$(PYTHON) $(SCRIPT_PREFIX)$*.py || echo "Script $(SCRIPT_PREFIX)$*.py does not exist."

list-scripts:
	@echo "Available up-<script> commands:"
	@sh -c "ls $(SCRIPT_PREFIX)*.py | sed 's/$(SCRIPT_PREFIX)\(.*\)\.py/up-\1/'"
