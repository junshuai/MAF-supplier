import web
import json

render = web.template.render('.')

urls = ("/", "hello",
        "/?wines", "WineController",
        "/?orders", "OrderController")

app = web.application(urls, globals())

orders = []

class hello:
    def GET(self):
        return '<a href="./wines">Get Details</a>' + \
               '<a href="./orders">Orders</a>'

class WineController:
    def GET(self):
        with open('wines.json', 'r') as f:
            data = f.read()
        return data

class OrderController:
    def GET(self):
        return orders

    def POST(self):
        string = web.input().get('order')
        return json.loads(string)

if __name__ == "__main__":
    app.run()
