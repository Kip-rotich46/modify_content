def modify_content(content):
    """Modify the content as needed (e.g., convert to uppercase)."""
    return content.upper()

# Prompt user for filename
filename = input("Enter the filename to read: ")

try:
    # Open and read the file
    with open(filename, "r") as file:
        content = file.read()
    
    # Modify the content
    modified_content = modify_content(content)
    
    # Write to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)
    
    print(f"Modified content has been written to {new_filename}")
except FileNotFoundError:
    print("Error: The file does not exist.")
except IOError:
    print("Error: Unable to read the file.")
