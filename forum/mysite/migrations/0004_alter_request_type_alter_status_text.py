# Generated by Django 4.1.7 on 2023-02-14 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_types_alter_status_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.types', verbose_name='Тип запроса'),
        ),
        migrations.AlterField(
            model_name='status',
            name='text',
            field=models.CharField(max_length=200, verbose_name='Описание статуса'),
        ),
    ]
