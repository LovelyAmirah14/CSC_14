# Assignement 10 Banton, Amirah
seperate = "--------------------------------------------------"

# 10-1 Learning Python
def read_file(file_path):
    """Read and print the contents of a file."""
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
file_path = 'learning_python.txt'
read_file(file_path)

print(seperate)

# 10-2 Learning C
file_path_c = 'learning_c.txt'
read_file(file_path_c)

print(seperate)

# 10-3 Simplier Code
def read_file_simplified(file_path):
    """Read and print the contents of a file, handling file not found."""
    try:
        with open(file_path, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
read_file_simplified('learning_python.txt')
read_file_simplified('learning_c.txt')
read_file_simplified('learning_ruby.txt')

print(seperate)

