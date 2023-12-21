from utils import *

def get_categories():
    """
    Read and return the categories from the categories file.

    Returns:
    dict: Dictionary containing categories.
    """
    with open(categories_file, 'r') as file:
        categories = json.load(file)
    return categories

def get_product_list():
    """
    Get a flat list of products from the products file.

    Returns:
    list: List containing product names.
    """
    products = get_products()
    product_list = list(products.keys())
    return product_list

def get_products_and_category():
    """
    Get a dictionary of products grouped by category.

    Returns:
    dict: Dictionary containing categories and their associated products.
    """
    products = get_products()
    products_by_category = defaultdict(list)
    for product_name, product_info in products.items():
        category = product_info.get('category')
        if category:
            products_by_category[category].append(product_info.get('name'))
    
    return dict(products_by_category)

def get_products():
    """
    Read and return the products from the products file.

    Returns:
    dict: Dictionary containing product information.
    """
    with open(products_file, 'r') as file:
        products = json.load(file)
    return products
