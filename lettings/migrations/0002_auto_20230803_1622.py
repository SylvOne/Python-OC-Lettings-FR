# Generated by Django 3.0 on 2023-08-03 16:22

from django.db import migrations

def copy_data(apps, schema_editor):
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    NewAddress = apps.get_model('lettings', 'Address')
    for old_obj in OldAddress.objects.all():
        NewAddress.objects.create(
            number=old_obj.number,
            street=old_obj.street,
            city=old_obj.city,
            state=old_obj.state,
            zip_code=old_obj.zip_code,
            country_iso_code=old_obj.country_iso_code
        )

    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    NewLetting = apps.get_model('lettings', 'Letting')
    for old_obj in OldLetting.objects.all():
        address = NewAddress.objects.get(id=old_obj.address.id)
        NewLetting.objects.create(
            title=old_obj.title,
            address=address
        )

class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_data),
    ]
