# Generated by Django 2.2.11 on 2020-04-21 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_import_importer_pulpimporter_pulpimporterrepository'),
    ]

    operations = [
        migrations.AlterField(
            model_name='export',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Task'),
        ),
    ]