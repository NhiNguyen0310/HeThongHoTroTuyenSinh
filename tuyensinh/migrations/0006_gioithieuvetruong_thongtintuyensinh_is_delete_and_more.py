# Generated by Django 4.2.1 on 2023-05-05 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tuyensinh", "0005_alter_thongtintuyensinh_content"),
    ]

    operations = [
        migrations.CreateModel(
            name="GioiThieuVeTruong",
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
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                ("active", models.BooleanField(default=True)),
                ("is_delete", models.BooleanField(default=False)),
                (
                    "img_banner",
                    models.ImageField(blank=True, null=True, upload_to="banner/%y%m%d"),
                ),
            ],
            options={
                "ordering": ["id"],
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="thongtintuyensinh",
            name="is_delete",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(upload_to="users/%Y/%m"),
        ),
    ]
