from eapp.models import Category, Product
from eapp import app


def load_Category():
    return Category.query.order_by('id').all()
def load_Product(kw=None, Category_id=None, page=1):
    query = Product.query
    if kw:
        query = query.filter(Product.name.contains(kw))
    if Category_id:
        query = query.filter(Product.category_id == int(Category_id))
    page_size = app.config['PAGE_SIZE']
    start= (page-1)*page_size

    return query.order_by('id').slice(start, start + page_size).all()

def count_Product ():
    return Product.query.count()