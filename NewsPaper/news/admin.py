from django.contrib import admin
from .models import *


class AuthorAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ['user', 'rating'] # генерируем список имён всех полей для более красивого отображения
    list_filter = ('user', 'rating')  # добавляем примитивные фильтры в нашу админку


class CategoryAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ['name'] # генерируем список имён всех полей для более красивого отображения


class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ['header', 'create_date'] # генерируем список имён всех полей для более красивого отображения
    list_filter = ('header', 'create_date')  # добавляем примитивные фильтры в нашу админку


class CommentAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ['user', 'create_date'] # генерируем список имён всех полей для более красивого отображения
    list_filter = ('user', 'create_date')  # добавляем примитивные фильтры в нашу админку


class CategoryUserAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ['user', 'category'] # генерируем список имён всех полей для более красивого отображения
    list_filter = ('user', 'category')  # добавляем примитивные фильтры в нашу админку


class PostCategoryAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ['post', 'category'] # генерируем список имён всех полей для более красивого отображения
    list_filter = ('post', 'category')  # добавляем примитивные фильтры в нашу админку


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CategoryUser, CategoryUserAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)