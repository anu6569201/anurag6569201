# Generated by Django 5.0 on 2024-03-21 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_projectsmod_orderid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsgenere',
            name='prjGen',
            field=models.ManyToManyField(blank=True, related_name='prjGen', to='project.projectsmod'),
        ),
    ]
