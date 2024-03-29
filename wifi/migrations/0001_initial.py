# Generated by Django 2.2.6 on 2019-11-21 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('reg_date', models.DateTimeField(verbose_name='date published')),
                ('expaire_date', models.DateTimeField(null=True)),
                ('id_card', models.FileField(upload_to='uploads/')),
                ('phone', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('wifi_plan', models.IntegerField()),
                ('monthly_bill', models.FloatField()),
                ('payment_method', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('agent_name', models.CharField(max_length=100, null=True)),
                ('bill_address', models.TextField(null=True)),
                ('router_id', models.IntegerField()),
                ('note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wifi.Customer')),
            ],
        ),
    ]
