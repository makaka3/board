from django.db import models
from users.models import User


class Product(models.Model):
    KINDS = (
        ('b', 'Куплю'),
        ('s', 'Продам'),
        ('c', 'Обменяю')
    )
    title = models.CharField(
        max_length=100,
        verbose_name="Название"
    )
    content = models.TextField(
        verbose_name="Описание"
    )
    price = models.FloatField(
        verbose_name="Цена"
    )
    published = models.DateField(
        auto_now_add=True,
        verbose_name="Дата публикации"
    )
    rubric = models.ForeignKey(
        "Rubric",
        on_delete=models.PROTECT,
        verbose_name="Рубрика"
    )
    image = models.ImageField(
        null=True,
        blank=True
    )
    email = models.EmailField(
        verbose_name="Почта пользователя",
        blank=True, null=True
    )
    phone_number = models.IntegerField(
        verbose_name="Номер телефона пользователя",
    )
    addres = models.TextField(
        verbose_name="Адресс пользователя",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name="Пользователь"
    )

    kind = models.CharField(
        max_length=1,
        choices=KINDS,
        default="s",
        verbose_name="Тип объявления"
    )

    def __str__(self):
        return f"{self.title} {self.price}"

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Rubric(models.Model):
    name = models.CharField(max_length=20, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рубрика"
        verbose_name_plural = "Рубрики"
