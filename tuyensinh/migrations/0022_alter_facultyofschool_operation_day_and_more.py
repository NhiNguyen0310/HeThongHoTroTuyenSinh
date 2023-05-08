# Generated by Django 4.2.1 on 2023-05-08 15:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tuyensinh", "0021_alter_facultyofschool_operation_day_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facultyofschool",
            name="operation_day",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 5, 8, 22, 6, 53, 438514)
            ),
        ),
        migrations.RemoveField(
            model_name="thongtintuyensinh",
            name="category",
        ),
        migrations.AlterField(
            model_name="thongtintuyensinh",
            name="loaithongtintuyensinh",
            field=models.ManyToManyField(to="tuyensinh.loaithongtintuyensinh"),
        ),
        migrations.AddField(
            model_name="thongtintuyensinh",
            name="category",
            field=models.ManyToManyField(to="tuyensinh.category"),
        ),
    ]
