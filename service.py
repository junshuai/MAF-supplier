import web

render = web.template.render('.')

urls = ("/", "hello",
        "/?wines", "WineController")

app = web.application(urls, globals())

class hello:
    def GET(self):
        return '<a href="./wines">Get Details</a>' + \
               '<a href="./orders">Orders</a>'

class WineController:
    def GET(self):
        with open('wines.json', 'r') as f:
            data = f.read()
        return data

if __name__ == "__main__":
    app.run()
