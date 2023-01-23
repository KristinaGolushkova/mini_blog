from django.contrib import admin
from .models import Rubric, Ad, Comments


# Register your models here.

@admin.register(Rubric)
class RubricAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'rubric', 'date']

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'post')