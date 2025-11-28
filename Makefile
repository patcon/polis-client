# Make it simpler to change args during `uv run` calls.
UV_RUN ?= uv run

regenerate: regenerate-py regenerate-ts ## Regenerate all the client code from OpenAPI spec

regenerate-py: ## Regenerate the Python client code
	rm -rf src/polis_client/generated/
	openapi-python-client generate --path openapi/polis.yml --output-path src/polis_client/generated/ --overwrite --meta none

regenerate-ts: ## Regenerate Typescript client code
	rm -rf typescript/src/polis_client/generated
	npx --yes @hey-api/openapi-ts --input ./openapi/polis.yml --output typescript/src/polis_client/generated --silent

# These make tasks allow the default help text to work properly.
%:
	@true

.PHONY: help regenerate regenerate-py regenerate-ts

help:
	@echo 'Usage: make <command>'
	@echo
	@echo 'where <command> is one of the following:'
	@echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
