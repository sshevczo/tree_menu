from django.urls import path
from .views import index, draw_menu

urlpatterns = [

    path('', index, name='menu_main'),
    path('<path:path>/', draw_menu, name='draw_menu'),
]
