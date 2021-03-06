# Generated by Django 2.2.3 on 2019-07-13 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('criteria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('inn', models.CharField(max_length=12)),
                ('ogrn', models.CharField(max_length=13)),
            ],
            options={
                'verbose_name': 'supplier',
                'verbose_name_plural': 'suppliers',
            },
        ),
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'tender',
                'verbose_name_plural': 'tenders',
            },
        ),
        migrations.CreateModel(
            name='TenderMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='suppliers.Supplier')),
            ],
            options={
                'verbose_name': 'tender member',
                'verbose_name_plural': 'tender members',
            },
        ),
        migrations.CreateModel(
            name='SupplierType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('criteria', models.ManyToManyField(to='criteria.Criterion')),
            ],
        ),
        migrations.AddField(
            model_name='supplier',
            name='type',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to='suppliers.SupplierType'),
        ),
    ]
