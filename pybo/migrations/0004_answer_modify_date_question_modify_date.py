# Generated by Django 5.1.4 on 2025-02-20 07:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pybo", "0003_answer_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="modify_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="modify_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
