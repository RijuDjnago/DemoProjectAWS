# Generated by Django 5.0.6 on 2024-08-13 08:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificationbox',
            old_name='type',
            new_name='type_msg',
        ),
        migrations.AddField(
            model_name='notificationbox',
            name='request_from',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='request_from_model', to='app.requestformmodel'),
            preserve_default=False,
        ),
    ]
