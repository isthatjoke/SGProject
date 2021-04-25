from post.models import Post
from hub.models import get_hub_cats_dict


def get_moderate_count(request):
    on_moderate = Post.on_moderate_count()

    return {
        'on_moderate': on_moderate
    }


def get_menu(request):
    head_menu_object_list = get_hub_cats_dict()

    return {
        'head_menu_object_list': head_menu_object_list,
    }

