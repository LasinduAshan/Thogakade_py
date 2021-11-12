import sys
import json
import os
from pprint import pprint

__db_location__ = "db"
# __session_file__ = f"{__db_location__}/session.db"
__session_file__ = f"{__db_location__}/customer.db"
__customer_folder__ = f"{__db_location__}/customer"
__customer__last_id__ = f"{__db_location__}/customer_id.db"

__item_folder__ = f"{__db_location__}/item"
__item__last_id__ = f"{__db_location__}/item_id.db"

__order_folder__ = f"{__db_location__}/order"
__order__last_id__ = f"{__db_location__}/order_id.db"


def init(arguments):

    def db():
        os.makedirs(__customer_folder__)

    section = arguments[0]
    if section == "init":
        command = arguments[1]
        if command == "db":
            db()


def __get_logged_user():
    f = open(__session_file__, "r")
    username = f.readline()
    return username


def view():
    username = __get_logged_user()
    print(username)


def login(username):
    f = open(__session_file__, "w")
    f.write(username)
    f.close()


#-----------------------------------------------------------------------------------------------------------------
# item add

class Item:
    def __init__(self):
        if os.path.exists(__item__last_id__):
            with open(__item__last_id__, "r") as last_id_f:
                self.last_id = int(last_id_f.readline())
        else:
            self.last_id = 0

    def save(self):
        id = self.last_id+1

        # Save database item
        _data_ = {
            "id": id,
            "name": self.name,
            "price": self.price,
            "qty": self.qty
        }
        with open(f"{__item_folder__}/{id}.db", "w") as item_file:
            json.dump(_data_, item_file)

        # Save next id
        self.last_id += 1
        with open(__item__last_id__, "w") as f:
            f.write(str(self.last_id))

    def find(self, id):
        Item.__get_item_by_path(self, f"{__item_folder__}/{id}.db")

    def __get_item_by_path(item, path):
        with open(path, "r") as item_file:
            _data_ = json.load(item_file)
            item.id = _data_["id"]
            item.name = _data_["name"]
            item.price = _data_["price"]
            item.qty = _data_["qty"]

    def all(self):
        item_file_names = os.listdir(__item_folder__)
        items = []
        for item_file_name in item_file_names:
            item = Item()
            Item.__get_item_by_path(
                item, f"{__item_folder__}/{item_file_name}")
            items.append(item)
        return items

    def search(self, key, value):
        items = self.all()
        result_items = []
        for item in items:
            item_value = getattr(item,key)
            if item_value == value:
                result_items.append(item)
        return result_items


    def __repr__(self):
        return f"id:{self.id},name:{self.name},price:{self.price},qty:{self.qty}"

    def __str__(self):
        return f"id:{self.id},name:{self.name},price:{self.price},qty:{self.qty}"


# def item_create(name, price, qty):
#     item = Item()
#     item.name = name
#     item.price = price
#     item.qty = qty
#     item.save()


def item_all():
    item = Item()
    items = item.all()
    pprint(items)

def item_view(id):
    item = Item()
    item.find(id)
    print(item.id, item.name, item.price, item.qty)

def item_search(key,value):
    item = Item()
    results = item.search(key,value)
    pprint(results)



#-----------------------------------------------------------------------------------------------------------------
# customer add


class Customer:
    def __init__(self):
        if os.path.exists(__customer__last_id__):
            with open(__customer__last_id__, "r") as last_id_f:
                self.last_id = int(last_id_f.readline())
        else:
            self.last_id = 0

    def save(self):
        id = self.last_id+1

        # Save database item
        _data_ = {
            "id": id,
            "name": self.name,
            "address": self.address,
            "contact": self.contact
        }
        with open(f"{__customer_folder__}/{id}.db", "w") as customer_file:
            json.dump(_data_, customer_file)

        # Save next id
        self.last_id += 1
        with open(__customer__last_id__, "w") as f:
            f.write(str(self.last_id))

    def find(self, id):
        Customer.__get_customer_by_path(self, f"{__customer_folder__}/{id}.db")

    def __get_customer_by_path(customer, path):
        with open(path, "r") as customer_file:
            _data_ = json.load(customer_file)
            customer.id = _data_["id"]
            customer.name = _data_["name"]
            customer.address = _data_["address"]
            customer.contact = _data_["contact"]

    def all(self):
        customer_file_names = os.listdir(__customer_folder__)
        customers = []
        for customer_file_name in customer_file_names:
            customer = Customer()
            Customer.__get_customer_by_path(
                customer, f"{__customer_folder__}/{customer_file_name}")
            customers.append(customer)
        return customers

    def search(self, key, value):
        customers = self.all()
        result_customers = []
        for customer in customers:
            customer_value = getattr(customer,key)
            if customer_value == value:
                result_customers.append(customer)
        return result_customers


    def __repr__(self):
        return f"id:{self.id},name:{self.name},address:{self.address},contact:{self.contact}"

    def __str__(self):
        return f"id:{self.id},name:{self.name},adress:{self.address},contact:{self.contact}"


