# Generated by Django 3.0.8 on 2021-02-15 16:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0004_auto_20210214_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='jcomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='calc.jcomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.user')),
            ],
        ),
    ]
