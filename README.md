[![TESTS](https://github.com/VirtualPatientEngine/demoMLsourceCode/actions/workflows/tests.yml/badge.svg)](https://github.com/VirtualPatientEngine/demoMLsourceCode/actions/workflows/tests.yml)
[![RELEASE](https://github.com/VirtualPatientEngine/demoMLsourceCode/actions/workflows/release.yml/badge.svg)](https://github.com/VirtualPatientEngine/demoMLsourceCode/actions/workflows/release.yml)

<h1 align="center" style="border-bottom: none;">🚀 Template to write source code for ML and data models</h1>

## How to use this repo?
1. Click on the `Use this template` button on the top-right of the page to create a copy of this repo.
2. Update the `setup` method in `setup.py`, and change the `package_name` in `release.config.js`.
3. Place your configs in `configs/*`, ML and data models in `app/*`, their corresponding tests in `tests/*`, and test notebooks in `experiment/*` (check out our Code/Dev/Data/MLOps guides for more information).
*Please note that all the protocols defined for Code/DevOps (e.g.: how to test your code locally, install pylint in VScode, define virtualenv, etc.) are also applicable to this template.*
4. Define the layout of your code documentaton website in `mkdocs.yml` and the web pages in `docs/*` in the markdown format (view the documentation of the example code used in the repo [here](https://virtualpatientengine.github.io/demoMLsourceCode))
5. Check out the layout below for more information.

```
├── .github                 <- Github Actions workflows
│
├── app/                    <- Source code
│   ├── data/                     <- Data scripts
│   ├── models/                   <- Model scripts
│   ├── utils/                    <- Utility scripts
|
├── configs/                <- Hydra configs (this is where you define
|                                               configurable parameters)
│   ├── data/                     <- Data configs for data modules
│   ├── model/                    <- Model configs for ML modules
│   ├── logger/                   <- Logger configs for MLflow
│   ├── trainer/                  <- Trainer configs for lightning's trainer
│   │
│   ├── config.yaml               <- Main config (see notebook in the experiment folder)
│
├── experiment/             <- Jupyter notebooks to demonstrate how to use Hydra
|                                (This is tailored for developers eager to fork your 
|                                 repo and test it out immediately. For those interested
|                                 in using your ML models and data modules as a package,
|                                 they can install the .whl file located in the dist/ folder
|                                 and proceed to write their own code for experimentation.)
│
├── tests/                  <- Tests of any kind
│
├── mkdocs.yml              <- File to describe the layout of the website
├── docs/                   <- Define individual pages of the website
├── setup.py                <- File for installing project (the app folder) as a package
├── .gitignore              <- List of files ignored by git
├── requirements.txt        <- File for installing python dependencies
├── package*                <- Files for mkdocs (do not modify)
├── node_modules/           <- Files for mkdocs (do not modify)
├── dist/                   <- Distribution (this is handles automatically via GitHub actions)
├── env/                    <- Environment
└── README.md
```

>NOTE: Contact Gurdeep for any assistance. Report errors or request features directly under `Issues` tab, or write comments in the MLOps guide shared on Teams.