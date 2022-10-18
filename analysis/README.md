# analysis

The `analysis` folder should contain all analysis, split up into subfolders. So `./interestingThingA` would contain one or more Python files, that do *something* to raw data.

In general, there should be no data in these folders, only analysis, and maybe some very simple intermediate result (like a `.csv` file or something). This way we can still keep track of the entire folder using `git`. The scripts and other things in here should get their data from the raw data source, in a reproducible way if at all possible.
