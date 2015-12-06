import web
import json


class Item:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity


class Order:
    def __init__(self, name, address, email, items):
        self.name = name
        self.address = address
        self.email = email
        self.items = items 


orders = []

urls = ("/", "index",
        "/?wines", "WineController",
        "/?orders", "OrderController")


app = web.application(urls, globals())


class index:
    def GET(self):
        render = web.template.render('.')
        return render.index(orders)


class WineController:
    def GET(self):
        with open('wines.json', 'r') as f:
            data = f.read()
        return data

class OrderController:
    def GET(self):
        pass

    def POST(self):
        order_json = web.input().get('order')
        order_d = json.loads(order_json)

        items_json = web.input().get('items')
        items_d = json.loads(items_json)

        items = [Item(item_d[u'title'], item_d[u'price'], item_d[u'quantity']) for item_d in items_d]
        orders.append(Order(order_d[u'name'], order_d[u'address'], order_d[u'email'], items))

        web.ctx.status = '201 CREATED'

    def DELETE(self):
        pass


if __name__ == "__main__":
    app.run()
