# AgroHub
The project of Al Coders bin Shawarma for HackSamagam

## Creating a New Python Environment with Conda

### Step 1: Open a Terminal (Command Prompt for Windows)

Open your terminal or command prompt. You can usually find it in your operating system's applications or use the search feature.

### Step 2: Install Conda (If not installed)

If you don't have Conda installed, you can download and install it from the [official Conda website](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

### Step 3: Create a New Environment

```bash
# Replace 'myenv' with your desired environment name and 'python=3.8' with your desired Python version
conda create --name myenv python=3.8
```
### Step 4: Activate the Environment

```bash
conda activate myenv
```
### Step 5: Installing the Packages

```bash
conda install --file requirements.txt
```
### Step 6: Deactivate the Environment

```bash
conda deactivate
```
### Step 7: Remove the Environment (Optional)

```bash
conda env remove --name myenv
```
