from django.db import models


# Create your models here.
class Rubric(models.Model):
    name = models.CharField(
        'Разделы отзовика',
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.name


class Ad(models.Model):
    objects = None
    title = models.CharField(
        'Название товара',
        max_length=50,
        default='func',
        unique=True,
        db_index=True,
        null=True,
        blank=True,
    )
    content = models.TextField(
        'Отзыв о товаре',
        blank=True,
        null=True,
    )
    author = models.CharField(
        'Имя автора',
        max_length=50
    )
    # assessment = models.FloatField(
    # 'Оценка',
    # null=True,
    # blank=True,
    # )
    date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True,
    )

    rubric = models.ForeignKey(
        Rubric,
        on_delete=models.PROTECT,
        related_name='entries',
        to_field='name',
        null=True,
        blank=True
    )

    img = models.ImageField('Фото товара', upload_to='image/%Y')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        unique_together = ('title', 'date')

    def __str__(self):
        return "{} {}".format(self.title, self.date)


class Comments(models.Model):
    """Комментарий"""
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(Ad, verbose_name="Отзывы", on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.name, self.post)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Likes(models.Model):
    ip = models.CharField(max_length=100)
    pos = models.ForeignKey(Ad, verbose_name='Публикация', on_delete=models.CASCADE)
