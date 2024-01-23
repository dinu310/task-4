def read_from_file(filename):
    # Open the file in read mode
    with open(filename, "r") as f:
        # Read the content of the file
        content = f.read()

    # Display the content of the file
    print(content)

# Usage example
read_from_file("2024-01-23_dhtData.txt")
