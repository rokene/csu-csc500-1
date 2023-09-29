.DEFAULT_GOAL := help

MODULE1=module-1/module1.py
MODULE3D=module-3/bank-ledger.py
MODULE3=module-3/module3.py
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

.PHONY: m3
m3: ## executes module 3
	@echo "executing module 3 part 1 ..."
	@$(MODULE3) --part 1
	@echo "executing module 3 part 2 ..."
	@$(MODULE3) --part 2
	@echo "completed module 3."

.PHONY: m3-d
m3-d: ## executes module 3 discussion sample code
	@echo "executing module 3 discussion code ..."
	@$(MODULE3D)
	@echo "completed module 3 discussion code."

pp: ## executes portfolio project
	@echo "executing portfolio project ..."
	@$(PORTFOLIO)
