# Setting Up and Running Your Python Script on Windows

This guide will help you set up and run a Python script from anywhere on your Windows system after cloning it from a GitHub repository.

## Prerequisites

- Ensure Python is installed on your system. You can check this by running `python --version` in Command Prompt.
- A cloned GitHub repository containing your Python script located in `C:\`.

## Steps to Set Up the Script

### 1. Locate Your Cloned Repository

Assuming you have cloned the repository directly into your `C:\` drive, navigate to:

Make sure your Python script (e.g., `file_organizer.py`) is located within this repository.

### 2. Move the Script to a Convenient Location

To run the script more easily, create a dedicated folder for your scripts. 

1. Open File Explorer and navigate to your user folder (`C:\Users\YourUsername`).
2. Right-click and select **New > Folder** and name it `scripts`.
3. Copy `file_organizer.py` from `C:\YourRepoName` and paste it into `C:\Users\YourUsername\scripts`.

### 3. Add the Scripts Directory to Your PATH

To run your script from anywhere in the Command Prompt, you need to add the `scripts` directory to your system PATH.

1. Right-click on **This PC** or **My Computer** and select **Properties**.
2. Click on **Advanced system settings** on the left sidebar.
3. In the System Properties window, click on the **Environment Variables** button.
4. Under the **System variables** section, find and select the `Path` variable, then click **Edit**.
5. Click **New** and add the path to your scripts directory:
6. Click **OK** to close all the dialog boxes.


### Steps to run
1. open cmd or powershell
2. move to the directory you want to declutter using cd DIRNAME:/
3. type `file_organizer` or  `file_organizer.bat`


