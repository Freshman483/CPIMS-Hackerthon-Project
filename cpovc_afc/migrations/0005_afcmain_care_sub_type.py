# Generated by Django 4.1.3 on 2022-11-14 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_afc', '0004_alter_afcquestions_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='afcmain',
            name='care_sub_type',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
