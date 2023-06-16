# Generated by Django 4.1.7 on 2023-04-18 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_category_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='tematic',
            field=models.CharField(choices=[('CULTURE', 'Культура'), ('SCIENCE', 'Наука'), ('TECH', 'Технология'), ('POLITICS', 'Политика'), ('SPORT', 'Спорт'), ('ENTERTAINMENT', 'Развлечения'), ('ECONOMICS', 'Экономика'), ('EDUCATIONS', 'Образование')], max_length=100, unique=True),
        ),
    ]
