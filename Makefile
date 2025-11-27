# Make it simpler to change args during `uv run` calls.
UV_RUN ?= uv run

codegen: ## Make the generated client code from OpenAPI spec
	openapi-python-client generate --path openapi/polis.yml --output-path src/polis_client/generated/ --overwrite --meta none

# These make tasks allow the default help text to work properly.
%:
	@true

.PHONY: help codegen

help:
	@echo 'Usage: make <command>'
	@echo
	@echo 'where <command> is one of the following:'
	@echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
