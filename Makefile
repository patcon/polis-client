# Make it simpler to change args during `uv run` calls.
UV_RUN ?= uv run

regenerate: regenerate-py regenerate-ts ## Regenerate all the client code from OpenAPI spec

regenerate-py: ## Regenerate the Python client code
	rm -rf python/src/polis_client/generated/
	uv run openapi-python-client generate --path openapi/polis.yml --output-path python/src/polis_client/generated/ --overwrite --meta none

debug-py:
	uv run python python/debug.py

regenerate-ts: ## Regenerate Typescript client code
	rm -rf typescript/polis_client/generated
	rm -rf typescript/dist
	cd typescript && npm run build

debug-ts:
	cd typescript && npm run debug-ts

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
