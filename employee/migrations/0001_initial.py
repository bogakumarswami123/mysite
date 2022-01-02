# Generated by Django 3.1 on 2020-08-25 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.TextField(max_length=200)),
                ('designation', models.TextField(max_length=1000)),
                ('work_address', models.TextField(blank=True, max_length=1000, null=True)),
                ('home_address', models.TextField(blank=True, max_length=1000, null=True)),
                ('age', models.DecimalField(decimal_places=16, max_digits=20, null=True)),
                ('salary', models.DecimalField(decimal_places=16, max_digits=20, null=True)),
                ('experience', models.DecimalField(decimal_places=16, max_digits=20, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]