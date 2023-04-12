from django.contrib import admin

from .models import Article


# class RelationshipInlineFormset(BaseInlineFormSet):
#     def clean(self):
#         for form in self.forms:
#             # В form.cleaned_data будет словарь с данными
#             # каждой отдельной формы, которые вы можете проверить
#             form.cleaned_data
#             # вызовом исключения ValidationError можно указать админке о наличие ошибки
#             # таким образом объект не будет сохранен,
#             # а пользователю выведется соответствующее сообщение об ошибке
#             raise ValidationError('Тут всегда ошибка')
#         return super().clean()  # вызываем базовый код переопределяемого метода


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'published_at', 'image')


# class CategoryInline(admin.TabularInline):
#     model = Category


# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     inlines = [CategoryInline]
    # list_display = ['title', 'text', 'published_at', 'image']

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['id','title']
#
#
# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     pass



