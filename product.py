# create class
class Product:
    # from previous,dict have id/name/price/stock
    # after self.__ (private attributes)
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

# get id from class
    def get_product_id(self):
        return self.__product_id

# 1.display from class
    def display_information(self):
        print(f"ID:{self.__product_id} | Name:{self.__name} |"
              f"Price:${self.__price:} | Stock:{self.__stock}"
              )

# 3.update stock from class
    def update_stock(self, quantity):
        if quantity < 0:
            print("Stock cannot be negative.")
            return False
        self.__stock = quantity
        return True

# return to dict ,from class


def to_dict(self):
    return {"ID": self.__product_id, "Name": self.__name,
            "Price": self.__price, "Stock": self.__stock}
