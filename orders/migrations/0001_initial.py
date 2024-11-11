# Generated by Django 5.1.3 on 2024-11-11 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('order_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
