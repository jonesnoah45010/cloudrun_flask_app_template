# Template For Building a Cloud Run App using Flask

- Before we get into the template code itself, there are few steps needed to get yourself set up in google cloud to make deploying the code possible.  
- If you wish to jump directly into running the app locally without worrying about cloud deployment, then skip to the **Template Code** section.





## Setting up Google Cloud Console Project and Installing gcloud CLI

- This section will walk you through the process of creating a new project in the Google Cloud Console and installing the `gcloud` command-line interface (CLI) tools on macOS, Windows, or Linux.

### Step 1: Create a Google Cloud Project

1.  **Sign in to Google Cloud Console:** Go to the Google Cloud Console and sign in with your Google account.
2.  **Create a new project:** Click on the project dropdown at the top of the page next to "Google Cloud Platform". Then click on "New Project".
3.  **Configure your project:**
    -   **Name your project:** Enter a project name in the "Project Name" field.
    -   **Select a billing account:** Choose a billing account to associate with the project. If you do not have a billing account, you will need to create one.
    -   **Choose a location:** (Optional) You can specify an organization or leave it as "No organization".
4.  **Create the project:** Click on "Create" to create your new project.
5.  **Select the project:** After creation, select your newly created project from the project dropdown menu.

### Step 2: Install the gcloud CLI

#### macOS and Linux

1.  **Open a terminal window.**
2.  **Download and run the installation script:**
    
    - `curl https://sdk.cloud.google.com | bash` 
    
3.  **Restart your shell:**
    
    - `exec -l $SHELL` 
    
4.  **Initialize the `gcloud` CLI:**
 
    - `gcloud init` 
    

#### Windows

1.  **Download the installer:**
    -   Visit the Google Cloud SDK page and download the Cloud SDK installer for Windows.
2.  **Run the installer:**
    -   Run the downloaded installer and follow the prompts. The installer includes the `gcloud` CLI, `gsutil`, and `bq` command-line tools.
3.  **Initialize `gcloud` CLI:**
    -   After installation, open a Command Prompt or PowerShell window and run:
        
        - `gcloud init` 
        

#### For All Platforms

During the `gcloud init` process, you will be prompted to:

-   Log in with your Google account.
-   Select a Cloud project to use as your default.
-   Choose a default compute region and zone.

### Verify Installation

- To verify that `gcloud` has been installed correctly, run:

- `gcloud version` 

- You should see the version of `gcloud` and other installed components.

### Next Steps

- Now that you have set up your Google Cloud project and installed the `gcloud` CLI, you can start using Google Cloud resources and services. 


## Template Code

### Prerequisites

-   Python 3 installed on your system. You can download Python from the official website.
-  This project assumes you will be using python3.11 but should work for any version >3.6
- GitHub CLI installed on your system. You can download GitHub CLI from the official website

### Step 1:  Create a Python Virtual Environment.

#### macOS and Linux

#### 1. Open a Terminal

-   macOS: Open the Terminal app from Applications > Utilities.
-   Linux: Open your terminal emulator from your applications menu or using a keyboard shortcut.

#### 2. Update pip (Optional)

- It's a good practice to make sure you're using the latest version of pip:

- `python3 -m pip install --upgrade pip` 

#### 3. Create a Virtual Environment

- Navigate to your project directory:

- `cd /path/to/your-project` 

Create a virtual environment named `my_venv` (you can use any name):

- `python3 -m venv my_venv` 

#### 4. Activate the Virtual Environment

- `source my_venv/bin/activate` 

- Your command prompt will change to indicate that you are now operating within the virtual environment. It will look something like `(my_venv) username@hostname:~/path/to/your-project$`.

#### 5. Deactivate the Virtual Environment

- When you are done working in the virtual environment, you can deactivate it:

- `deactivate` 

#### Windows

#### 1. Open Command Prompt or PowerShell

- Search for `cmd` or `PowerShell` in the Start menu and open it.

#### 2. Update pip (Optional)

- Ensure your version of pip is up-to-date:

- `pip install --upgrade pip` 

#### 3. Create a Virtual Environment

- Navigate to your project directory:

- `cd \path\to\your-project` 

Create a virtual environment named `my_venv`:

- `python -m venv my_venv` 

#### 4. Activate the Virtual Environment

- `.\my_venv\Scripts\activate` 

- Your command prompt will change to show that you are now working within the virtual environment. It will look something like `(my_venv) C:\path\to\your-project>`.

#### 5. Deactivate the Virtual Environment

- To exit the virtual environment, use:

- `deactivate`


### Step 2:  Running the Code Locally

