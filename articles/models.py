from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название статьи')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации статьи')
    image = models.ImageField(upload_to='articles/', blank=True, null=True, verbose_name='Картинка')
    tags = models.ManyToManyField(Tag, related_name='article', through='Scope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    def get_tags_ordered(self):
        main_tag = None
        other_tags = []
        for scope in self.scope_set.all():
            if scope.is_main:
                main_tag = scope.tag
            else:
                other_tags.append(scope.tag)
        ordered_tags = [main_tag] + sorted(other_tags, key=lambda tag: tag.name)
        return ordered_tags


class ArticleTags(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_tags')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.article.title}"


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        app_label = 'articles'

    def __str__(self):
        return f"{self.tag.name} ({'Основной раздел' if self.is_main else 'Дополнительный раздел'})"


class Comment(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return f"{self.author.username} - {self.article.title}"
