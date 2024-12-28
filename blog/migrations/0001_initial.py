# Generated by Django 5.1.4 on 2024-12-28 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150, verbose_name="Заголовок")),
                ("content", models.TextField(verbose_name="Содержимое")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="blog/image",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(auto_now_add=True, verbose_name="Дата создания"),
                ),
                (
                    "publication",
                    models.BooleanField(default=True, verbose_name="публикация"),
                ),
                (
                    "number_views",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Укажите количество просмотров",
                        verbose_name="Количество просмотров",
                    ),
                ),
            ],
            options={
                "verbose_name": "блог",
                "verbose_name_plural": "блоги",
            },
        ),
    ]
