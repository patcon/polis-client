# Make it simpler to change args during `uv run` calls.
UV_RUN ?= uv run

regenerate: regenerate-py regenerate-ts ## Regenerate all the client code from OpenAPI spec

commit-generated: regenerate
	git add python/src/polis_client/generated/
	git add typescript/dist/
	git add typescript/src/polis_client/generated/
	git commit -m "Adding auto-generated files."

regenerate-py: ## Regenerate the Python client code
	rm -rf python/src/polis_client/generated/
	$(UV_RUN) openapi-python-client generate --path openapi/polis.yml --output-path python/src/polis_client/generated/ --overwrite --meta none

debug-py:
	$(UV_RUN) python python/debug.py

regenerate-ts: ## Regenerate Typescript client code
	rm -rf typescript/polis_client/generated
	rm -rf typescript/dist
	cd typescript && npm run build


test: test-py ## Run all tests

test-py: ## Run Python tests
	$(UV_RUN) pytest

test-live-api: ## Run Python live_api tests
	$(UV_RUN) uv run pytest -m live_api

debug-ts:
	cd typescript && npm run debug-ts

build-py: regenerate-py ## Build a wheel for publishing to PyPI
	rm -rf dist/
	uv build

publish-py: ## Publish built package to PyPI
	uv publish

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
