from post.models import Post


def get_moderate_count(request):
    on_moderate = Post.on_moderate_count()

    return {
        'on_moderate': on_moderate
    }


