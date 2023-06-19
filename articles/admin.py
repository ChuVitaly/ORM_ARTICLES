from django.forms import BaseInlineFormSet, ValidationError
from django.contrib import admin
from .models import Article, Comment, Tag, Scope, ArticleTags


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_scope_count = 0
        for form in self.forms:
            cleaned_data = form.cleaned_data
            if cleaned_data.get('is_main'):
                main_scope_count += 1

        if main_scope_count != 1:
            raise ValidationError('Ошибка: должен быть указан один основной раздел.')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset
    extra = 1
    verbose_name_plural = 'Разделы'
    verbose_name = 'Раздел'
    fields = ['tag', 'is_main']
    ordering = ['is_main', 'tag__name']


class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline, ]
    list_display = ('title', 'text', 'published_at')
    search_fields = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'article', 'pub_date')


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(ArticleTags)
