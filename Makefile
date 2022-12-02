# -----------------------------------------------------------------------------
# Make configuration
# -----------------------------------------------------------------------------
.DEFAULT_GOAL = help

# -----------------------------------------------------------------------------
# Commands (## comments for description)
# -----------------------------------------------------------------------------
.PHONY: fetch
fetch: ## Fetches a day's data
	curl 'https://adventofcode.com/2022/day/${AOC_DAY}/input' -H "cookie: session=${ADVENT_OF_CODE_TOKEN}" > data/day${AOC_DAY}.txt

.PHONY: run
run: ## Runs a day
	python days/day${AOC_DAY}.py

.PHONY: watch
watch: ## Run Python tests and watch for changes
	ptw .

.PHONY: test
test: ## Run tests (see also: make [test-js, test-py])
	pytest .

.PHONY: help
help: ##- Print this help text
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  make %-20s\033[0m %s\n", $$1, $$2}'
