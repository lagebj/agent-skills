.PHONY: validate check

validate:
	python3 scripts/validate-skills.py

check: validate
