def output_to_console(text):
    """
    Outputs the specified text to the console.

    Args:
        text (str): The text to be printed to the console.
    """
    print(text)

def write_to_file(filename, text):
    """
    Writes the specified text to a file. If the file already exists, it will
    be overwritten.

    Args:
        filename (str): The path to the file where the text will be written.
        text (str): The text to write to the file.
    """
    with open(filename, 'w') as file:
        file.write(text)
