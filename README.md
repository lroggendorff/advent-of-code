Working through [Advent of Code](https://adventofcode.com/)
in Python
for funsies
and very little profit.

# Install dependencies

```
brew install pyenv
pyenv install 3
pip install -r requirements.txt
```

# Start a new year

```
export AOC_YEAR=2023
make init
```

# Set up for a new day

```
AOC_DAY=3 make setup
```

# Fetch input data

```
export ADVENT_OF_CODE_TOKEN="token from your adventofcode.com session cookie"
AOC_DAY=3 make fetch
```

# Run tests and watch for changes

```
make watch
```

# Run a day's code

```
AOC_DAY=3 make run
```
