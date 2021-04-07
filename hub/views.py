from django.shortcuts import render
from hub.models import Hub, HubCategory, get_hub_cats_dict
from post.models import Post


def main(request):
    head_menu_object_list = get_hub_cats_dict()
    all_posts = Post.get_all_posts()

    content = {
        'head_menu_object_list': head_menu_object_list,
        'all_posts_object_list': all_posts,
    }

    return render(request, 'hub/index.html', context=content)
