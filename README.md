## Action-workflows:    
 
![GitHub Workflow Status (with branch)](https://img.shields.io/github/actions/workflow/status/jge162/Action-workflows/python_check.yml)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/jge162/Action-workflows)
[![Python Action](https://github.com/jge162/Action-workflows/actions/workflows/python_check.yml/badge.svg)](https://github.com/jge162/Action-workflows/actions/workflows/python_check.yml)
![GitHub package.json version](https://img.shields.io/github/package-json/v/jge162/Action-workflows)
![GitHub](https://img.shields.io/github/license/jge162/Action-workflows?color=purple)
[![Contributors](https://img.shields.io/github/contributors/jge162/Action-workflows.svg)](https://github.com/jge162/Action-workflows/graphs/contributors) 
[![Forks](https://img.shields.io/github/forks/jge162/Action-workflows.svg)](https://github.com/jge162/Action-workflows/network/members)
[![Issues](https://img.shields.io/github/issues/jge162/Action-workflows.svg)](https://github.com/jge162/Action-workflows/issues) 
<img src="https://user-images.githubusercontent.com/31228460/218295872-1865b4ba-9c3c-4a28-bac8-0fd11c7c37f6.png" width="79%">

## Purpose of this repository:
  
This is template to copy simple-to-use GitHub actions, for the initial setup of any repository.
<hr>

## Example action to run a `python.py` file to verify that errors exist in the code:

If errors exist within the code they'll be listed in the actions console. 

Also
you can run more than one file, by separating them using commas.
   
## Up to you to decide on your triggers, I used `push` and `pull_request.`

Also, a good one to use is also `workflow_dispacth`, to manually run the action.
 
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
  
## Install required `dependencies.`

This way your can run python files.

```yaml  
jobs:
  build-and-analyze:
    runs-on: ubuntu-latest

    steps:
    - name: Python Action
      uses: jge162/Action-workflows@v1.1.1

    - run: |
        echo "Install required dependencies" 
        sudo apt-get update
        sudo apt-get install python3
```         
    
## Lastly use a `for` loop to run multiple instances.

This way you can run one, or multiple python scripts.

```yaml
     - run: |
        echo "Run, Build Application using scripts"
        python3 -c "
        scripts = ['./script.py', './script2.py'] 
        for script in scripts:
            with open(script, 'r') as file:
                exec(file.read())
```  
         
<hr>

## Issues and/or bugs, please create an issue to help me squash them!

Please report issues [here](https://github.com/jge162/Action-workflows/issues/new), for discussion and resolution.

## <u>License & Code of Conduct info:</u>
  
[jge162/Action-workflows](https://github.com/jge162/Action-workflows) is licensed under the [GNU General Public License v3.0](https://github.com/jge162/Action-workflows/blob/main/LICENSE). <br> <br>
See also: [Code of Conduct](https://github.com/jge162/Action-workflows/blob/main/CODE_OF_CONDUCT.md).
<br> <br>

<strong>Thank you for your interest in actions-worflows!</strong> :)
