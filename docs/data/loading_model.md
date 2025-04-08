# Adding New Models to the Repository

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

> ⚠️ Your model will **not be accepted** if either the XML or YAML file is missing.

---

## 🗂 Folder Structure Reference

Your files should be organized as follows:

```
vpeleaderboard/data/
├── models/
│   └── BIOMD000000064.xml
├── configs/
│   └── BIOMD000000064_url.yaml
```

- Both files must share the **same base name** (e.g., `BIOMD000000064`).
- The YAML filename must end with `.yaml`.

---

## How to Add a New Model

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

- Copy the XML model file into the `models/` directory.
- Copy the YAML config file into the `configs/` directory.

Make sure the files follow the naming conventions described above.

---

### 5. Commit and Push Your Changes

```bash
git add models/BIOMD000000064.xml configs/BIOMD000000064_url.yaml
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

