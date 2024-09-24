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
                "model": "catalog.category",
                "pk": 8,
                "fields": {
                    "name": "🌯Шаурма",
                    "descr": "Категория шаурмы"
                }
            },
            {
                "model": "catalog.category",
                "pk": 9,
                "fields": {
                    "name": "🍗Наггетсы",
                    "descr": "Категория наггетсов"
                }
            },
            {
                "model": "catalog.category",
                "pk": 10,
                "fields": {
                    "name": "🥤Напитки",
                    "descr": "Категория напитков"
                }
            },
            {
                "model": "catalog.product",
                "pk": 6,
                "fields": {
                    "name": "Coca-cola 0.5л",
                    "descr": "",
                    "img": "photos/photo_2024-01-31_16-51-48.jpg",
                    "category": 10,
                    "price": 90,
                    "created_at": "2024-09-18T11:39:02.314Z",
                    "updated_at": "2024-09-24T12:48:44.831Z"
                }
            },
            {
                "model": "catalog.product",
                "pk": 8,
                "fields": {
                    "name": "Сырная",
                    "descr": "Состав: Сырный лаваш, куриное филе, китайская капуста, сыр(много 😋), помидоры, маринованные огурцы, домашний сырный соус с укропом",
                    "img": "photos/photo_2024-09-24_17-23-52.jpg",
                    "category": 8,
                    "price": 270,
                    "created_at": "2024-09-24T12:22:28.133Z",
                    "updated_at": "2024-09-24T13:27:42.277Z"
                }
            },
            {
                "model": "catalog.product",
                "pk": 9,
                "fields": {
                    "name": "Классическая",
                    "descr": "Состав: Куриное филе, свежие и маринованные огурцы, помидоры, капуста, сыр, соус чесночно-томатный👌",
                    "img": "photos/photo_2024-02-01_18-38-10.jpg",
                    "category": 8,
                    "price": 250,
                    "created_at": "2024-09-24T12:23:13.054Z",
                    "updated_at": "2024-09-24T13:27:54.147Z"
                }
            },
            {
                "model": "catalog.product",
                "pk": 11,
                "fields": {
                    "name": "10шт",
                    "descr": "С соусом на выш выбор: Сладкий чили, BBQ, сырный",
                    "img": "photos/photo_2024-09-24_18-25-08.jpg",
                    "category": 9,
                    "price": 240,
                    "created_at": "2024-09-24T13:26:28.860Z",
                    "updated_at": "2024-09-24T13:26:28.860Z"
                }
            },
            {
                "model": "catalog.product",
                "pk": 12,
                "fields": {
                    "name": "Очередной товар",
                    "descr": "Для прохождения критерия по 100 символам.\r\n\r\nLorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae reprehenderit distinctio aspernatur et eius, dolore consequuntur doloremque rerum totam iusto. Delectus, velit? Cumque beatae nihil architecto, voluptatum necessitatibus debitis possimus itaque aliquid, optio aliquam tempora hic illo deleniti perferendis laborum laudantium quo eligendi ab veniam veritatis exercitationem, consequuntur facilis rerum. Sapiente, enim amet minus assumenda laboriosam iure labore mollitia. Quis dolore eveniet minima alias voluptatum libero nulla sequi expedita velit? Beatae, facilis libero nostrum, aperiam natus commodi autem dignissimos blanditiis ex exercitationem illo tempora necessitatibus dolorum reprehenderit quo magni perferendis, quia unde. Ipsum error amet velit eligendi vel consequuntur eum.",
                    "img": "",
                    "category": 8,
                    "price": 999,
                    "created_at": "2024-09-24T13:29:28.359Z",
                    "updated_at": "2024-09-24T13:29:28.359Z"
                }
            }
        ]

        with open('fixture.json', 'w', encoding='utf8') as backup:
            backup.write(json.dumps(data, ensure_ascii=False, indent=4))
