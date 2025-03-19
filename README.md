# smart-store-caffery
A project designed for inventory management. The goal is to use Git for version control and document our workflow.

## Table of Contents
- [smart-store-caffery](#smart-store-caffery)
  - [Table of Contents](#table-of-contents)
  - [Project Setup](#project-setup)
  - [Git Workflow](#git-workflow)
  - [Key Files](#key-files)
  - [Using a Virtual Environment](#using-a-virtual-environment)
  - [Running Python Scripts](#running-python-scripts)
  - [Updating and Pushing Changes](#updating-and-pushing-changes)
  - [Final Notes](#final-notes)

## Project Setup
1. Clone the Repository
To get started, clone the repository from GitHub:

git clone https://github.com/ellacaffery/smart-store-caffery.git

Navigate into the project folder:
cd smart-store-caffery

1. Open Project in VS Code
    Open VS Code.
    Use File > Open Folder and select the project folder.
    Verify that key files such as README.md, .gitignore, and requirements.txt are present.

## Git Workflow
1. Checking the Current Branch
Before making changes, check your current branch:
git branch
Ensure you are on the main branch.

2. Pulling the Latest Changes
Always fetch the latest changes before making updates:
git pull origin main --rebase

3. Making Changes and Saving Files
Edit files as needed and save your work in VS Code (Ctrl + S or Cmd + S).

4. Staging and Committing Changes
After editing, add your changes to Git:
git add .
git commit -m "Descriptive commit message"

5. Pushing Changes to GitHub
Once committed, push updates to GitHub:
git push origin main

## Key Files
- README.md → Project documentation and workflow tracking.
- .gitignore → Specifies files to exclude from version control.
- requirements.txt → Lists Python packages required for the project.
- utils/logger.py → Contains logging utilities (to be added).
- scripts/data_prep.py → Data preparation script (to be added).

## Using a Virtual Environment
A virtual environment isolates dependencies for the project.

1. Create the Virtual Environment
python -m venv .venv

2. Activate the Virtual Environment
Windows (PowerShell)
.venv\Scripts\Activate

1. Install Dependencies
pip install -r requirements.txt

## Running Python Scripts
To execute the data_prep.py script:
py scripts\data_prep.py

## Updating and Pushing Changes
After making updates to your project or README file, follow these steps:

git add .
git commit -m "Update README with workflow and commands"
git push origin main

## Final Notes
- Always pull (git pull origin main --rebase) before pushing changes to avoid conflicts.
- Use descriptive commit messages to track progress.
- If you get merge conflicts, resolve them manually and commit again.