# Generated by Django 4.2 on 2023-12-08 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doc_to_pdf', '0002_alter_doctopdf_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='doctopdf',
            table='doc_to_pdf',
        ),
    ]