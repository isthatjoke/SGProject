from django.shortcuts import render
from hub.models import Hub, HubCategory, get_hub_cats_dict


def main(request):
    head_menu_object_list = get_hub_cats_dict()
    content = {
        'head_menu_object_list': head_menu_object_list,

    }

    return render(request, 'hub/index.html', context=content)
