# Generated by Django 3.0.6 on 2021-07-27 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio', '0002_auto_20210719_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deal_title', models.CharField(max_length=200)),
                ('deal_content', models.TextField()),
                ('deal_date', models.DateTimeField()),
                ('price', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('ready', '미결제'), ('paid', '결제완료')], db_index=True, default='ready', max_length=9)),
                ('u_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
