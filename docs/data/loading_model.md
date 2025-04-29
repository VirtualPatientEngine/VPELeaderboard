# How to Load and Contribute SBML Models

This guide outlines the correct procedure for contributing SBML models to the Virtual Patient Leaderboard repository. By following these instructions, your models will be automatically validated, processed, and integrated into the leaderboard system via CI/CD.

---

## Required Files

To submit a model, **you must provide both of the following**:

<!-- - **XML Model File**

  Example: `your_model.xml`  
  ➤ Place this in the `models/` directory.

- **YAML Configuration File**

  Example: `your_model.yaml`  
  ➤ Place this in the `configs/` directory.  -->

| File Type | Naming Example | Target Directory |
|-----------|----------------|------------------|
| SBML Model File | `your_model.xml` | `vpeleaderboard/data/models/` |
| YAML Configuration File | `your_model.yaml` | `vpeleaderboard/data/configs/` |


> ⚠️ Kindly ensure both files are present when submitting your model. Submissions with only one file will not be processed. Every XML model file must have a corresponding YAML configuration file with the same base name.

---

## Folder Structure Reference

Ensure your file placement adheres to this structure:

```
vpeleaderboard/data/
├── models/
│   └── your_model.xml
|   └── BIOMD0000000537_url.xml
├── configs/
│   └── your_model.yaml
|   └── BIOMD0000000537_url.yaml
```

 Please ensure that both the XML file and the corresponding YAML configuration file share the **same base name**.
 Submissions that do not follow this structure will fail the automated GitHub Actions validation.

---

## How to add a new model

### 1. Fork the Repository

Navigate to the [repository](https://github.com/VirtualPatientEngine/VPELeaderboard) and click the **“Fork”** button in the top-right corner of the repository on GitHub to create a copy under your GitHub account.

---

### 2. Clone Your Fork Locally

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

---

### 3. Create a New Branch

Ensure you use a descriptive branch name that clearly reflects the purpose of your changes:

```bash
git checkout -b add-new-your_model
```
This helps maintain clarity and consistency across the project, making it easier to track changes and collaborate effectively.

---

### 4. Add Your Files

#### YAML Configuration Parameters

Each SBML model must be accompanied by a .yaml configuration file that defines the simulation durations. These parameters control how long the model runs for training, validation, and testing phases during automated processing.

Your `.yaml` file must include the following fields:

| Key               | Type   | Description                                                                                                                                                   |
|-------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `train_duration`  | `int`  | Defines the **duration** (in simulation time units) allocated for the **training phase** of the model. This value should match the scale of the model's dataset. |
| `val_duration`    | `int`  | Defines the **duration** (in simulation time units) allocated for the **validation phase**.                                             |
| `test_duration`   | `int`  | Defines the **duration** (in simulation time units) allocated for the **testing phase**. Should align with testing scenarios in the model’s intended use.       |


Example Configuration

```bash
train_duration: 6
val_duration: 3
test_duration: 5
```

- Put the XML model file into the models/ directory.

- Put the YAML configuration file into the configs/ directory.

> ⚠️ Make sure both files follow the naming conventions described above and that a YAML file is provided for every XML model file.

---

### 5. Commit and Push Your Changes

```bash
git add models/your_model.xml configs/your_model.yaml
git commit -m "Add model your_model with configuration"
git push origin add-new-model-your_model
```

---

### 6. Open a Pull Request (PR)

1. Go to your fork on GitHub.
2. Click **"Compare & pull request"**.
3. Set the base branch to `main` of the original repository.
4. Provide a clear and concise title and description.
5. Click **"Create pull request"**.

[Virtual Patient Engine Docs](https://virtualpatientengine.github.io/AIAgents4Pharma/ops/DevOps/)