def customer_create(name, address, contact):
    customer = Customer()
    customer.name = name
    customer.address = address
    customer.contact = contact
    customer.save()


def customer_all():
    customer = Customer()
    customers = customer.all()
    pprint(customers)

def customer_view(id):
    customer = Customer()
    customer.find(id)
    print(customer.id, customer.name, customer.address, customer.contact)

def customer_search(key,value):
    customer = Customer()
    results = customer.search(key,value)
    pprint(results)

def customer_by_name(name):
    customer = Customer()
    customers = customer.all()
    # pprint(customers)

    for customer in customers:
        if(customer.name == name):
            return customer

#-----------------------------------------------------------------------------------------------------
#   order add


class Order:
    def __init__(self):
        if os.path.exists(__order__last_id__):
            with open(__order__last_id__, "r") as last_id_f:
                self.last_id = int(last_id_f.readline())
        else:
            self.last_id = 0

    def save(self):
        id = self.last_id+1

        # Save database item
        _data_ = {
            "oid": id,
            "cid": self.cid,
            "customer_name": self.customer_name,
            "itmid": self.itmid,
            "itm_name": self.itm_name,
            "qty": self.qty,
            "price": self.price,
            "total": self.total
        }
        with open(f"{__order_folder__}/{id}.db", "w") as order_file:
            json.dump(_data_, order_file)

        # Save next id
        self.last_id += 1
        with open(__order__last_id__, "w") as f:
            f.write(str(self.last_id))

    def find(self, id):
        Order.__get_order_by_path(self, f"{__order_folder__}/{id}.db")

    def __get_order_by_path(order, path):
        with open(path, "r") as order_file:
            _data_ = json.load(order_file)
            order.oid = _data_["oid"]
            order.cid = _data_["cid"]
            order.customer_name = _data_["customer_name"]
            order.itmid = _data_["itmid"]
            order.itm_name = _data_["itm_name"]
            order.qty = _data_["qty"]
            order.price = _data_["price"]
            order.total = _data_["total"]
            

    def all(self):
        order_file_names = os.listdir(__order_folder__)
        orders = []
        for order_file_name in order_file_names:
            order = Order()
            Order.__get_order_by_path(
                order, f"{__order_folder__}/{order_file_name}")
            orders.append(order)
        return orders

    # def search(self, key, value):
    #     customers = self.all()
    #     result_customers = []
    #     for customer in customers:
    #         customer_value = getattr(customer,key)
    #         if customer_value == value:
    #             result_customers.append(customer)
    #     return result_customers


    def __repr__(self):
        # return f"cid:{self.cid},customer_name:{self.customer_name}"
        return f"oid:{self.oid},cid:{self.cid},customer_name:{self.customer_name},itmid:{self.itmid},itm_name:{self.itm_name},qty:{self.qty},price:{self.price},total:{self.total}"

    def __str__(self):
        return f"oid:{self.oid},cid:{self.cid},customer_name:{self.customer_name},itmid:{self.itmid},itm_name:{self.itm_name},qty:{self.qty},price:{self.price},total:{self.total}"
        # return f"cid:{self.cid},customer_name:{self.customer_name}"

def order_create(itemID, qty):

    print("item id",itemID, "qty",qty)
    item = Item()
    item.find(itemID)
    # print(item.id, item.name, item.price, item.qty)

    username = __get_logged_user()
    # print(username)

    customer = customer_by_name(username)
    # print(customer.id,customer.name,customer.address,customer.contact)

    # print(int(item.price)* int(qty))

    order = Order()
    order.cid = customer.id
    order.customer_name = customer.name
    order.itmid = item.id
    order.itm_name = item.name
    order.qty = qty
    order.price = item.price
    order.total = int(item.price)* int(qty)
    order.save()
    

def order_all():
    order = Order()
    orders = order.all()

    username = __get_logged_user()


    index=0
    print("Your orders [")
    while index < len(orders):
        if(orders[index].customer_name == username):
            pprint(orders[index])
        index +=1
    print("]")
        






if __name__ == "__main__":
    arguments = sys.argv[1:]

    init(arguments)

    section = arguments[0]
    command = arguments[1]
    params = arguments[2:]

    if section == "user":
        if command == "login":
            login(*params)
        elif command == "view":
            view()
    elif section == "customer":
        if command == "create":
            customer_create(*params)
        elif command == "all":
            customer_all()
        elif command == "view":
            customer_view(*params)
        elif command == "search":
            customer_search(*params)
    elif section == "item":
        if command == "all":
            item_all()
        elif command == "view":
            item_view(*params)
        elif command == "search":
            item_search(*params)
    elif section == "order":
        if command == "create":
            order_create(*params)
        elif command == "all":
            order_all()
        elif command == "view":
            customer_view(*params)

else:
    print(__name__)
