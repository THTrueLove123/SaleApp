import math

from flask import Flask, render_template, request

from eapp import app,dao


@app.route('/')
def index():
    product = dao.load_Product(kw = request.args.get('KW'),
                               Category_id = request.args.get('category_id'),
                               page = int(request.args.get('page', 1)))

    page_size = app.config['PAGE_SIZE']

    return render_template("index.html",  product=product, pages=math.ceil(dao.count_Product()/page_size))

@app.route('/login')
def login_view():
    return render_template("login.html")

@app.route('/register')
def register_view():
    return render_template("register.html")

@app.context_processor
def aaaa():
    return {
        'categories' : dao.load_Category()
    }
if __name__ == '__main__':
    with app.app_context():
        from eapp import admin
        app.run(debug=True)
