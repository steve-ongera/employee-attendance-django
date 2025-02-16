# Generated by Django 5.0.6 on 2024-05-18 13:56

import apps.employee.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_rename_generate_id_card_employee_id_card_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.CharField(default='1', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='employee_photos', validators=[apps.employee.models.validate_image]),
        ),
    ]
