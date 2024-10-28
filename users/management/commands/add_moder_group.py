from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = """
    Добавления моделей группы Модератора
    """

    def handle(self, *args, **options):
        # Название группы модератора продуктов
        group_name = "Moderators"

        # Список прав для создаваемой группы
        permissions_list = [
            "can_unpublish_product",
            "delete_product"
        ]

        # Удаляем уже созданную группу если таковая имеется
        is_exists = any([x.name == group_name for x in Group.objects.all()])
        if is_exists:
            user_input = input('Данная группа уже существует. Удаляем? [Y/n]: ')
            if user_input in ['Y', '']:
                Group.objects.get(name=group_name).delete()
            else:
                return print('Неопределённый ответ. Команда не выполнена')

        moderators = Group.objects.create(name=group_name)
        for perm in permissions_list:
            moderators.permissions.add(Permission.objects.get(codename=perm))

        moderators.save()

        print(f'\nГруппа модератора продуктов "{group_name}" с правами ({', '.join(permissions_list)}) успешно создана\n↑↑↑')
