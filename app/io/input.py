import pandas

def input_from_console():
    """
    Prompts the user to enter text via the console.

    Returns:
        str: The text entered by the user.
    """
    return input("Please enter some text: ")

def read_from_file(filename):
    """
    Reads the contents of a file using Python's built-in capabilities.

    Args:
        filename (str): The path to the file to be read.

    Returns:
        str: The content of the file.
    """
    with open(filename, 'r') as file:
        return file.read()

def read_from_file_pandas(filename):
    """
    Reads the contents of a file into a pandas DataFrame.

    Args:
        filename (str): The path to the file to be read.

    Returns:
        DataFrame: The content of the file loaded into a pandas DataFrame.
    """
    return pandas.read_csv(filename)
