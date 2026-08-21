# GitHub-User-Activity
In this project, you will build a simple command line interface (CLI) to fetch the recent activity of a GitHub user and display it in the terminal. This project will help you practice your programming skills, including working with APIs, handling JSON data, and building a simple CLI application.
Requirements

The application should run from the command line, accept the GitHub username as an argument, fetch the user's recent activity using the GitHub API, and display it in the terminal. The user should be able to:

    Provide the GitHub username as an argument when running the CLI.
    bash

    github-activity <username>

    Fetch the recent activity of the specified GitHub user using the GitHub API. You can use the following endpoint to fetch the user's activity:
    javascript

    # https://api.github.com/users/<username>/events
    # Example: https://api.github.com/users/kamranahmedse/events

    Display the fetched activity in the terminal.
    javascript

    Output:
    - Pushed 3 commits to kamranahmedse/developer-roadmap
    - Opened a new issue in kamranahmedse/developer-roadmap
    - Starred kamranahmedse/developer-roadmap
    - ...
https://roadmap.sh/projects/github-user-activity
