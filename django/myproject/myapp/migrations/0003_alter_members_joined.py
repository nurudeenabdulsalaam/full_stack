# Generated by Django 4.2.2 on 2023-08-20 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_members_email_members_membertype_alter_members_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='Joined',
            field=models.DateTimeField(null=True),
        ),
    ]