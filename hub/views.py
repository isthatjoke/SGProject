from django.shortcuts import render


def main(request):
    content = {}

    return render(request, 'hub/index.html', context=content)
