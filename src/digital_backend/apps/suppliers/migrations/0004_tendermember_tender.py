# Generated by Django 2.2.3 on 2019-07-13 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0003_tender_buyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='tendermember',
            name='tender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='suppliers.Tender'),
        ),
    ]
