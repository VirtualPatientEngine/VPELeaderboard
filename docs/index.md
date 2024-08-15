# Index
### A template to write source for your ML and data models

#### 1. [Introduction](index.md)
This repository serves as a template for writing source code for your machine learning (ML) and dataset models. It is built on top of powerful templates:<br>

- [**Hydra:**](https://hydra.cc/docs/intro/) an open-source Python framework that allows you to specify all configurable parameters in one place without modifying the code. Please checkout the jupyter notebook in the the folder [experiment](https://github.com/VirtualPatientEngine/demoMLsourceCode/tree/main/experiment) to understand how Hydra works.

- [**Lightning:**](https://lightning.ai/docs/pytorch/stable/) a PyTorch deep learning framework that eliminates boilerplate code.
    We will mostly use the following 2 modules from the lightning package to build ML and data models.

    A ```LightningModule``` organizes your PyTorch code into 6 sections:<br>
        
        - Initialization (__init__ and setup())
        - Train Loop (training_step())
        - Validation Loop (validation_step())
        - Test Loop (test_step())
        - Prediction Loop (predict_step())
        - Optimizers and LR Schedulers (configure_optimizers())

    A ```datamodule``` encapsulates the five steps involved in data processing in PyTorch:<br>

        - Download / tokenize / process
        - Clean and (maybe) save to disk
        - Load inside Dataset
        - Apply transforms (rotate, tokenize, etc…)
        - Wrap inside a DataLoader

    For example purposes, this repository contains code to build Multilayer Perceptron (MLP) and Graph Convolutional Network (GCN) models tailored for node classification tasks using ```LightningModule```. Additionally, this repo contains code to build the CORA and MNIST data models using ```datamodule```.

##### How to use this repo?
1. Click on the `Use this template` button on the top-right of the [GitHub page](https://github.com/VirtualPatientEngine/demoMLsourceCode/tree/main) to create a copy of this repo.
2. Update the `setup` method in `setup.py`, and change the `package_name` in `release.config.js`.
3. Place your configs in `configs/*`, ML and data models in `app/*`, their corresponding tests in `tests/*`, and test notebooks in `experiment/*` (check out our *Code/Dev/Data/MLOps guides* for more information how to test your code locally, install pylint in VScode, define virtualenv, etc.).
4. Define the layout of your code documentaton website in `mkdocs.yml` and the web pages in `docs/*` in the markdown format.
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

The documentation provided in the next sections guide you the through the implementation of the code.

#### 2. [MLP model](mlp.md)
#### 3. [GCN model](gcn.md)
#### 4. [CORA datamodule](cora.md)
#### 5. [MNIST datamodule](mnist.md)
#### 6. [Testing Documentation](tests.md)

>NOTE: Contact Gurdeep for any assistance. Report errors or request features directly under `Issues` tab, or write comments in the MLOps guide shared on Teams.