# Define the name of the project
PROJECT_NAME = "GitHub-Actions-workflows"

# Define the list of files to be included in the project
FILES = ["script.py"]

# Import the script.py file
import ./script.py

# Compile the files
def compile_files():
    # Call the compile_files function in script.py
    script.compile_files()

# Run the simulation
def run_simulation():
    # Call the run_simulation function in script.py
    script.run_simulation()

# Main function to run the program
def main():
    compile_files()
    run_simulation()

print("success running script")

# Run the main function
if __name__ == "__main__":
    main()
