# Django Project at AppEngine
> This intends to be an [readme-documented][-0], [open-source-licensed][-1], [semantic-versioned][-2],
[conventional-committed][-3] and [changelogged][-4] git repository starting point
for the development of a brand-new [twelve-factor][-5] Django project

A straightforward beginning for an open-source Django project repository

[-0]: https://www.makeareadme.com/ "Make a README"
[-1]: https://choosealicense.com/licenses/ "Choose a License"
[-2]: https://semver.org/ "Semantic Versioning"
[-3]: https://www.conventionalcommits.org/en/v1.0.0/ "Conventional Commits"
[-4]: https://keepachangelog.com/en/1.0.0/ "Keep a Changelog"
[-5]: https://12factor.com/ "Twelve Factor"

Beside brings GAE's expected file system structure, generic-named powered-up Django project base
and useful Makefile targets to help development process, it also provides deploy-on-push automation 
through the use of Google's official [deploy-appengine][1] github action.

[1]: https://github.com/google-github-actions/deploy-appengine

### Table of Contents
<details>
  <summary>See all</summary>

  * [Getting started](#getting-started)
    * [Development environment](#development-environment)
    * [Repo publication](#repo-publication)
  * [Project specifications](#project-specifications)
    * [Features](#features)
    * [Folder structure](#folder-structure)
  * [Maintenance](#maintenance-)
  * [License](#license-)

</details>


## Getting started
First of all, [![create a new repository][B1]][!1] from this template, \
Name it accordingly and place where it best fits for your team.

[B1]: https://img.shields.io/static/v1?label=create%20a%20new%20repository&message=%20&style=social "Create new repository"
[!1]: https://github.com/generic-tree/sjango-project/generate "Github repository's template generation URL"

### Development environment
Make sure you have `Git`, `Make` and `Python` installed:
```shell
$ git --version
git version 2.25.1
$ make --version
GNU Make 4.2.1
$ python3 --version
Python 3.9.0+
```

Maybe you also want to [install Google Cloud SDK][2] to be able to manage your App Engine service via `gcloud` cli

Thus, clone the recent-created repository locally,
and set up its development environment:

```shell
$ make init
$ . venv/bin/activate
```

Finally, you are ready to create [your Django's first app][3]
and proceed developing your application.

[2]: https://cloud.google.com/sdk/docs/install
[3]: https://docs.djangoproject.com/en/dev/intro/tutorial01/

### Continuos deployment
Well, you need to have a *Google Cloud Project* configured.
So, through its console, enable the [App Engine Admin API][4]
and also set up a [Service Account][5] to your project,
registering its key into your fresh-repo [secrets][6]
as `GCP_SA_KEY`.

[4]: https://console.developers.google.com/apis/api/appengine.googleapis.com "Google Cloud Console: App Engine Admin API"
[5]: https://console.cloud.google.com/iam-admin/serviceaccounts "Google Cloud Console: Service Accounts"
[6]: https://docs.github.com/en/free-pro-team@latest/actions/reference/encrypted-secrets "GitHub Docs: Secrets"


### Repo publication
After all, you should make this project your own: \
Write a good README to present your project to the world. \
And also ensure to tailor the project license to your needs.


## Project specifications
Here some descriptions about this template project:

### Features
This project shortens a repository start setup, considering:
* Inclusion of mature README document, inspired by [Standard Readme][>1]
* Inclusion of open-source LICENSE file
* Inclusion of structured, yet raw, CHANGELOG file
* Compliance with widely-used version control conventions, such as:
    * [Semantic Versioning][-2]
    * [Conventional Commit][-3]
    * [Keep a Changelog][-4]

It also powers up development workflow by:
* Inclusion of proficient `Makefile` that improves development management
* Inclusion of appropriate `.gitignore` file

[>1]: https://github.com/RichardLitt/standard-readme/blob/master/spec.md "Standard readme specification"

### Folder structure
```
.
├── .git/                       Version control system folder
├── .github                     Github repo's configuration directory
│   └── workflows               Continuous integration settings
│       └── deploy.yml          Deploy-on-push automation descriptor
├── .gcloudignore               Ignored files manifest
├── .gitignore                  Ignored files manifest
├── app.yml                     App Engine service's settings
├── CHANGELOG.md                Release notes description
├── LICENSE                     License file
├── Makefile                    Development management facilities
├── README.md                   Readme document
├── requirements.txt            Python dependency list
└── src
    ├── __project__             Django project root folder
    └── manage.py               Django's command-line utility
```


## Maintenance [![][B2]][>2]
This project is maintained by the author, [@artu-hnrq](https://github.com/artu-hnrq). \
It has reached a stable, usable state and is being **actively developed**.

[B2]: https://www.repostatus.org/badges/latest/active.svg "Repostatus active badge"
[>2]: https://www.repostatus.org "Repo maintenance status"


## License [![][B3]][>3]
This project is published under the permissions established by [GNU General Public License v3.0][>3].

[B3]: https://img.shields.io/github/license/artu-hnrq/Django_GoogleAppEngine_Template?color=green "License badge"
[>3]: https://choosealicense.com/licenses/gpl-3.0/ "GPL 3.0 License description"
