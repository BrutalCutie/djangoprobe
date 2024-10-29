from .models import Category, Product


class ProductService:

    @staticmethod
    def get_category_prods():
        cat_products = Product.objects.filter(checkbox=True)

        return cat_products
