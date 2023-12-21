from utils import *
# The function read_string_to_list appears to be designed to convert a JSON-formatted string into a Python list. The use of json.loads is appropriate for this task, and the function handles the case where the input string is not a valid JSON by printing an error message and returning None.
def read_string_to_list(input_string):
    if input_string is None:
        return None

    try:
        input_string = input_string.replace("'", "\"")  # Replace single quotes with double quotes for valid JSON
        data = json.loads(input_string)
        return data
    except json.JSONDecodeError:
        print("Error: Invalid JSON string")
        return None


