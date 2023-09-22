.DEFAULT_GOAL := help

MODULE1=module-1/module1.py
PORTFOLIO=portfolio-project/portfolio-project.py

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: m1
m1: ## executes module 1
	@echo "executing module 1 ..."
	@$(MODULE1) -t addition -n1 1.2 -n2 3.3
	@$(MODULE1) -t subtraction -n1 1.2 -n2 3.3
	@$(MODULE1) -t multiplication -n1 1.2 -n2 3.3
	@$(MODULE1) -t division -n1 1.2 -n2 3.3
	@echo "completed module 1."

pp: ## executes portfolio project
	@echo "executing portfolio project ..."
	@$(PORTFOLIO)
