from django.core.management.base import BaseCommand
from catalog.models import Product, Category
import json
from config.settings import BASE_DIR
import os


class Command(BaseCommand):
    help = """
    Удаление данных моделей и добавление данных из фикстуры fixture.json
    """

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        is_exist = os.path.exists(os.path.join(BASE_DIR, "fixture.json"))

        if not is_exist:
            self.self_guard()

        os.system('python -Xutf8 manage.py loaddata fixture.json --format json')

        print('Данные из фикстуры успешно загружены')

    @staticmethod
    def self_guard():
        """
        Функция служит подстраховкой, на случай если тестовый файл фикстуры был удалён.
        Создаёт json файл с данными
        :return:
        """
        data = [
            {
                "model": "catalog.product",
                "pk": 5,
                "fields": {
                    "name": "Сырная",
                    "descr": "Состав: Куриное филе, томаты, мар. огурцы, сыр(много), сырный соус",
                    "img": "",
                    "category": 8,
                    "price": 270,
                    "created_at": "2024-09-18T11:36:35.326Z",
                    "updated_at": "2024-09-18T11:36:35.326Z"
                }
            },
            {
                "model": "catalog.product",
                "pk": 6,
                "fields": {
                    "name": "Coca-cola 0.5л",
                    "descr": "",
                    "img": "",
                    "category": 10,
                    "price": 90,
                    "created_at": "2024-09-18T11:39:02.314Z",
                    "updated_at": "2024-09-18T11:39:02.314Z"
                }
            },
            {
                "model": "catalog.category",
                "pk": 8,
                "fields": {
                    "name": "Шаурма",
                    "descr": "Категория шаурмы"
                }
            },
            {
                "model": "catalog.category",
                "pk": 9,
                "fields": {
                    "name": "Наггетсы",
                    "descr": "Категория наггетсов"
                }
            },
            {
                "model": "catalog.category",
                "pk": 10,
                "fields": {
                    "name": "Напитки",
                    "descr": "Категория напитков"
                }
            }
        ]

        with open('fixture.json', 'w', encoding='utf8') as backup:
            backup.write(json.dumps(data, ensure_ascii=False, indent=4))
