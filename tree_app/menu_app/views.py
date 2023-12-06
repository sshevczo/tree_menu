from django.shortcuts import render
from .models import Menu


def index(request):
    context = {'menus': Menu.objects.all()}
    return render(request, 'menu_app/index.html', context=context)


def draw_menu(request, path):
    splitted_path = path.split('/')
    assert len(splitted_path) > 0, ('= Draw_menu function failed =')
    print(splitted_path)
    return render(
        request, 'app/index.html', {'menu_name': splitted_path[0], 'menu_item': splitted_path[-1]})
