# Generated by Django 3.2.20 on 2023-07-23 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_section'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='entry',
        ),
        migrations.AddField(
            model_name='entry',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='entry', to='home.section'),
        ),
    ]