# Generated by Django 3.1.4 on 2021-02-19 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_tbl_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('account_date', models.CharField(max_length=30)),
                ('stock', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tbl_account',
            },
        ),
    ]
