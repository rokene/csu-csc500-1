.DEFAULT_GOAL := help

MODULE1=module-1/module1.py
MODULE3D=module-3/bank_ledger.py
MODULE3=module-3/module3.py
MODULE4D=module-4/factorial.py
MODULE5D=module-5/discussion.py
MODULE5=module-5/module5.py
MODULE6D=module-6/discussion.py
MODULE7=module-7/module7.py
MODULE8D=module-8/discussion.py
PORTFOLIO=portfolio_project/portfolio_project.py

.PHONY: help
help:
	@echo "doing it"
	@grep -E '^[a-zA-Z_-]+:.*?## .*' $(MAKEFILE_LIST) | sort

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

.PHONY: m4-d
m4-d: ## executes module 4 discussion sample code
	@echo "executing module 4 discussion code ..."
	@$(MODULE4D)
	@echo "completed module 4 discussion code."

.PHONY: m5-d
m5-d: ## executes module 5 discussion sample code
	@echo "executing module 5 discussion code ..."
	@$(MODULE5D)
	@echo "completed module 5 discussion code."

.PHONY: m5
m5: ## executes module 5
	@echo "executing module 5 ..."
	@$(MODULE5) --part 1
	@$(MODULE5) --part 2
	@echo "completed module 5."

.PHONY: m6-d
m6-d: ## executes module 6 discussion sample code
	@echo "executing module 6 discussion code ..."
	@$(MODULE6D)
	@echo "completed module 6 discussion code."

.PHONY: m7
m7: ## executes module 7
	@echo "executing module 7 ..."
	@$(MODULE7)
	@echo "completed module 7."

.PHONY: m8-d
m8-d: ## executes module 8 discussion sample code
	@echo "executing module 8 discussion code ..."
	@$(MODULE8D)
	@echo "completed module 8 discussion code."

.PHONY: pp-m1
pp-m1: ## executes the portfolio project milestone 1
	@echo "executing portfolio project milestone 1 ..."
	@$(PORTFOLIO) -f --part 1
	@echo "executing portfolio project milestone 1 completed."

.PHONY: pp-m2
pp-m2: ## executes the portfolio project milestone 2
	@echo "executing portfolio project milestone 2 ..."
	@$(PORTFOLIO) -f --part 2
	@echo "executing portfolio project milestone 2 completed."
