# Generated by Django 3.0.6 on 2021-07-09 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('portfolio', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='f_id',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, related_name='portfolios', to='user.Field'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portfolios', to=settings.AUTH_USER_MODEL),
        ),
    ]
