## Action-workflows: 
    
[![Python Action](https://github.com/jge162/Action-Workflows/actions/workflows/python_check.yml/badge.svg)](https://github.com/jge162/Action-Workflows/actions/workflows/python_check.yml)
![GitHub](https://img.shields.io/github/license/jge162/Action-workflows)

<img src="https://user-images.githubusercontent.com/31228460/218295872-1865b4ba-9c3c-4a28-bac8-0fd11c7c37f6.png" width="79%">

## Purpose of this repository:

>[!IMPORTANT]\
>This is a template for copying simple-to-use GitHub actions, designed for the initial setup of any repository.

## Example action to run a `python.py` file to verify that no errors exist in your code:

>[!NOTE]\
>If errors exist within the code they'll be listed in the actions console.
>Also you can run more than one file, by separating them using commas.
   
## You decide on which triggers to use for `push` and `pull_request.`

>[!NOTE]\
>Also, a good trigger to use is also `workflow_dispacth`, to manually run the action.
 
```yaml
name: Run Python file
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build-and-analyze:
    runs-on: ubuntu-latest

    steps:
    - name: Python Action
      uses: jge162/Action-workflows@v2.1.0
      with:
          token: ${{ secrets.GITHUB_SECRET }}

    - run: |
        echo "Install required dependencies" 
        sudo apt-get update
        sudo apt-get install python3
```         
    
## Lastly use a `for` loop to run multiple instances of Python scripts.

>This way you can run one, or multiple python scripts.

```yaml
     - run: |
        echo "Run, Build Application using scripts"
        python3 -c "
        scripts = ['./script.py', './script2.py'] 
        for script in scripts:
            with open(script, 'r') as file:
                exec(file.read())
```

---

## Issues and/or bugs, Create one to Help me squash them!

>[!IMPORTANT]\
>Please report issues [here](https://github.com/jge162/Action-workflows/issues/new), for discussion and resolution.

## <u>License & Code of Conduct info:</u>
  
[Action-workflows](https://github.com/jge162/Action-workflows) is licensed under the [GNU General Public License v3.0](https://github.com/jge162/Action-workflows/blob/main/LICENSE).

## See also: [Code of Conduct](https://github.com/jge162/Action-workflows/blob/main/CODE_OF_CONDUCT.md).

>[!WARNING]\
>Designed with 💙 by [@jermyiah™](https://github.com/jge162)
