# Generated by Django 4.2.8 on 2024-01-02 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0003_student_publish_student_updated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="publish",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
