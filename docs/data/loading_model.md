# How to load SBML models

This guide explains how to upload and contribute a new model to the repository. Please ensure that all required files are correctly named and placed in the appropriate directories before submitting.

---

## Required Files

To submit a model, **you must provide both of the following**:

- **XML Model File**

  Example: `BIOMD000000064.xml`  
  ➤ Place this in the `models/` directory.

- **YAML Configuration File**

  Example: `BIOMD000000064_url.yaml`  
  ➤ Place this in the `configs/` directory.

> ⚠️ Kindly ensure both files are present when submitting your model. Submissions with only one file will not be processed. Every XML model file must have a corresponding YAML configuration file with the same base name..

---

## Folder Structure Reference

Your files should be organized as follows:

```
vpeleaderboard/data/
├── models/
│   └── BIOMD000000064_url.xml
├── configs/
│   └── BIOMD000000064_url.yaml
```

 Please ensure that both the XML file and the corresponding YAML configuration file share the **same base name**

---

## How to add a new model

### 1. Fork the Repository

Click the **“Fork”** button in the top-right corner of the repository on GitHub to create a copy under your GitHub account.

---

### 2. Clone Your Fork Locally

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

---

### 3. Create a New Branch

```bash
git checkout -b add-new-model-BIOMD000000064
```

---

### 4. Add Your Files

- Put the XML model file into the models/ directory.

- Put the YAML configuration file into the configs/ directory.

Make sure both files follow the naming conventions described above and that a YAML file is provided for every XML model file.

---

### 5. Commit and Push Your Changes

```bash
git add models/BIOMD000000064_url.xml configs/BIOMD000000064_url.yaml
git commit -m "Add model BIOMD000000064"
git push origin add-new-model-BIOMD000000064
```

---

### 6. Open a Pull Request (PR)

1. Go to your fork on GitHub.
2. Click **"Compare & pull request"**.
3. Set the base branch to `main` of the original repository.
4. Provide a clear and concise title and description.
5. Click **"Create pull request"**.

[Virtual Patient Engine Docs](https://virtualpatientengine.github.io/AIAgents4Pharma/ops/DevOps/)


