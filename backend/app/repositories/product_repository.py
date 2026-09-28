products = {
    1: {
        "id": 1,
        "name": "keyboard",
        "price": 5000,
    },
    2: {
        "id": 2,
        "name": "mouse",
        "price": 3000,
    },
}

def find_all():
    
    return list(products.values())
    
def find_by_id(product_id: int):
    
    return products.get(product_id)

def save(product: dict):
    
    products[product["id"]] = product
    
    return product

def count():
    
    return len(products)

def update(product_id: int, product: dict):
    products[product_id] = product
    return product

def delete(product_id: int):

    deleted_product = products.pop(product_id)

    return deleted_product