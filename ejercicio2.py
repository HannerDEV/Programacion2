products = [
    ("Laptop", "Electronics", 2500, 5),
    ("Mouse", "Electronics", 80, 20),
    ("Keyboard", "Electronics", 150, 8),
    ("Chair", "Furniture", 450, 12),
    ("Desk", "Furniture", 900, 3),
    ("Monitor", "Electronics", 700, 0),
]

categories = [
    "Electronics",
    "Electronics",
    "Electronics",
    "Furniture",
    "Furniture",
    "Electronics"
]

for product in products:
    print(f"{product[0]} -> {product[2]}")

for i, product in enumerate(products):
    print(f"{i + 1}. {product[0]}")

for product, category in zip(products, categories):
    print(f"{product[0]} -> {category}")

more_five_products = [product[0] for product in products if product[3] > 5]
print(more_five_products)

categories_set = set(categories)
print(categories_set)

products_dict = {product[0] : product[2] for product in products}
print(products_dict)

for product in products:
    assert product[2] > 0, "error"
    assert product[3] >= 0, "error"

try:
    nameProduct = input("Enter a product name: ")
    priceProduct = products_dict[nameProduct]
    print(f"Product price: {priceProduct}")
except KeyError:
    print("Product not found")
