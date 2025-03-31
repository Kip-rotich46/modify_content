# File Read & Write Challenge 🖋️

## Description
This program reads a file, modifies its content, and writes the modified version to a new file. It also includes error handling to gracefully manage missing or unreadable files.

## Features
- Reads a user-specified file.
- Modifies the content (default: converts text to uppercase).
- Writes the modified content to a new file prefixed with `modified_`.
- Handles errors such as missing or unreadable files.

## Usage
1. Run the script in a Python environment.
2. Enter the filename when prompted.
3. If the file exists, a modified version will be created.
4. If the file does not exist, an error message will be displayed.

## Example
```
Enter the filename to read: example.txt
Modified content has been written to modified_example.txt
```

## Error Handling
- Displays an error message if the file does not exist (`FileNotFoundError`).
- Handles `IOError` if the file cannot be read.

## Requirements
- Python 3.x

## Author
Gideon Kiprotich

