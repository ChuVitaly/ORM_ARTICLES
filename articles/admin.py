from django.contrib import admin

from .models import Article, Comment, Tag, Scope, ArticleTags


class ScopeInline(admin.TabularInline):
    model = Scope
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

# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('title', 'text', 'published_at', 'image')






