# GitHub Action-workflows: 

<img src="https://user-images.githubusercontent.com/31228460/218295872-1865b4ba-9c3c-4a28-bac8-0fd11c7c37f6.png" width="79%">

![GitHub Workflow Status (with branch)](https://img.shields.io/github/actions/workflow/status/jge162/Action-workflows/python_check.yml)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/jge162/Action-workflows)
[![Python Action](https://github.com/jge162/Action-workflows/actions/workflows/python_check.yml/badge.svg)](https://github.com/jge162/Action-workflows/actions/workflows/python_check.yml)
![GitHub package.json version](https://img.shields.io/github/package.json/v/jge162/Action-workflows)

# Purpose of this repo:
  
To create, simple to use GitHub actions on any repo for initial setup

# Example action to run a `python.py` file to verify no errors in code:

If errors in code exist they will be listed in the actions console. Also
you can run more than one file, seperated with commas...
   
# Up to you to decide on your triggers, I used `push` and `pull_request`
 
```yaml
name: Run Python file
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
```         
  
# Install required `dependencies.`

This way your can run, Python file.

```yaml  
jobs:
  build-and-analyze:
    runs-on: ubuntu-latest

    steps:
    - name: Python Action
      uses: jge162/Action-workflows@v1.0.1

    - run: |
        echo "Install required dependencies" 
        sudo apt-get update
        sudo apt-get install python3
```         
    
# Lastly use a for loop to run multipe instances.

This way you can run one or multple python scripts.

```yaml
     - run: |
        echo "Run, Build Application using scripts"
        python3 -c "
        scripts = ['./script.py', './script2.py'] 
        for script in scripts:
            with open(script, 'r') as file:
                exec(file.read())
        "
```  
       
# Issues and/or bugs, please create an issue to help me squash them!:

Please report [issues](https://github.com/jge162/Action-workflows/issues/new) here for discussion and resolution please.

# License info:
  
jge162/Action-workflows is licensed under the [GNU General Public License v3.0](https://github.com/jge162/Action-workflows/blob/main/LICENSE)