- Now that you have activated a virtual environment, you can clone the code into your desired working directory.  

#### 1. Get the code:

- Run the following command in your desired working directory

- `git clone REPO_LINK_HERE`

#### 2. Install Python Libraries Using Pip:
- You will need to install the python modules used by this app before running it. You will only need to do this once for this virtual environment. If you want to run this app in a new virtual environment, you will need to do this again.
- Run the command below...
- `pip install -r requirements.txt`
- *Note: If you end up adding your own custom code to this app, make sure to include the name of any new libraries you ended up pip installing to the requirements.txt file.  This makes sharing the app with others easier, as they will just need to install requirements.txt on their end and the app will run without issue.*

#### 3. Run the Flask app:
- Navigate into the cloudrun_flask_app_template directory that you just cloned
- Execute the command below...
- `python3 main.py` for macOS/Linux users
- `python main.py` for Windows users
- Copy the local url that appears in your terminal and past it into your desired web browser.


#### Step 3:  Editing the Code:
- You can now start making the project your own. 

- Project Contents:
-- **`static` folder**: A directory that contains all elements of the web application that are "static", i.e. don't change.  This includes things like images, JavaScript code and CSS code.
-- **`static/css` folder**: A directory that contains various CSS code to control the styling of your HTML pages.
-- **`static/css/form.cs` file**: A file containing CSS code to control the styling for the templates/form.html page.
-- **`static/css/index.cs` file**: A file containing CSS code to control the styling for the templates/index.html page.
-- **`static/images` folder**: A directory that contains image files that you would like for your HTML pages to be able to render.
--  **`static/images/cute_frog.png` file**: sample image file rendered in as an example in the templates/index.html page
-- **`static/js` folder**: A directory containing all the JavaScript files that control the dynamic actions taking place in your HTML pages.
-- **`static/js/form.js` file**: A file containing JavaScript that is used in the templates/index.html page.
-- **`templates` folder**: A directory containing all of the HTML files representing the various pages of your app.
--  **`templates/form.html` file**: A file containing HTML code for rendering an example page showcasing how to use an HTML form and JavaScript to submit data to an endpoint in the Flask app's main script and then display the response from the endpoint on screen.
-- **`template/index.html` file**: A file containing HTML code for rendering an example of a landing page with an image and a button leading to another page, in this case the form.html page.
-- **`tmp` folder**: A directory used for doing file uploads and storing temporary files.  This folder must use this naming convention, as google cloud run uses this convention.  If you change the name of this folder, your app will still run locally but will not work in cloud run properly.
-- **`deploy.bat` file**: A script that can be executed to deploy this Flask app as a google cloud run application on Windows
-- **`deploy.sh` file**: A script that can be executed to deploy this Flask app as a google cloud run application on macOS or Linux
-- **`Dockerfile` file** : A file used by Docker, a containerization platform, to containerize and initialize the Flask app as part of the deployment process.  In this basic form, it just initializes the app directory structure and installs all of the necessary libraries for the app to run before it is deployed. 
-- **`main.py` file**:  This is the primary executable file and holds all of the Flask endpoints, which control how the back end works and interacts with the front end.  Controls which HTML pages can be rendered.  **It is the most important file in the project.** 
-- **`README.md` file**:  This is the file you are reading right now.  It is the markdown formatted description of the application.  Once you make this code your own, you can change this document to be an explanation of what your application does and how to use it, or go into detail about how the code works if you want it to be collaborative.
-- **`requirements.txt` file**: A file containing a list of all of the python libraries that this application uses to run properly. 



### Step 3:  Deploying to Google Cloud Run

- This is not very difficult if you have your google cloud console account and project set up already.  If not, go back to the **Setting up Google Cloud Console Project and Installing gcloud CLI** section.

#### 1. Edit the deploy script:
- In your preferred code editor, open `deploy.sh` for macOS/Linux users or `deploy.bat` for Windows users and then edit the `SERVICE_NAME`,`PROJECT_NAME`,`REGION` variables at the top of the script. You should update these to match the features of your google cloud console project.  `SERVICE_NAME` can be whatever label you want to give to your application. `PROJECT_NAME` needs to be the actual project_id of the project you created in google cloud console. `REGION` needs to be the actual region that your set up the `PROJECT_NAME` under, often it defaults to us-east1 if you are not sure.
#### 2. Run the deploy script:
- After editing the deploy script, all you need to do is execute it.  On macOS/Linux you can enter `sh deploy.sh` in your command line. On Windows you can just double click on the deploy.bat file in your file explorer or just type in the filename and press enter in Command Prompt.
