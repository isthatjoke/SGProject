from django.core.management import BaseCommand

from authapp.models import HubUser
from hub.models import Hub, HubCategory
from post.models import Post


class Command(BaseCommand):

    def handle(self, *args, **options):

        # Очищаем базу данных
        HubUser.objects.all().delete()
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

             'content': 'Мы в проекте Embox некоторое время назад запустили Qt на платформе STM32. '
                          'Примером было приложение moveblocks — анимация с четырьмя синими квадратами, '
                          'которые перемещаются по экрану. Нам захотелось большего, например, '
                          'добавить интерактивность, '
                          'ведь на плате доступен тачскрин. Мы выбрали приложение animatedtiles просто потому, что оно '
                          'и на компьютере круто смотрится. По нажатию виртуальных кнопок множество иконок плавно '
                          'перемещаются по экрану, собираясь в различные фигуры. Причем выглядит это вполне как 3d '
                          'анимация и у нас даже были сомнения, справится ли микроконтроллер с подобной задачей.',
             'hub_category': 'программирование', 'user_id': 'User_1'},

            {'name': 'История одного видео редактора',

             'content': 'Эта история берет начало у истока 2019 года, когда я заметил, что мое бесполезное '
                          'пребывание в интернете, социальных сетях и смартфоне стало критичным и я решил вовлечь '
                          'себя в собственный эксперимент цифровой детоксикации. К слову сказать данный опыт '
                          'продолжался ориентировочно пол года и он очень сильно повлиял на мои современные взгляды. '
                          'В тот момент я искал кнопочный телефон, чтобы заменить им смартфон, который отнимал '
                          'уйму времени. Так ко мне попал matrix-фон Nokia 8110 с KaiOS на борту и именно с '
                          'этого момента когда я клал трубку после очередного разговора, приятели шутили, '
                          'что мне опять звонил тот самый бог сновидений Морфеус.',
             'hub_category': 'разработка мобильных приложений',
             'user_id': 'User_1'},

            {'name': 'Вышел релиз GitLab 13.10 с улучшениями для администраторов и управлением уязвимостями',
             'content': 'GitLab 13.10 уже доступен! В этом месяце мы сосредоточили наше внимание на масштабируемости и удобстве управления продуктом, чтобы вы могли итерировать и вводить новшества быстрее, безопаснее и с меньшим количеством проблем. Релиз 13.10 предлагает улучшения администрирования для масштабирования DevOps в вашей организации, проверку целостности пакетов для аварийного восстановления с Geo, автоматизацию управления уязвимостями для большей эффективности и согласованности в обеспечении безопасности и, как и всегда, множество фантастических вкладов от нашего обширного сообщества. Это — лишь некоторые из более чем 40 новых фич и улучшений в данном релизе.', 'hub_category': 'DevOps', 'user_id': 'User_1'},

            {'name': 'Подключаем SSD форм-фактора М2 к материнке, у которой нет разъема М2 и делаем этот SSD системным. Танцы с бубном',
             'content': 'Давным-давно, когда в мире жестких дисков только стали появляться твердотельные, я, как все прогрессивное человечество, озаботился приростом производительности посредством этой самой твердотельности носителей. Был куплен недорогой SSD марки Vertex, объемом 120 Гб и с успехом водружен в потроха компьютера. Не помню уже как туда заливалась система (и какая), с трудностями или без, но прирост скорости ощутился конкретно. К диску прилагалась наклейка со словами «My SSD is faster then your HDD», что грело обладателя сего девайса.', 'hub_category': 'Хранение данных', 'user_id': 'User_1'},

            {'name': 'Веб-империя правительства UK: все во имя человека, для блага человека',
             'content': 'Цифровизация сейчас в повестке дня едва ли не любого государства. Но все понимают ее по-разному, по-разному ее начинают, до разной степени готовности и продуманности доводят и приоритеты расставляют по-разному. Для кого-то и у кого-то цифровизация – это контроль и запреты, для кого-то и у кого-то – удобство и польза каждого отдельного гражданина. С первым вариантом вы все знакомы очно, а о том, как властям Великобритании удается идти по второму пути рассказываем в этой статье на примере подходов к созданию правительственных сайтов.', 'hub_category': 'Usability', 'user_id': 'User_1'},

            {'name': 'От эскиза до релиза: пайплайн регулярного создания контента на примере идеи для оружия от игрока',
             'content': 'Огромное количество игр построено на сервисной поддержке, будь то тактический шутер Rainbow Six Siege или большая ролевая World of Warcraft. Игроков постоянно вовлекают ивентами, игровыми режимами, картами, персонажами или перками. Но когда в проекте уже сотни и тысячи единиц контента, а релизы ежемесячно — это может стать проблемой для разработчиков.', 'hub_category': 'Работа с 3D-графикой', 'user_id': 'User_1'},

            {'name': 'Как сделать полнотекстовую поисковую машину на 150 строках кода Python',

             'content': 'Полнотекстовый поиск — неотъемлемая часть нашей жизни. Разыскать нужные материалы в сервисе'
                          ' облачного хранения документов Scribd, найти фильм в Netflix, купить туалетную бумагу на '
                          'Amazon или отыскать с помощью сервисов Google интересующую информацию в Интернете — '
                          'наверняка вы сегодня уже не раз отправляли похожие запросы на поиск нужной информации в'
                          ' невообразимых объёмах неструктурированных данных. И что удивительнее всего — несмотря на '
                          'то что вы осуществляли поиск среди миллионов (или даже миллиардов) записей, вы получали '
                          'ответ за считанные миллисекунды. Специально к старту нового потока курса '
                          'Fullstack-разработчик на Python, в данной статье мы рассмотрим основные компоненты '
                          'полнотекстовой поисковой машины и попытаемся создать систему, которая сможет за миллисекунды '
                          'находить информацию в миллионах документов и ранжировать результаты по релевантности, '
                          'причём всю систему можно воплотить всего в 150 строках кода на Python!',
             'hub_category': 'программирование',
             'user_id': 'User_1'},

            {'name': 'Жизнь без AppStore и Google Play: работаем с Huawei Mobile Services и AppGallery',

             'content': 'С конца 2019 Huawei поставляет Android-смартфоны без сервисов Google, в том '
                          'числе без привычного всем магазина приложений Google Play. В'
                          ' качестве альтернативы китайская компания предлагает собственные разработки — '
                          'Huawei Mobile Services (HMS), а также магазин AppGallery. В этом тексте мы расскажем, '
                          'как с этим жить и работать.', 'hub_category': 'разработка мобильных приложений',
             'user_id': 'User_2'},

            {'name': 'Деплоим проект на Kubernetes в Mail.ru Cloud Solutions. Часть 1: архитектура приложения, запуск Kubernetes и RabbitMQ',
             'content': 'О Kubernetes и его роли в построении микросервисных приложений известно, пожалуй, большинству современных IT-компаний. Однако при его внедрении часто возникает вопрос — какой вариант установки выбрать: Self-Hosted или Managed-решение от одного из облачных провайдеров. О недостатках первого варианта, думаю, известно всем, кто проходил через ручное конфигурирование K8s: сложно и трудоемко. Но в чем лучше Cloud-Native подход?', 'hub_category': 'DevOps', 'user_id': 'User_2'},

            {'name': 'С днём бэкапа! Но не бэкапом единым…',
             'content': '31 марта — это такой Хэллоуин безопасников: по легенде именно в этот день всякая нечисть вылезает из даркнета и бомбит атаками ИТ-инфраструктуру компаний. Кто-то нацеливается на компании покруче и ищет славы, кто-то тихо крысит коммерческую информацию, чтобы продать её подороже… И тут день бы выстоять да ночь продержаться. Но это, конечно, чистой воды сказка и миф: на самом деле угрозы информационной безопасности существуют не в последний день марта, а в режиме 24/7/365. Но многим почему-то пофиг: у них есть подушки безопасности в автомобиле, они пристёгивают ремень, надевают шлем на картинге, страхуют жилище, ставят сигнализацию на квартиру и автомобиль, надевают чехол на дорогой телефон, но на работе упорно пишут пароли на стикерах, жмотятся на средства безопасности и наивно полагают, что уж их компания-то точно никому не сдалась. ', 'hub_category': 'Хранение данных', 'user_id': 'User_2'},

            {'name': 'Компьютеры, какими я их любил',
             'content': 'Я много лет боролся с проблемой синхронизации файлов. В самом начале Dropbox был отличным сервисом, но в последние несколько лет они начали разрастаться. Я перешел на iCloud, но это было еще хуже. Наконец, несколько дней назад, после того, как iCloud снова загадочно сломался, я решил, что пора попробовать что-то другое. Я попробовал Syncthing, бесплатную альтернативу с открытым исходным кодом. И знаете, что? Это стало освобождением. Разумность, простота, надежность, различные функции. Это приносит радость от использования и заставляет поверить в то, что распад цивилизации можно немного замедлить.', 'hub_category': 'Usability', 'user_id': 'User_2'},

            {'name': 'Почему мы отказались от стандартных теней Unity для мобильных шутеров и вместо этого написали свои',
             'content': 'Использование освещения и теней практически в любом игровом проекте добавляет реализма картинке и подчеркивает взаимное расположение объектов в сцене. Без них игры были бы скучными, безжизненными, было бы сложнее ориентироваться в игровом мире. Сегодня мы расскажем, как в геймдеве делаются тени — в реальном времени и статичные. В своих проектах War Robots и Dino Squad мы используем сразу несколько техник — им и уделим особое внимание.', 'hub_category': 'Работа с 3D-графикой', 'user_id': 'User_2'},

            {'name': 'Какая «идеальная» цель развития у языков программирования?',

             'content': 'С постоянной периодичностью появляется информация о выходе новой версии того или иного '
                          'языка программирования. И с каждой новой версией расширяются его возможности, добавляются'
                          ' новые синтаксические конструкции или иные улучшения. И это очень сильно напоминает '
                          'развитие '
                          'технологий, как и в любой другой области техники. Когда с очередным этапом '
                          'совершенствуются создаваемые творения. Быстрее, выше, сильнее … и одновременно '
                          'значительно сложнее. Понятно, что дата публикации статьи говорит сама за себя.'
                          ' Тем не менее, новые стандарты С++, постоянно выходящие спецификации Java или новый '
                          'синтаксис у PHP 8, невольно заставляют задуматься, а в нужную ли сторону идет развитие '
                          'языков программирования? Ведь большинство нововведений добавляют сложность в основной '
                          'рабочий инструмент и решая одни проблемы, неявно добавляя множество других.',
             'hub_category': 'программирование', 'user_id': 'User_3'},

            {'name': 'Как реализовать таб-бар с нестандартной кнопкой: CAShapeLayer и UIResponderChain',

             'content': 'Дизайн играет важную роль в мобильном приложении, напрямую влияя на его успех. '
                          'На этапе проектирования интерфейса часто отдается предпочтение нестандартным, '
                          'иногда даже интерактивным, элементам, которые будут притягивать взгляд, способствуя '
                          'повышению показателя user retention (удержание пользователей).',
             'hub_category': 'разработка мобильных приложений',
             'user_id': 'User_3'},

            {'name': 'Выдерни шнур, выдави стекло',
             'content': 'Привет. У каждого на работе иногда случаются «чёрные» дни. Для меня такими днями являются аварии в работе сервисов, приводящие к недоступности систем для конечных пользователей. По счастью, такое происходит нечасто, но каждый такой случай заставляет меня долго рефлексировать над вопросами «что мы сделали не так».', 'hub_category': 'DevOps', 'user_id': 'User_3'},

            {'name': 'На каких серверах держится Архив Интернета?',
             'content': 'Internet Archive — некоммерческая организация, которая с 1996 года сохраняет копии веб-страниц, графические материалы, видео- и аудиозаписи и программное обеспечение. Каждый может зайти в Wayback Machine и посмотреть, как выглядел Хабр в 2006 году или «Яндекс» в 1998 году, хотя загрузка архивных копий занимает около минуты (это не для реализма 90-х, а по техническим причинам, см. ниже).', 'hub_category': 'Хранение данных', 'user_id': 'User_3'},

            {'name': 'Гайд по UI анимации. Как начать анимировать интерфейсы',
             'content': 'Привет! Меня зовут Айгуль, я продуктовый дизайнер в Райффайзенбанке, а до этого работала в Mail.ru Group, OneTwoTrip и приложила руку к нескольким стартапам. Как-то я взяла на себя задачу продумать систему UI-анимаций для дизайн-системы. Но когда я начала над ней работу, удивилась, как мало написано практических материалов. В статьях часто перечисляют правила анимации Уолта Диснея, которые никак не помогают в UI, или авторы делают подборку красивых гифок без намека на то, как такое реализовать.', 'hub_category': 'Usability', 'user_id': 'User_3'},

            {'name': 'Средства моделирования крупных сборок: хорошие новости для производителей промышленного оборудования',
             'content': 'При разработке конвейерных систем, промышленных роботов, строительного оборудования и других механизмов с крупными узлами, производители промышленного оборудования сталкиваются со специфическими проблемами. Дело в том, что электромеханические системы становятся сложнее. Большие сборочные узлы замедляют темпы проектирования и увеличивают вероятность пространственных ошибок и других конструкторских и технологических проблем. А поскольку большинство сложных систем проектируются на заказ, в каждом проекте эти проблемы повторяются вновь и вновь.', 'hub_category': 'Работа с 3D-графикой', 'user_id': 'User_3'},

            {'name': 'IntelliJ IDEA 2021.1',
             'content': 'Сегодня у нас особый день: состоялся первый релиз этого года — IntelliJ IDEA 2021.1! '
                          'Обновление уже доступно на нашем сайте и в Toolbox App. Кроме того, можно обновиться '
                          'из самой IDE или с помощью snap-пакета, если вы являетесь пользователем Ubuntu. В этой'
                          ' версии введено множество новых функций и устранены некоторые недочеты. Теперь вы можете '
                          'работать с Java-проектами в WSL 2, использовать интегрированный Space, устраивать '
                          'видеозвонки при совместной работе над кодом с сервисом Code With Me и запускать код'
                          ' на SSH хостах и в Docker-контейнерах. А еще мы добавили базовую поддержку Java 16, '
                          'ряд новых полезных инспекций и возможность предпросмотра HTML-файлов прямо из IDE. И '
                          'это далеко не все! Изменения затронули практически каждый раздел IDE.',
             'hub_category': 'программирование', 'user_id': 'User_4'},

            {'name': 'Как сократить стоимость мобильной разработки',
             'content': 'MVP (Minimum Viable Product – «минимально жизнеспособный продукт») – необходим, чтобы '
                          'понять, как товар или услуга заскакивает аудитории, при максимальных затратах на '
                          'воссоздание. Ей не требуются структурные и дизайнерские излишества – всё, что там '
                          'не будет, работает сурово на бизнес-задача продукта. Концепция MVP уместна, когда '
                          'нужно отпустить приложение своевременно, понять, что индивидуумы будут им пользоваться, '
                          'и перепроверить все гипотезы, которые вы переформулировали на этапе строительства. '
                          'Выбрав её, вы не истратите деньги на скучный аудитории товар. А если интереса не будет, '
                          'то вы сможете развивать приложение дальше. MVP-версия мобильного дополнения для '
                          'интернет-магазина должна непременно состоять из главной страницы, справочника с поиском,'
                          ' корзины и функции выплаты.', 'hub_category': 'разработка мобильных приложений',
             'user_id': 'User_4'},

            {'name': 'Реализуем бессерверный API с AWS Gateway и Lambda',
             'content': 'Без API не обходится ни одно веб-приложение. Для их разработки используются разные методы. Сейчас, например, набирает популярность бессерверный подход — он экономичный, масштабируемый и относительно простой. Как ведущий провайдер бессерверных вычислений Amazon Web Services (AWS) вносит огромный вклад в бессерверную разработку. Здесь мы обсудим общие концепции реализации API с помощью AWS Lambda и других сервисов AWS.', 'hub_category': 'DevOps', 'user_id': 'User_4'},

            {'name': 'Администрирование Informatica PowerCenter в деталях, часть первая',
             'content': 'Привет! Меня зовут Баранов Владимир, и я уже несколько лет администрирую Informatica в «Альфа-Банк». В статье я поделюсь опытом работы с Informatica PowerCenter. IPC это платформа, которая занимается ETL (Extract, Transformation, Loading). Я сосредоточусь на описании конкретных кейсов и решений, расскажу о некоторых тонкостях и постараюсь дать пищу для ума. ', 'hub_category': 'Хранение данных', 'user_id': 'User_4'},

            {'name': 'Юзабилити-тестирование на удаленке. Выводы и лайфхаки по итогам года работы',
             'content': 'Год назад пандемия вынудила работодателей отправить сотрудников по домам. Офисы опустели, и многим пришлось корректировать схемы взаимодействия внутри команд, искать новые инструменты для выполнения задач. В том числе и софтверным компаниям — так, наш коллектив столкнулся с невозможностью провести привычное «коридорное» юзабилити-тестирование. В новых условиях нельзя было просто постучаться к коллегам с просьбой пройти пользовательский сценарий новой версии интерфейса. Нужно было искать иное решение. ', 'hub_category': 'Usability', 'user_id': 'User_4'},

            {'name': 'Оптимальная расчетная конечно-элементная модель. Способы соединения частей КЭ модели',
             'content': '«Оптимальная расчетная конечно-элементная модель – какая она?» – такой чаще всего не проговоренный вслух, а порою даже и неосознанный вопрос непременно рождается (как минимум в подсознании) у каждого инженера-расчетчика при получении ТЗ на решение задачи методом конечных элементов. Каковы критерии этой самой расчетной модели-мечты? Пожалуй, здесь стоит отталкиваться от известного философского принципа «Всё следует упрощать до тех пор, пока это возможно, но не более того». Вот только как применить этот принцип к нашим научным и инженерным задачам? ', 'hub_category': 'Работа с 3D-графикой', 'user_id': 'User_4'},
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

                                  content=item['content'],
                                  hub_category=hub_category,
                                  user_id=user_id,
                                  status=Post.STATUS_PUBLISHED))
        Post.objects.bulk_create(post_list)

        print(f'Перезагрузка БД выполнена')