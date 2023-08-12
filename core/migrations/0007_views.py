# Generated by Django 4.2.4 on 2023-08-10 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Views',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(blank=True, max_length=200)),
                ('comment', models.TextField()),
                ('status', models.CharField(max_length=20)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.post')),
            ],
        ),
    ]
