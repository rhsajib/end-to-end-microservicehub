# Generated by Django 4.2 on 2023-12-01 19:38

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='user name')),
                ('hashed_password', models.CharField(verbose_name='password')),
                ('first_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='last name')),
                ('mobile', models.IntegerField(blank=True, max_length=50, null=True, verbose_name='mobile number')),
                ('about', models.TextField(blank=True, max_length=500, null=True, verbose_name='about')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('profile_photo', models.URLField(blank=True, verbose_name='profile photo')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'Users',
                'ordering': ['-date_joined'],
            },
        ),
    ]
