# DomeCode Open Source

![domecode](https://user-images.githubusercontent.com/41021374/89816875-e9909280-db64-11ea-8b93-484239dfa8d7.png)
![GitHub](https://img.shields.io/github/license/the-domecode/domecode-opensource)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/the-domecode/domecode-opensource)
![GitHub issues](https://img.shields.io/github/issues-raw/the-domecode/domecode-opensource)
![GitHub pull requests](https://img.shields.io/github/issues-pr/the-domecode/domecode-opensource)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/the-domecode/domecode-opensource/django)

![Relative date](https://img.shields.io/date/1596609000?label=domecode%20)
![Website](https://img.shields.io/website?down_color=red&down_message=down%20for%20maintenance&label=domecode%20status&up_color=blue&up_message=online&url=https%3A%2F%2Fdomecode.com%2F)
![Discord](https://img.shields.io/discord/723603615582912512?color=black&logo=discord&logoColor=white)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/the-domecode/domecode-opensource)

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/C0C4226J0)

DomeCode open-source is the open-source codebase of DomeCode, a unified platform to learn code, practice, discuss, plan tasks, take notes, listen to music and more!

The AGPL license allows the free use of this code-base in other free open-source projects. However, the codebase is NOT free to use for paid projects. For paid projects, the use of this codebase would be paid as well.

## Setup

* Clone this repository. 
* Run the migrations.
* Run this on your localhost.


Use the`devmanage.py` command instead of `manage.py` command on development environments.
This project uses `decouple` so make sure to make a local `.env` file in your root directory of the project containing all the variables with dummy values.
The variables you should include are the ones with `config()` next to them in the `devmanage.py` file. If there's an error due to the missing value of an environment variable, it can be fixed with ease by passing in appropriate variables. It's pretty generic stuff. 

Once you're done with that, you can start working on fixing the nitty gritty details, make improvements, finding issues and reporting them in the issues tab of this repository. Create PRs and have fun!

## Code Style

* Flake8 is used.

* Make sure the code has docstrings unless of course the code is pretty generic and is self explainable. If you came up with a solution by yourself on some sort of problem, make sure to include comments and/or docstring(s).

* The static files root is the `notes` directory which is weird and I'm aware of it but since the inception of this platform, the root static directory has been situated there and it's alright. `notes` app was the first app on this, anyway.

Note : In the repo's language stats, HTML and CSS have been disabled intentionally.

## Contributors

* [Arth Tyagi](https://github.com/arthtyagi) - Project Maintainer and Founder of [DomeCode](https://github.com/arthtyagi)
* [Arhaan Ahmad](https://github.com/Arhaan)

## A few other projects you might wanna look out for

### Geddit

_Being used in DomeCode_

![code (2)](https://user-images.githubusercontent.com/41021374/86322013-c1ee0680-bc57-11ea-8152-ca67856d9df4.png)

Visit [here](https://github.com/arthtyagi/geddit/).

### Judge

_Being used in DomeCode_

![judge (1)](https://user-images.githubusercontent.com/41021374/88198064-eccce880-cc60-11ea-8356-c86f7caddac8.png)

![image](https://user-images.githubusercontent.com/41021374/88192318-0454a300-cc5a-11ea-9b2a-1baa9597b957.png)

Visit [here](https://github.com/arthtyagi/judge) which is also available as PyPi package [here](https://pypi.org/project/django-judge/).

Installable with : `pip install django-judge`
Thanks for visiting this pre-launch landing page!

#### Want to work on DomeCode?

If you want to be an outside collaborator with involvement in DomeCode at your own frequency, just make contributions in this repository.

However, if you want to be part of the DomeCode's new features development team ( we have a private repository for that ) and want to have any future benefits that MIGHT be tied to working on DomeCode in any form, apply at `iwantin@domecode.com` for the following positions :

* Full Stack Web Developer ( FrontEnd - React.js/Vue.js/Angular.js ( preferably React.js) ; Backend - Django/Flask(preferably Django) )
* Generalist Full Stack Developer ( include what technologies you know of inside the email )
* Front-End Developer ( React.js/Vue.js/Angular.js ( preferably React.js ) along with basic understanding of Python.
* Backend Developer ( Django/Flask ( preferably Django ) ; basic understanding of JS and a basic sense of aesthetics )
* Mobile Developer ( React Native/Flutter, Native Android/Native iOS ( preferably ReactNative for Android and iOS )
* ML Developer ( fluent in Python, familiar with TensorFlow )
