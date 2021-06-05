from django.core.management.base import BaseCommand, CommandError
from news.models import Post, Category


class Command(BaseCommand):
    help = 'Удаление всех новостей в категории'  # показывает подсказку при вводе "python manage.py <ваша команда> --help"
    requires_migrations_checks = True  # напоминать ли о миграциях. Если тру — то будет напоминание о том, что не сделаны все миграции (если такие есть)

    def handle(self, *args, **options):
        # здесь можете писать любой код, который выполнется при вызове вашей команды
        self.stdout.readable()
        self.stdout.write(
            'Введите категорию новостей для удаления:')  # спрашиваем пользователя действительно ли он хочет удалить все товары
        answer = input()  # считываем подтверждение

        if answer != '':
            category = Category.objects.get(name=answer)
            Post.objects.filter(category=category).delete()
            self.stdout.write(self.style.SUCCESS('Succesfully wiped posts!'))
            return

        self.stdout.write(
            self.style.ERROR('Access denied'))  # в случае неправильного подтверждения, говорим что в доступе отказано