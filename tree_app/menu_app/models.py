from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100, help_text='Название меню', unique=True)
    description = models.CharField(max_length=1000, help_text='Описание', blank=True, null=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Меню'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100, help_text='Название пункта меню', unique=True)
    description = models.CharField(max_length=1000, help_text='Описание пункта меню', blank=True, null=True)
    url = models.CharField(max_length=100, verbose_name='URL-адресс', blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')

    class Meta:
        ordering = ['id']
        verbose_name = 'Меню'

    def __str__(self):
        return self.name
