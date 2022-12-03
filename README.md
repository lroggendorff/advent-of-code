Working through [Advent of Code 2022](https://adventofcode.com/2022)
for funsies and very little profit.

# Install dependencies

```
brew install pyenv
pyenv install 3.10.8
pip install -r requirements.txt
```

# Fetch data

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
