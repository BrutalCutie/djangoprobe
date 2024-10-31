from .models import Category, Product


class ProductService:

    @staticmethod
    def get_category_prods(category_id):
        cat_products = Product.objects.filter(checkbox=True, category=category_id)

        return cat_products


class CategoryService:

    @staticmethod
    def get_categories():
        categories = Category.objects.all()

        return categories
