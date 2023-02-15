import subprocess

# run jshint on build/index.js
output = subprocess.run(['jshint', 'dist/problem-matcher.json'], capture_output=True)

# check the exit code to see if there were errors
if output.returncode == 0:
    print("Great news! No errors found in index.js")
else:
    print("Ops, errors exist and code is not running correct")
