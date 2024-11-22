# ENPM611 Team1 Project

This project involves developing an application that analyzes GitHub issues for the Poetry open source project and generates valuable insights. The application will retrieve data from a JSON file (poetry_issues.json) and perform detailed analyses on issues to identify trends, highlight key contributors, and categorize issue types, providing an in-depth view of the project's ongoing activity and user engagement.

This application first implements some of the basic functions:

- `data_loader.py`: Utility to load the issues from the provided data file and returns the issues in a runtime data structure (e.g., objects)
- `model.py`: Implements the data model into which the data file is loaded. The data can then be accessed by accessing the fields of objects.
- `config.py`: Supports configuring the application via the `config.json` file. You can add other configuration paramters to the `config.json` file.
- `run.py`: This is the module that will be invoked to run your application. Based on the `--feature` command line parameter, one of the three analyses you implemented will be run. You need to extend this module to call other analyses.


In addition to the utility functions, an example analysis has also been implemented in `example_analysis.py`. It illustrates how to use the provided utility functions and how to produce output.

## Setup

To get started, your team should create a fork of this repository. Then, every team member should clone your repository to their local computer. 


### Install dependencies

In the root directory of the application, create a virtual environment, activate that environment, and install the dependencies like so:

```
pip install -r requirements.txt
```

### configure the data file
For this project, instead of downloading the data file and configuring the path manually or through an environment variable, we've embedded the JSON file directly within the project directory and updated the configuration to point to this file location. 


### Run an analysis

With everything set up, you should be able to run the existing example analysis:

```
python run.py --feature 0
```

That will output basic information about the issues to the command line.


## Feature 1 - Analysis Function
The module first_analysis.py which is invoked by the run.py contains our first analysis of the poetry issues json file. In this analysis, we offer the user the ability to see all the authors of user events, how many events they curated, and the frequency of event_label's for said author. Depending on the file size, the number of authors can make our insights very unpleasant to view, because of this, we sort the author usernames alphabetically and allow the user to select which subgroup to view (A-G, H-N, O-T, U-Z). From there, we list authors within that group and prompt the user to select an author. We then show a breakdown of the frequency of event_label's for the events the author created.

## To run the Analysis
python run.py --feature 1


## Feature 2 - Top 50 commenters Analyzer
The Top 50 commenters Analyzer feature analyzes the count of comments made by each user. This functionality extracts data from a field event_type in the poetry_issue Json. The graph displays the top 50 commenters, ranked by the number of comments they have made. Each bar is labeled with the commenter’s username, and the exact count is displayed above the bar for clarity. This analyzer helps identify the most active contributors in terms of commenting, providing insights into user engagement and collaboration patterns in the repository.

## To run the Top 50 commenters Analyser
python run.py --feature 2


## Feature 3 - Event Impact on Resolution Time Analyzer
The Event Impact on Resolution Time Analyzer aims to explore how specific events influence the time taken to resolve GitHub issues. This feature focuses on key events such as labeling (labeled) and assigning (assigned) that occur throughout an issue's lifecycle. It examines how these events, depending on when they happen (early or late), affect the total resolution time for an issue. This analysis provides insights into which actions may be effective in speeding up or delaying the resolution process of issues.

### Key Features:

Analyzes both closed and open issues, focusing on event types such as labeled and assigned.
Evaluates how early or late an event occurred compared to the issue's creation time.
Plots:
A scatter plot showing the relationship between the time taken to label an issue and the final resolution time.
A scatter plot showing the relationship between the time taken to assign an issue and the resolution time.
This analysis provides valuable information to understand which actions taken during an issue’s lifecycle can help speed up its resolution, potentially leading to better prioritization strategies.

## To run the Event Impact on Resolution Time Analyzer
python run.py --feature 3


## Feature 4 - Yearly Issue Analyzer
The Yearly Issue Analyzer feature analyzes the frequency of issues created each year, based on the created_date field in in the poetry_issue Json. The analyzer reads and aggregates issue counts for each year and generates a bar graph, depicting the trends over time. The graph helps track project activity levels, issue creation trends, and potential surges in demand for issue resolution or project support.

## To run the Yearly Issue Analyzer


python run.py --feature 4

## Explanation of Test case for test_fourth_analysis.py

    test_valid_dataset:

    Validates correct aggregation and graph generation for a typical dataset.

    test_empty_dataset:

    Ensures the program exits gracefully when there’s no data to analyze.

    test_invalid_dates:

    Confirms the program can handle missing or malformed created_date values.

    test_single_year_dataset:

    Validates behavior when all issues are from the same year.

    test_large_dataset:

    Simulates a large dataset to ensure the code is efficient and does not crash.


## Running Unit Tests
To run unit tests for the Fourth Analysis feature:

    python -m pytest test_fourth_analysis.py -v

## VSCode run configuration

To make the application easier to debug, runtime configurations are provided to run each of the analyses you are implementing. When you click on the run button in the left-hand side toolbar, you can select to run one of the three analyses or run the file you are currently viewing. That makes debugging a little easier. This run configuration is specified in the `.vscode/launch.json` if you want to modify it.

The `.vscode/settings.json` also customizes the VSCode user interface sligthly to make navigation and debugging easier. But that is a matter of preference and can be turned off by removing the appropriate settings.
