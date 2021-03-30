# How to contribute

[DomeCode](https://discord.domecode.com) has a partly open-source codebase so you can be a part of the development team on your own time without getting involved in the startup culture. If you solve an issue, it'd be highly appreciated if you upstream your changes to the open-source repository.

Most open source development activity is coordinated through our Discord. The Wiki is still a work in progress and the README.md does a good job at getting you started.


## Getting Started

- Join our [Discord](https://discord.domecode.com/)
- Make sure you have a [GitHub account](https://github.com/signup/free)
- Fork [our repository(ies)](https://github.com/the-domecode) on GitHub
- Run the migrations.
- Run this on your localhost.

**Things to take care of :**

- Use the `devmanage.py` command instead of `manage.py` command on development environments.

- This project uses `decouple` so make sure to make a local `.env` file in your root directory of the project containing all the variables with dummy values.

- The variables you should include are the ones with `config()` next to them in the `devmanage.py` file. If there's an error due to the missing value of an environment variable, it can be fixed with ease by passing in appropriate variables. It's pretty generic stuff. 

- Once you're done with that, you can start working on fixing the nitty gritty details, make improvements, finding issues and reporting them in the issues tab of this repository. Create PRs and have fun!

**Note : You should take note of that if you are working on the fork of this repository, you have to sync it before pushing changes to the fork and making a PR to this repo. How to sync changes made on this repo to your fork? Have a look at [this](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork).**

## Code Style

- Flake8 is used.

- Make sure the code has docstrings unless of course the code is pretty generic and is self explainable. If you came up with a solution by yourself on some sort of problem, make sure to include comments and/or docstring(s).

- The static files root is the `notes` directory which is weird and I'm aware of it but since the inception of this platform, the root static directory has been situated there and it's alright. `notes` app was the first app on this, anyway.

- Please make sure you are using pre-commit hooks to avoid linting problems from Github Actions later.

## Making Pull Requests

The pull requests should be made to the `dev` branch. The code will be tested there, pushed to `master`, tested again and then make it to deployment environment through the private codebase.

Please make sure that any new code you add is extensively documented through comments and/or docstrings. Your code should be maintainable.

- [X] Code is linted properly.
- [X] Code is documented.
- [X] Code relates directly to an issue made on our repository. If it does not, make sure to open an issue first and then link the PR to that issue.
- [X] Code is not low quality. Low quality refers to spaghetti code here.

## Working on the internal development team

You can become a part of our community by getting involved on our [Discord](https://discord.domecode.com/), making good PRs on Github.
However, if you want to work on the internal development team, you need to finish [this application](https://forms.gle/9JrnkjHSwY3Vzb2a9t).

Thanks a lot!

