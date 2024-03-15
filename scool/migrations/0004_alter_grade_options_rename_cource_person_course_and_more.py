# Generated by Django 5.0.3 on 2024-03-15 06:49

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scool', '0003_alter_course_options_course_cource_num_course_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grade',
            options={'verbose_name': 'Оценка', 'verbose_name_plural': 'Оценки'},
        ),
        migrations.RenameField(
            model_name='person',
            old_name='cource',
            new_name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='course_num',
            field=models.SmallIntegerField(default=0, verbose_name='Номер курса'),
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('name', 'course_num')},
        ),
        migrations.RemoveField(
            model_name='grade',
            name='cource',
        ),
        
        migrations.AddField(
            model_name='course',
            name='end_date',
            field=models.DateField(null=True, verbose_name='Окончание курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='start_date',
            field=models.DateField(null=True, verbose_name='Начало курса'),
        ),
        migrations.AddField(
            model_name='grade',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scool.course', verbose_name='Курс'),
        ),
        migrations.AddField(
            model_name='grade',
            name='date',
            field=models.DateField(null=True, verbose_name='Дата оценки'),
        ),
        migrations.AddField(
            model_name='grade',
            name='date_add',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата добавления'),
        ),
        migrations.AddField(
            model_name='grade',
            name='date_upd',
            field=models.DateField(auto_now=True, null=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(choices=[('py', 'Python'), ('js', 'JavaScript'), ('an', 'Android'), ('fr', 'FrontEnd')], default='', max_length=25, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scool.person', verbose_name='Чья оценка'),
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(12), django.core.validators.MaxValueValidator(99)], verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=25, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=25, verbose_name='Имя'),
        ),
        migrations.RemoveField(
            model_name='course',
            name='cource_num',
        ),
    ]
