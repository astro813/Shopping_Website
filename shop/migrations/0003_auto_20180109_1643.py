# Generated by Django 2.0.1 on 2018-01-09 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_jacket_neck_line_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sleeve_color', models.CharField(max_length=250)),
                ('body_color', models.CharField(max_length=250)),
                ('nect_line_color', models.CharField(max_length=250)),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Cloth')),
            ],
        ),
        migrations.RemoveField(
            model_name='jacket',
            name='cloth',
        ),
        migrations.DeleteModel(
            name='jacket',
        ),
    ]
