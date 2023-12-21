from utils import *

def answer_user_msg(user_msg, product_info):
    """
    This function generates a response as a customer service assistant based on user input and relevant product information.

    Parameters:
    - user_msg (str): The user's message/query.
    - product_info (str): Relevant product information to be included in the response.

    Returns:
    str: The generated response from the customer service assistant.
    """
    delimiter = "####"
    system_message = """
    You are a customer service assistant for a large electronic store. \
    Respond in a friendly and helpful tone, with concise answers. \
    Make sure to ask the user relevant follow-up questions.
    """
    # Example user_msg:
    # user_msg = "Tell me about the SmartX ProPhone and the FotoSnap camera, the DSLR one. Also, what can you tell me about your TVs?"
    
    # Construct a list of messages for the OpenAI Chat API, including system, user, and assistant messages.
    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{delimiter}{user_msg}{delimiter}"},
        {'role': 'assistant', 'content': f"Relevant product information:\n{product_info}"},
    ]

    # Get the completion/response from the OpenAI Chat API.
    response = get_completion_from_messages(messages)
    return response
