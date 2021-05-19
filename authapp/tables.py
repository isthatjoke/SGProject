from django_tables2 import Table, Column, A

from authapp.models import HubUser


class UsersRatingTable(Table):
    username = Column(linkify=('post:users_posts', {'pk': A('pk')}))
    created_at = Column(verbose_name='Участник с')
    last_login = Column(verbose_name='Последняя активность')

    class Meta:
        model = HubUser
        fields = ('username', 'rating', 'last_login', 'created_at',)
