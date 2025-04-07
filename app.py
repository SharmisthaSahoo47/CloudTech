# Sample Python code demonstrating file handling and basic operations

# Step 1: Write to a file
file_name = "sample.txt"

# Open a file for writing (creates the file if it doesn't exist)
with open(file_name, "w") as file:
    file.write("Hello, this is a sample Python script!\n")
    file.write("This file is being written using Python.\n")

print(f"Data has been written to {file_name}.")

# Step 2: Read from the file
try:
    with open(file_name, "r") as file:
        content = file.read()
        print("\nReading from file:")
        print(content)

except FileNotFoundError:
    print(f"Error: The file {file_name} does not exist.")

