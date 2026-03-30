# Jenkins Automation Guide for Student Registration Form

This guide covers how to automate the automated execution of the Selenium tests you just built using Jenkins.

## Prerequisites
1. **Python 3.x** must be installed on your system.
2. **Google Chrome** browser must be installed.
3. **Jenkins** must be installed and running on your local machine (typically on `http://localhost:8080`).

## Step 1: Install Jenkins on Windows
If you haven't installed Jenkins yet:
1. Download the Windows installer from the [Jenkins Official Website](https://www.jenkins.io/download/).
2. Run the installer and follow the setup wizard.
3. Once running, it will open `http://localhost:8080` in your browser.
4. Unlock Jenkins using the password located in `C:\Program Files\Jenkins\secrets\initialAdminPassword`.
5. Install the "Suggested Plugins" and create your first Admin user.

## Step 2: Create a Simple Jenkins Job
1. Open your Jenkins Dashboard at `http://localhost:8080/`.
2. Click on **"New Item"** in the left menu.
3. Enter a name for the job (e.g., `Student-Registration-Selenium-Tests`).
4. Select **"Freestyle project"** and click **"OK"**.

## Step 3: Connect the Project Folder
In the configuration screen of your new job:
1. Since we are testing locally without a Git repository for now, scroll down to the **"Build Environment"** or jump straight to the **"Build Steps"**.
2. Jenkins allows you to define a **Custom Workspace** to point to your existing folder. 
   - Click "**Advanced...**" near the top right of the "General" tab.
   - Check the box for "**Use custom workspace**".
   - Enter the Directory path: `C:\Users\kanis\OneDrive\Desktop\p1`

*(Alternative: You can push your code to a GitHub repository, go to "Source Code Management" in Jenkins, select "Git", and paste the repository URL).*

## Step 4: Configure the Job to Run Selenium Test Scripts
1. Scroll down to the **"Build Steps"** section.
2. Click **"Add build step"** and select **"Execute Windows batch command"**.
3. In the command box, enter the following script to install Python dependencies and run the tests:

```bat
@echo off
echo "Installing Python Requirements..."
pip install -r requirements.txt

echo "Running Selenium Test Suite..."
python test_form.py
```

4. Click **"Save"** at the bottom of the page.

## Step 5: Execute the Job and Observe Builds
1. On the job's main page, click **"Build Now"** on the left-hand menu.
2. A new build item (e.g., `#1`) will appear in the **Build History** on the bottom left.
3. Click on the build number (`#1`) and then click **"Console Output"**.
4. You will see the live output from your batch command executing the `python test_form.py` script. 
5. The Chrome browser window will briefly open and perform the UI interactions during the test execution.
6. The job will be marked as **SUCCESS** (blue/green ball) if all tests pass, or **FAILED** (red ball) if any assertion in the tests fails.
