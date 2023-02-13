# GitHub Action-workflows:

<img src="https://user-images.githubusercontent.com/31228460/218295872-1865b4ba-9c3c-4a28-bac8-0fd11c7c37f6.png" width="79%">

![GitHub Workflow Status (with branch)](https://img.shields.io/github/actions/workflow/status/jge162/Action-workflows/python_check.yml?branch=main&style=for-the-badge)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/jge162/Action-workflows?logo=github&style=for-the-badge)
![GitHub Repo stars](https://img.shields.io/github/stars/jge162/Action-workflows?color=red&logo=github&style=for-the-badge)

# Purpose of this repo:

To create, simple to use GitHub actions on any repo for initial setup.

# Example action to run a `python.py` file to verify no errors in code:

If errors in code exist they will be listed in the actions console. Also
you can run more than one file, seperated with commas.

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
    - name: Checkout repository
      uses: actions/checkout@v3

    - run: |
        echo "Install required dependencies" 
        sudo apt-get update
        sudo apt-get install python3
    - run: |
        echo "Run, Build Application using scripts"
        python3 -c "
        scripts = ['./script.py', './script2.py'] 
        for script in scripts:
            with open(script, 'r') as file:
                exec(file.read())
        "
```

# Issues and/or bugs, please create an issue to help me squash them:

Please report [issues](https://github.com/jge162/Action-workflows/issues/new) here for discussion and resolution please.

# Additional custom GitHub Action I created. 

This action will create a new release after a Pull request is closed. But, conditions are `user == jge162 && PR label == create release` 
in order to run. See code example Below:

```yaml
name: Release on Pull Request Close

on:
  pull_request:
    types: [closed]

jobs:
  build-and-release:
    runs-on: ubuntu-latest
    if: github.event.pull_request.merged == true && contains(github.event.pull_request.labels.*.name, 'create release') && github.event.pull_request.user.login == 'jge162'
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      - name: Build and test code
        run: |
          # Build and test code here
      - name: Get latest tag
        run: |
          git fetch --tags
          echo "::set-output name=latest_tag::$(git describe --tags $(git rev-list --tags --max-count=1))"
        id: get_latest_tag
      - name: Bump patch version
        run: |
          semver=$(echo "${{ steps.get_latest_tag.outputs.latest_tag }}")
          major=$(echo $semver | cut -d'.' -f1)
          minor=$(echo $semver | cut -d'.' -f2)
          patch=$(echo $semver | cut -d'.' -f3)
          new_patch=$((patch+1))
          new_tag="$major.$minor.$new_patch"
          echo "::set-output name=new_tag::$new_tag"
        id: bump_version
      - name: Create release
        uses: softprops/action-gh-release@v1
        with:
          files: |
            build/*
          tag_name: ${{ steps.bump_version.outputs.new_tag }}
          body: |
            This is the release notes for ${{ steps.bump_version.outputs.new_tag }}
        env:
          GITHUB_TOKEN: ${{ secrets.WORKFLOW_SECRET }}
```

# License info:

jge162/Action-workflows is licensed under the [GNU General Public License v3.0.](https://github.com/jge162/Action-workflows/blob/main/LICENSE)
