from django.shortcuts import render


def main(request):
    content = {}

    return render(request, 'index.html', context=content)
