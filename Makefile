MANAGE := poetry run python3 manage.py
.PHONY: shell
shell:
		@$(MANAGE) shell_plus --ipython
.PHONY: migrate
migrate:
		@$(MANAGE) migrate
.PHONY: install
install:
		@poetry install
.PHONY: run
run:
		@$(MANAGE) runserver