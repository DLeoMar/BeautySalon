# Generated by Django 4.0.4 on 2023-03-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_owner_appointment_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='address',
            field=models.CharField(blank=True, default='', help_text='Street, Brgy/Village, City/Town, Province', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='fathers_full_name',
            field=models.CharField(blank=True, default='', help_text='Surname FirstName, MiddleName', max_length=50, null=True, verbose_name="Father's Full Name"),
        ),
        migrations.AddField(
            model_name='appointment',
            name='godparents',
            field=models.CharField(blank=True, default='', help_text='Name of God Parents, separated by new line', max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='mothers_full_name',
            field=models.CharField(blank=True, default='', help_text='Surname FirstName, MiddleName', max_length=50, null=True, verbose_name="Mother's Full Name"),
        ),
        migrations.AddField(
            model_name='appointment',
            name='officiant',
            field=models.CharField(blank=True, default='', help_text='Name of Priest', max_length=50, null=True),
        ),
    ]
