# SciencyProject

Template for starting a new scientific project, specifically designed to allow keeping track of things with git and GitHub (or other online git repos).

## Structure

See individual subfolders for more complete description of what you should and should not do, but in general:

### `writing`

The writing folder is really just a copy of [ScienceMarkdown](<https://github.com/WetenSchaap/SciencyMarkdown>). It is meant for writing (yes, really!). Write a paper, or anything else here. Don't do analysis here!

### `analysis`

Analysis is for analysis of raw data. Don't put actual raw data here! Write scripts that pull raw data from your hard-drive and do something with it. You can maybe save some very simple intermediate result (like a `.csv` file or something) if it saves time. You should typically find Notebooks here.

### `notes`

Contains everything that does not fit in the other categories. Probably just a mess. But sometimes a mess is useful.

## Python

This project folder comes with its own Python environment in the form of `pyproject.toml`, which can be installed using [`poetry`](https://python-poetry.org): just run `poetry install`. The supplied `pyproject.toml` file should cover most use cases, but you can always add a missing dependency using `poetry add [package]`.

If you discover that you are building an awful lot of functions in your `analysis` folder and would want a custom package, you can just make it (use the `poetry new` command), push it to GitHub, and add it to the Python environment using: `poetry add --editable git+https://github.com/WetenSchaap/PACKAGE.git`. If you make changes, push to GitHub and import by running `poetry update`. Alternatively, you can also point directly to the relevant folder if you are really changing it all the time: `poetry add --editable ./my-package/`. But long term the git way is easier.
