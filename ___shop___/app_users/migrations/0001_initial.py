# Generated by Django 4.1.4 on 2023-01-07 16:39

import app_users.managers
import app_users.models
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyGroups',
            fields=[
            ],
            options={
                'verbose_name': 'группа',
                'verbose_name_plural': 'группы',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('full_name', models.CharField(max_length=254, verbose_name='Полное имя')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('avatar_file', models.ImageField(blank=True, null=True, upload_to='images/user_avatars/', validators=[app_users.models.User.validate_image_size, django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif', 'jpeg'], message='Расширение не поддерживается. Разрешенные расширения .jpg .gif .png .jpeg')], verbose_name='Аватар')),
                ('phoneNumber', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\d{10}$')], verbose_name='Телефон')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Сотрудник')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
                'db_table': 'users',
                'ordering': ['id'],
            },
            managers=[
                ('objects', app_users.managers.UserManager()),
            ],
        ),
    ]
