from utils import *
import json

def create_categories():
    """
    This function creates a dictionary of customer support categories and their corresponding subcategories. 
    It then writes the dictionary to a JSON file.

    Returns:
    dict: The created categories dictionary.
    """
    categories_dict = {
        'Billing': [
            'Unsubscribe or upgrade',
            'Add a payment method',
            'Explanation for charge',
            'Dispute a charge'
        ],
        'Technical Support': [
            'General troubleshooting',
            'Device compatibility',
            'Software updates'
        ],
        'Account Management': [
            'Password reset',
            'Update personal information',
            'Close account',
            'Account security'
        ],
        'General Inquiry': [
            'Product information',
            'Pricing',
            'Feedback',
            'Speak to a human'
        ]
    }

    # Specify the file path for the categories JSON file.
    categories_file = 'categories.json'

    # Write the categories dictionary to the JSON file.
    with open(categories_file, 'w') as file:
        json.dump(categories_dict, file)

    return categories_dict


