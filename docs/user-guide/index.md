## Getting Started with VPELeaderboard

Welcome to **VPELeaderboard**, an open-source project developed by **Team VPE**. The primary objective of this project is to evaluate and benchmark the performance of advanced time series forecasting models when applied to simulated biological data. Unlike traditional methods that rely on handcrafted mathematical models, we focus on directly forecasting simulation results through AI-driven techniques. This leaderboard provides a comprehensive analysis of the strengths and limitations of these models, offering valuable insights into their effectiveness in predicting the dynamics of complex biological systems.

Our toolkit currently consists of the following components:

- **Data:** Explore integrated datasets, including ordinary differential equation models in SBML format.
- **Algorithms:** A collection of cutting-edge algorithms that have been developed to tackle time series forecasting and predictive modeling tasks.
- **Leaderboard:** An interactive leaderboard that evaluates and compares the performance of time series forecasting models, focusing on how well they predict the trajectories of simulated biological processes.

### How to Use VPELeaderboard

Follow the steps below to get started with VPELeaderboard:

#### 1. Clone the Repository

Clone the repository to your local machine:


    git clone https://github.com/your-username/VPELeaderboard.git


Ensure that you replace `your-username` with your actual GitHub username.


#### 2. Set Up the Environment
Ensure that your Python environment is properly set up:


    python -m venv vpe-env
    source vpe-env/bin/activate  # For macOS/Linux
    vpe-env\\Scripts\\activate     # For Windows


#### 3. Install Dependencies

Navigate to the project directory and install the required dependencies:


    pip install -r requirements.txt


### Contribute Your Models
To contribute new models to the leaderboard, please follow the instructions in the  [How to Load and Contribute SBML Models](docs/data/loading_model.md) section. This guide provides the necessary steps for preparing and submitting your models, ensuring they are automatically validated and integrated into the leaderboard system via our CI/CD pipeline.

### Explore Tutorials
We provide a range of tutorials to assist you in using the platform effectively. Visit the Tutorials section in Data page for comprehensive guides and examples.

### Benchmark Your Algorithm
With VPELeaderboard, you can benchmark the performance of your algorithm against others based on specific datasets and performance metrics.

