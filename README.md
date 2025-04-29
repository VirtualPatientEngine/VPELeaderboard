# **THIS REPOSITORY IS A WORK IN PROGRESS!**
# VPELeaderboard

![Test Status](https://img.shields.io/badge/TESTS%20VPE%20Leaderboard-passing-brightgreen)
![Release](https://img.shields.io/badge/release-v1.0.0-blue)
![Python Version](https://img.shields.io/badge/python-%3E%3D%203.12-blue)

## Introduction

Welcome to **VPELeaderboard**, an open-source project developed by **Team VPE**. The primary objective of this project is to evaluate and benchmark the performance of advanced time series forecasting models when applied to simulated biological data. Unlike traditional methods that rely on handcrafted mathematical models, we focus on directly forecasting simulation results through AI-driven techniques. This leaderboard provides a comprehensive analysis of the strengths and limitations of these models, offering valuable insights into their effectiveness in predicting the dynamics of complex biological systems.

We invite you to explore the repository and gain a clear understanding of the models being tested and their performance metrics.

Our toolkit currently consists of the following components:

- **Data:** Explore integrated datasets, including ordinary differential equation models in SBML format.
- **Algorithms:** A collection of cutting-edge algorithms that have been developed to tackle time series forecasting and predictive modeling tasks.
- **Leaderboard:** An interactive leaderboard that evaluates and compares the performance of time series forecasting models, focusing on how well they predict the trajectories of simulated biological processes.

---

![alt text](docs/images/image.png)

## Table of Contents

- [Get Started](#get-started)
- [How to Add Your Models](#how-to-add-your-models)
- [Contributing](#contributing)

---

## Get Started

![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FVirtualPatientEngine%2FAIAgents4Pharma%2Frefs%2Fheads%2Fmain%2Fpyproject.toml)

Kickstart your journey with **VPELeaderboard** by using git and following an easy step-by-step guide for effortless setup.

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/VirtualPatientEngine/VPELeaderboard.git
    cd AIAgents4Pharma
    ```

2. **Set Up the Environment**

    Ensure that your Python environment is properly set up:

    ```bash
    python -m venv vpe-env
    source vpe-env/bin/activate  # For macOS/Linux
    vpe-env\\Scripts\\activate     # For Windows
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## How To Add Your Models

To contribute new models to the leaderboard, please follow the instructions in the  [How to Load and Contribute SBML Models](docs/data/loading_model.md) section. This guide provides the necessary steps for preparing and submitting your models, ensuring they are automatically validated and integrated into the leaderboard system via our CI/CD pipeline.

## Contributing

We greatly appreciate your interest in contributing to VPELeaderboard. To get started, please follow the steps below:

1. **Fork the repository** to create a personal copy of the project.
2. **Create a new branch** for your feature  or bug fix (`git checkout -b feat/feature-name`)
3. **Implement the necessary changes** for your contribution.
3. **Commit your changes** with a clear and concise message (`git commit -m 'feat: Add new feature'`)
4. **Push your changes** to your forked repository  (`git push origin feat/feature-name`)
5. **Open a pull request** and engage with us via the Discussions tab to facilitate review.

   _Note: Please note: We welcome all types of contributions, not limited to programming. You are encouraged to submit bug reports, propose new features, or participate as a beta tester. We highly value your input and support._

Please stay tuned for more information.

> NOTE: Contact Gurdeep for any assistance. Report errors or request features directly under `Issues` tab.   
