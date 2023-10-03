# Generated by Django 4.2.4 on 2023-10-02 17:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('comment', models.TextField(verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Кллиенты',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата начала рассылки')),
                ('stop_time', models.DateTimeField(verbose_name='Дата окончания рассылки')),
                ('status', models.CharField(choices=[('started', 'Запущена'), ('created', 'Создана'), ('done', 'Завершена')], default='created', max_length=20, verbose_name='Статус рассылки')),
                ('period', models.CharField(choices=[('daily', 'Ежедневная'), ('weekly', 'Раз в неделю'), ('monthly', 'Раз в месяц')], default='daily', max_length=20, verbose_name='Периодичность рассылки')),
                ('mail_to', models.ManyToManyField(to='mailing.client', verbose_name='Кому')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=150, verbose_name='Тема письма')),
                ('message', models.TextField(verbose_name='Текст письма')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='MailingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ok', 'Успешно'), ('failed', 'Ошибка')], default='ok', verbose_name='Статус')),
                ('last_try', models.DateTimeField(auto_now_add=True, verbose_name='Дата последней попытки')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.client', verbose_name='Клиент')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailing', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
            },
        ),
        migrations.AddField(
            model_name='mailing',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailing.message', verbose_name='Сообщение'),
        ),
    ]