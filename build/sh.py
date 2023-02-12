# Define the name of the project
PROJECT_NAME = "GitHub-Actions-workflows"

# Define the list of files to be included in the project
FILES = ["scripts.py"]

# Compile the files
def compile_files():
    # Write your code here to compile the files
    print(f"Compiling {FILES} into {PROJECT_NAME}.out")

# Run the simulation
def run_simulation():
    # Write your code here to run the simulation
    print(f"Running simulation for {PROJECT_NAME}.out")

# Main function to run the program
def main():
    compile_files()
    run_simulation()

print("success running script")

# Run the main function
if __name__ == "__main__":
    main()
