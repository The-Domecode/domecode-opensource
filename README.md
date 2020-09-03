<h1 align="center"><img src="https://user-images.githubusercontent.com/41021374/92151521-e70d1a00-ee3e-11ea-8b2c-33f02cb67411.png" alt="DomeCode" height=200 width=200 align="middle"> DomeCode</h1>
<p align="center">
  <a href="https://discord.gg/ZwTJPNB"><img src="https://badgen.net/badge/discord/join%20chat/7289DA?icon=discord" alt="Discord Server"/></a>
<a><img src="https://img.shields.io/github/license/the-domecode/domecode-opensource"/></a>
<a><img src="https://img.shields.io/date/1596609000?label=domecode%20"/></a>
<a><img src="https://img.shields.io/github/license/the-domecode/domecode-opensource"/></a>
<a><img src="https://img.shields.io/github/issues-raw/the-domecode/domecode-opensource"/></a>
<a><img src="https://img.shields.io/github/issues-pr/the-domecode/domecode-opensource"/></a>
<a><img src="https://img.shields.io/website?down_color=red&down_message=down%20for%20maintenance&label=domecode%20status&up_color=blue&up_message=online&url=https%3A%2F%2Fdomecode.com%2F"/></a>
<a><img src="https://img.shields.io/github/commit-activity/m/the-domecode/domecode-opensource"/></a>
<a href="https://ko-fi.com/C0C4226J0"><img src="https://www.ko-fi.com/img/githubbutton_sm.svg"/></a>

</p>

## What is DomeCode?🤔

[DomeCode](https://domecode.com) is a coding platform that unifies the coding experience by providing all relevant resources and tools in a single platform.
On DomeCode, you can practice in six languages including Rust, C, C++, Go, Java and Python. Learn, take notes, discuss stuff on the forum, connect with other developers, collaborate on projects with them, be a part of a developer community and way more!

This repository is the open-source codebase of [DomeCode](https://domecode.com/), a unified platform to learn code, practice, discuss, plan tasks, take notes, listen to music and more!

**The AGPL license allows the free use of this code-base in other free open-source projects.
However, the codebase is NOT free to use for paid projects. For paid projects, the use of this codebase would be paid as well.**

If anyone wants to share their experience using [DomeCode](https://domecode.com/), you can share it with me personally on Discord(zuck#9454) or send me an email at [`founder@domecode.com`](mailto:founder@domecode.com) 📧 .

P.S This repository is the open-source codebase of DomeCode. The proprietary codebase of DomeCode is accessible to those in the internal development team only.

## What do you get with [DomeCode](https://domecode.com/)?

- 🏃‍♂️ Challenges to test your skills;

- 📖 Tutorials to guide programmers of all skill levels;

- 🧵 Forums to discuss the challenges or anything else programming-related;

- 🗓 Planning tools to take notes 📝 and plan tasks 🗒️ right from where you learn to code/practice code;

- 📌 Creator feature to allow you to create listings of your product/project containing all essential information in the form of a shareable link so that no information is left out about your project;

- 🎶 Lo-Fi Music to program by;

- ⚛ Fusion, a disposable code editor with tutorials and preview within it for those getting started with front-end!

<a align="center">This is what the disposable code editor feature looks like<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--ypRb9rHp--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/74wiej88s3gpupdr55lu.png"/></a>

## Why DomeCode?🤗

- You don’t need to navigate to dozens of platforms anymore, DomeCode organizes all the tools and resources for you 📚 .
- You can finally focus more on programming instead of finding the “right” website for every small thing ☺️ .
- You get to collaborate with developers around you 🖇️ .
- DomeCode provides its users with a significant productivity boost ⚡ .
- Save around 30% of your overall time ⌛ spent in the process of learning a programming concept, taking notes, and practicing it.
- You simply get more without any hassle 😊 .

Join our community 💬 on [Discord!](https://discord.gg/ZwTJPNB).

## 🧰 Tools in DomeCode

At the time of this writing on 4th September, 2020, 
DomeCode offers the user an array of future that make DomeCode truly a unified platform.

- ➔ Growth Tools

Tracks, Practice, Quizzes, Fusion, **Help!, Certificate Programs**

- ➔ Planning Tools 

Notes, Creator, Tasks

- ➔ Miscellaneous Tools

Music, Forum, Leaderboard, **1v1 challenges**

- ➔ Social Tools

**Messaging, User Finder, Bored!**

Unreleased features are **highlighted**.

## 📆 Milestones so far

- Launched the alpha version on **5th August, 2020**.
- **15000+** web traffic requests within 24 hours of the alpha release.
- **275+** registered users as of 2nd September, 2020.
- Bounce Rate **optimal** according to Google Analytics.
- Total number of users over the past 4 weeks ( both registered and unregistered ) sum up to **2, 400+** according to Google Analytics.
- More than **2** sessions on average per user where the users include unregistered users as well.
- **Upcoming** - Stable Release in October.
- **Upcoming** - An exclusive blog. Apply to become a DomeCode blogger **[here](https://forms.gle/8Q6gQYBJxsKYgxMP7)**.

## Setup

- Clone your fork of this repository.
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

Note : In the repo's language stats, HTML and CSS have been disabled intentionally.

## 🧑 Contributors

- [Arth Tyagi](https://github.com/arthtyagi) - Founder, CEO, Full Stack Developer, [DomeCode](https://domecode.com/)
- [Arhaan Ahmad](https://github.com/Arhaan) - Back-end developer, [DomeCode](https://domecode.com/).

## 💼 Work on DomeCode

If you want to be an outside collaborator with involvement in DomeCode at your own frequency, just make contributions in this repository.

However, if you want to be part of the DomeCode's new features development team ( we have a private repository for that ) and want to have any future benefits that MIGHT be tied to working on DomeCode in any form, apply at `iwantin@domecode.com` for the following positions :

- Full Stack Web Developer ( FrontEnd - React.js/Vue.js/Angular.js ( preferably React.js) ; Backend - Django/Flask(preferably Django) )
- Generalist Full Stack Developer ( include what technologies you know of inside the email )
- Front-End Developer ( React.js/Vue.js/Angular.js ( preferably React.js ) along with basic understanding of Python.
- Backend Developer ( Django/Flask ( preferably Django ) ; basic understanding of JS and a basic sense of aesthetics )
- Mobile Developer ( React Native/Flutter, Native Android/Native iOS ( preferably ReactNative for Android and iOS )
- ML Developer ( fluent in Python, familiar with TensorFlow )

**OR**

Apply using [this](https://forms.gle/Y4Cza1i3yxdsWRvo7).

## A few other projects you might wanna look out for

### Geddit

_Being used in DomeCode_

![code (2)](https://user-images.githubusercontent.com/41021374/86322013-c1ee0680-bc57-11ea-8152-ca67856d9df4.png)

Visit [here](https://github.com/arthtyagi/geddit/).

### Judge

![judge (1)](https://user-images.githubusercontent.com/41021374/88198064-eccce880-cc60-11ea-8356-c86f7caddac8.png)

![image](https://user-images.githubusercontent.com/41021374/88192318-0454a300-cc5a-11ea-9b2a-1baa9597b957.png)

Visit [here](https://github.com/arthtyagi/judge) which is also available as PyPi package [here](https://pypi.org/project/django-judge/).

Installable with : `pip install django-judge`
Thanks for visiting this!
