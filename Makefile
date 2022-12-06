# -----------------------------------------------------------------------------
# Make configuration
# -----------------------------------------------------------------------------
.DEFAULT_GOAL = help

# -----------------------------------------------------------------------------
# Commands (## comments for description)
# -----------------------------------------------------------------------------
.PHONY: fetch
fetch: ## Fetches a day's inputs
	curl 'https://adventofcode.com/2022/day/${AOC_DAY}/input' -H "cookie: session=${ADVENT_OF_CODE_TOKEN}" > inputs/day${AOC_DAY}.txt

.PHONY: setup
setup: ## Creates a day's tests and code
	echo 'def answer(data):\n    pass\n\n\ndef answer_part_two(data):\n    pass\n\n\nif __name__ == "__main__":\n    data = open("inputs/day${AOC_DAY}.txt").read()\n    print(answer(data.strip()))\n    print(answer_part_two(data.strip()))\n' > days/day${AOC_DAY}.py
	echo 'from days.day${AOC_DAY} import (\n    answer,\n    answer_part_two,\n)\n\n\ndef test_answer():\n    data = """\n\n    """\n    assert answer(data.strip()) == 0\n\ndef test_answer_part_two():\n    data = """\n\n    """\n    assert answer_part_two(data.strip()) == 0\n' > tests/test_day${AOC_DAY}.py

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
