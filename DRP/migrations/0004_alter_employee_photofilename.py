# Generated by Django 4.2.2 on 2023-07-12 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DRP", "0003_alter_employee_dateofjoining_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="PhotoFileName",
            field=models.ImageField(upload_to="Photos/"),
        ),
    ]