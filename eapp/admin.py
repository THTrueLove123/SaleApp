from flask_admin.contrib.sqla import ModelView
from eapp import db, app
from eapp.models import Category, Product
from flask_admin import Admin
from flask_admin import BaseView, expose

admin = Admin(app=app, name = "SaleApp")

class TestAdmin(ModelView):
    column_list = ['id', 'name','active', 'price']
    column_searchable_list = ['name']
    column_filters = ['name','id']
class StatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')
admin.add_view(ModelView(Category, db.session))
admin.add_view(TestAdmin(Product, db.session))
admin.add_view(StatsView(name = 'THONG KE - BAO CAO'))