# Generated by Django 3.1.4 on 2021-02-20 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_tbl_order_tbl_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_id', models.CharField(max_length=30)),
                ('coustomer_id', models.CharField(max_length=30)),
                ('product_id', models.CharField(max_length=30)),
                ('complaints', models.CharField(max_length=30)),
                ('complaint_date', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tbl_complaint',
            },
        ),
    ]