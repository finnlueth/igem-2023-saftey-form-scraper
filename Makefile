export SHELL := /bin/bash

.DEFAULT_GOAL := help

.PHONY: venv clean help notebook

venv: ## Create a virtual environment
	@python3 -m venv .venv && \
	source .venv/bin/activate && \
	pip install --upgrade pip && \
	pip install -r requirements.txt

clean: ## Delte all environment files
	@rm -rf .venv

notebook: ## Start a jupyter notebook
	source .env/bin/activate\
	&& jupyter-lab

# Miscilaneous commands
help: ## Print this help.
	@grep -E '^[0-9a-zA-Z%_-]+:.*## .*$$' $(firstword $(MAKEFILE_LIST)) | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'

