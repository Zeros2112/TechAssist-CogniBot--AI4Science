import openai

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0, max_tokens=500):
    """
    Generate a chat-based language model completion using the OpenAI API.

    Args:
    messages (list): List of message objects with 'role' and 'content'.
    model (str): The language model to use (default is "gpt-3.5-turbo").
    temperature (float): Controls the randomness of the model's output (default is 0).
    max_tokens (int): Maximum number of tokens in the generated completion (default is 500).

    Returns:
    str: Completed message content.
    """
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens, 
    )
    return response.choices[0].message["content"]
