# Generated by Django 4.2.1 on 2023-06-02 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductCategory",
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
                ("name", models.CharField(max_length=50, verbose_name="商品分類名稱")),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=500, null=True, verbose_name="商品分類描述"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="建立日期"),
                ),
                ("modified", models.DateTimeField(auto_now=True, verbose_name="修改日期")),
            ],
            options={
                "verbose_name": "商品分類",
                "verbose_name_plural": "商品分類",
                "ordering": ["-created"],
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=50, verbose_name="商品名稱")),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=500, null=True, verbose_name="商品描述"
                    ),
                ),
                ("price", models.PositiveIntegerField(default=0, verbose_name="商品價格")),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="建立日期"),
                ),
                ("modified", models.DateTimeField(auto_now=True, verbose_name="修改日期")),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="product_set",
                        to="products.productcategory",
                        verbose_name="商品分類",
                    ),
                ),
            ],
            options={
                "verbose_name": "商品",
                "verbose_name_plural": "商品",
                "ordering": ["-created"],
            },
        ),
    ]
