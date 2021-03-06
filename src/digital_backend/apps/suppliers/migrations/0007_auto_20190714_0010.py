# Generated by Django 2.2.3 on 2019-07-13 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('criteria', '0003_auto_20190714_0010'),
        ('suppliers', '0006_auto_20190713_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('criterion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criteria.Criterion')),
            ],
            options={
                'verbose_name': 'check result',
                'verbose_name_plural': 'check results',
            },
        ),
        migrations.AlterField(
            model_name='supplier',
            name='inn',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='ogrn',
            field=models.CharField(max_length=13, unique=True),
        ),
        migrations.DeleteModel(
            name='SupplierCheckResult',
        ),
        migrations.AddField(
            model_name='vote',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.Supplier'),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('supplier', 'criterion')},
        ),
    ]
