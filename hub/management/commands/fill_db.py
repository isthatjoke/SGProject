from django.core.management import BaseCommand

from authapp.models import HubUser
from hub.models import Hub, HubCategory
from post.models import Post


class Command(BaseCommand):

    def handle(self, *args, **options):

        # Очищаем базу данных
        # HubUser.objects.all().delete()
        Hub.objects.all().delete()
        HubCategory.objects.all().delete()
        Post.objects.all().delete()

        user_list = list()
        user_names = [
            {'username': 'User_1', 'password': 'geekbrains',
             'email': 'user1@test.ru'},
            {'username': 'User_2', 'password': 'geekbrains',
             'email': 'user2@test.ru'},
            {'username': 'User_3', 'password': 'geekbrains',
             'email': 'user3@test.ru'},
            {'username': 'User_4', 'password': 'geekbrains',
             'email': 'user4@test.ru'},
        ]
        hub_list = list()
        hub_names = ('разработка', 'администрирование', 'дизайн')
        hub_category_list = list()
        hub_category_names = [
            {'name': 'программирование', 'description': 'Искусство создания компьютерных программ',
             'tags': '#python, #programmer', 'category': 'разработка'},
            {'name': 'разработка мобильных приложений', 'description': 'Android, iOS, Windows Phone и прочие',
             'tags': '#swift, #Java', 'category': 'разработка'},
            {'name': 'DevOps', 'description': 'Методология разработки программного обеспечения',
             'tags': '#Docker, #Linux', 'category': 'администрирование'},
            {'name': 'Хранение данных', 'description': 'Что имеем, то храним',
             'tags': '#PostgreSQL, #MySQL', 'category': 'администрирование'},
            {'name': 'Usability', 'description': 'Удобство использования',
             'tags': '#Photoshop, #paint', 'category': 'дизайн'},
            {'name': 'Работа с 3D-графикой', 'description': "It's time to render!",
             'tags': '#3d-maker, #blender', 'category': 'дизайн'},
        ]
        post_list = list()
        post_name = [
            {'name': 'Запуск QT на STM32. Часть 2. Теперь с псевдо 3d и тачскрином',
             'short_desc': 'Мы в проекте Embox некоторое время назад запустили Qt на платформе STM32.',
             'post_text': 'Мы в проекте Embox некоторое время назад запустили Qt на платформе STM32. Примером было приложение moveblocks — анимация с четырьмя синими квадратами, которые перемещаются по экрану. Нам захотелось большего, например, добавить интерактивность, ведь на плате доступен тачскрин. Мы выбрали приложение animatedtiles просто потому, что оно и на компьютере круто смотрится. По нажатию виртуальных кнопок множество иконок плавно перемещаются по экрану, собираясь в различные фигуры. Причем выглядит это вполне как 3d анимация и у нас даже были сомнения, справится ли микроконтроллер с подобной задачей.',
             'hub_category': 'программирование', 'user_id': 'User_1'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'разработка мобильных приложений',
             'user_id': 'User_1'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'DevOps', 'user_id': 'User_1'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'Хранение данных', 'user_id': 'User_1'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'Usability', 'user_id': 'User_1'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'Работа с 3D-графикой', 'user_id': 'User_1'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'программирование', 'user_id': 'User_2'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'разработка мобильных приложений',
             'user_id': 'User_2'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'DevOps', 'user_id': 'User_2'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'Хранение данных', 'user_id': 'User_2'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'Usability', 'user_id': 'User_2'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'Работа с 3D-графикой', 'user_id': 'User_2'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'программирование', 'user_id': 'User_3'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'разработка мобильных приложений',
             'user_id': 'User_3'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'DevOps', 'user_id': 'User_3'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'Хранение данных', 'user_id': 'User_3'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'Usability', 'user_id': 'User_3'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'Работа с 3D-графикой', 'user_id': 'User_3'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'программирование', 'user_id': 'User_4'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'разработка мобильных приложений',
             'user_id': 'User_4'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'DevOps', 'user_id': 'User_4'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'Хранение данных', 'user_id': 'User_4'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'Usability', 'user_id': 'User_4'},
            {'name': 'программирование', 'short_desc': 'Искусство создания компьютерных программ',
             'post_text': '#python, #programmer', 'hub_category': 'Работа с 3D-графикой', 'user_id': 'User_4'},
        ]

        for item in user_names:
            user_list.append(HubUser(username=item['username'], password=item['password'], email=item['email']))

        HubUser.objects.bulk_create(user_list)

        for item in hub_names:
            hub_list.append(Hub(name=item))

        Hub.objects.bulk_create(hub_list)

        for item in hub_category_names:
            hub = Hub.objects.get(name=item['category'])
            hub_category_list.append(HubCategory(name=item['name'], description=item['description'],
                                                 tags=item['tags'], category=hub))

        HubCategory.objects.bulk_create(hub_category_list)

        for item in post_name:
            hub_category = HubCategory.objects.get(name=item['hub_category'])
            user_id = HubUser.objects.get(username=item['user_id'])
            post_list.append(Post(name=item['name'],
                                  short_desc=item['short_desc'],
                                  post_text=item['post_text'],
                                  hub_category=hub_category,
                                  user_id=user_id))
        Post.objects.bulk_create(post_list)

        print(f'Перезагрузка БД выполнена')