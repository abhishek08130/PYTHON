# Q2. Write a python program to copy data from txt one file to another txt file.

# Program to copy data from one file to another
sources = input("Enter source file name: ")
targets = input("Enter target file name: ")

try:

    with open(sources, 'r') as source:
        with open(targets, 'w') as target:
            target.write(source.read())
    print("File copied successfully!")
except FileNotFoundError:
    print("Source file not found!")
except Exception as e:
    print(f"An error occurred: {e}")
