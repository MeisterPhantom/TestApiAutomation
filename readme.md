# Project for API's automation

### 1 - Create o replicate virtual environment

To do that, its necessary have installed python in the local machine if you don't have it you can download in the following link

[Python Download Page](https://www.python.org/downloads/)

After installed python, open a command line or console terminal and following the next steps:

From console terminal

1 - Install pipenv library

**Note:** Validate if you have pip library install in your computer. If you don't have it, you can install in the following page [Pip official page](https://pypi.org/project/pip/)

```
pip install pipenv
```

2 - Clone or download the repository

3 - From root folder project, execute the following sentence
```
pipenv install
```
```
pipenv shell
```
**_This command recreate the virtual environment, be careful when the environment is created, you should see the path where the virtual environment was created_**

4 - For initiate the virtual environment.

```
source ./path/virtual/environment/bin/activate
```
note that the name of the virtual environment appears at the beginning of the command line. This indicates that you are already working with the virtual environment 
![img.png](img.png)

### 3 - Run Tests ###

1 - For execute the test, execute the follow command
```
robot -d results tests
```

### 4 - Test Plan File ###

You can consult the test plan in the following link: [Test Plan](./PLAN%20DE%20PRUEBAS%20-%20API.pdf)