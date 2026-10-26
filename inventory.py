# create class
class Inventory:
    def __init__(self):
        # products is a dict
        self.__products = []

# get products from dict
    def get_products(self):
        return self.__products

# 1.display from dict
    def display_products(self):
        print("\nCurrent Inventory:")
        print("------------------")
        # from product.py
        for product in self.__products:
            product.display_information()
        print("------------------")


# 4.search from dict

    def search_product(self, product_id):
        for product in self.__products:
            # from product.py
            if product.get_product_id() == product_id:
                return product_id
            return None

# 2.add from dict
    def add_product(self, product):
        if self.search_product(product.get_product_id()) is not None:
            print("Product ID already exists.")
            return False
        self.__products.append(product)
        return True
