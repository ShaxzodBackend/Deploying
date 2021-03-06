# Generated by Django 4.0.1 on 2022-02-05 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_aboutus_description_en_aboutus_description_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='answer_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_en',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ru',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_uz',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
