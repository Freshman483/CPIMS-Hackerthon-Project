# Generated by Django 4.0.4 on 2022-11-20 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cpovc_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegOrgUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_unit_id_vis', models.CharField(max_length=12)),
                ('org_unit_name', models.CharField(max_length=255)),
                ('org_unit_type_id', models.CharField(max_length=4)),
                ('date_operational', models.DateField(blank=True, null=True)),
                ('date_closed', models.DateField(blank=True, null=True)),
                ('handle_ovc', models.BooleanField(default=False)),
                ('is_void', models.BooleanField(default=False)),
                ('parent_org_unit_id', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Organisational Units Registry',
                'verbose_name_plural': 'Organisational Units Registries',
                'db_table': 'reg_org_unit',
            },
        ),
        migrations.CreateModel(
            name='RegPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=25, null=True)),
                ('first_name', models.CharField(max_length=255)),
                ('other_names', models.CharField(blank=True, max_length=255, null=True)),
                ('surname', models.CharField(default=None, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('des_phone_number', models.IntegerField(blank=True, default=None, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, default=None, null=True)),
                ('sex_id', models.CharField(choices=[('SMAL', 'Male'), ('SFEM', 'Female')], max_length=4)),
                ('is_void', models.BooleanField(default=False)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Persons Registry',
                'verbose_name_plural': 'Persons Registries',
                'db_table': 'reg_person',
            },
        ),
        migrations.CreateModel(
            name='RegPersonsWorkforceIds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workforce_id', models.CharField(max_length=8, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
            ],
            options={
                'db_table': 'reg_persons_workforce_ids',
            },
        ),
        migrations.CreateModel(
            name='RegPersonsTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_type_id', models.CharField(max_length=4)),
                ('date_began', models.DateField(null=True)),
                ('date_ended', models.DateField(default=None, null=True)),
                ('is_void', models.BooleanField(default=False)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
            ],
            options={
                'verbose_name': 'Person Type (Child, Caregiver, other)',
                'verbose_name_plural': 'Person Types (Child, Caregiver, other)',
                'db_table': 'reg_persons_types',
            },
        ),
        migrations.CreateModel(
            name='RegPersonsSiblings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_linked', models.DateField(null=True)),
                ('date_delinked', models.DateField(null=True)),
                ('remarks', models.TextField(null=True)),
                ('is_void', models.BooleanField(default=False)),
                ('child_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_sibling', to='cpovc_registry.regperson')),
                ('sibling_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sibling_person', to='cpovc_registry.regperson')),
            ],
            options={
                'db_table': 'reg_persons_siblings',
            },
        ),
        migrations.CreateModel(
            name='RegPersonsOtherGeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=4, null=True)),
                ('city', models.CharField(max_length=150, null=True)),
                ('date_linked', models.DateField(null=True)),
                ('is_void', models.BooleanField(default=False)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cpovc_main.setuplocation')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
            ],
            options={
                'verbose_name': 'Person Geo area (Country, City, Location)',
                'verbose_name_plural': 'Person Geo areas (Country, City, Location)',
                'db_table': 'reg_person_other_geo',
            },
        ),
        migrations.CreateModel(
            name='RegPersonsOrgUnits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_linked', models.DateField(null=True)),
                ('date_delinked', models.DateField(blank=True, null=True)),
                ('primary_unit', models.BooleanField(default=False)),
                ('reg_assistant', models.BooleanField(default=False)),
                ('is_void', models.BooleanField(default=False)),
                ('org_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regorgunit')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
            ],
            options={
                'verbose_name': 'Persons Organisation Unit',
                'verbose_name_plural': 'Persons Organisation Units',
                'db_table': 'reg_persons_org_units',
            },
        ),
        migrations.CreateModel(
            name='RegPersonsGuardians',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship', models.CharField(max_length=5)),
                ('date_linked', models.DateField(null=True)),
                ('date_delinked', models.DateField(null=True)),
                ('child_headed', models.BooleanField(default=False)),
                ('is_void', models.BooleanField(default=False)),
                ('child_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_person', to='cpovc_registry.regperson')),
                ('guardian_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guardian_person', to='cpovc_registry.regperson')),
            ],
            options={
                'db_table': 'reg_persons_guardians',
            },
        ),
        migrations.CreateModel(
            name='RegPersonsGeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_type', models.CharField(max_length=4)),
                ('date_linked', models.DateField(null=True)),
                ('date_delinked', models.DateField(null=True)),
                ('is_void', models.BooleanField(default=False)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_main.setupgeography')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
            ],
            options={
                'verbose_name': 'Person Geographical area (Ward, Sub-county)',
                'verbose_name_plural': 'Person Geographical areas (Ward, Sub-county)',
                'db_table': 'reg_persons_geo',
            },
        ),
        migrations.CreateModel(
            name='RegPersonsExternalIds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier_type_id', models.CharField(max_length=4)),
                ('identifier', models.CharField(max_length=255)),
                ('is_void', models.BooleanField(default=False)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
            ],
            options={
                'db_table': 'reg_persons_external_ids',
            },
        ),
        migrations.CreateModel(
            name='RegPersonsContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_detail_type_id', models.CharField(max_length=4)),
                ('contact_detail', models.CharField(max_length=255)),
                ('is_void', models.BooleanField(default=False)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
            ],
            options={
                'db_table': 'reg_persons_contact',
            },
        ),
        migrations.CreateModel(
            name='RegPersonsBeneficiaryIds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiary_id', models.CharField(max_length=10, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
            ],
            options={
                'db_table': 'reg_persons_beneficiary_ids',
            },
        ),
        migrations.CreateModel(
            name='RegPersonsAuditTrail',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_type_id', models.CharField(db_index=True, max_length=4, null=True)),
                ('interface_id', models.CharField(db_index=True, max_length=4, null=True)),
                ('date_recorded_paper', models.DateField(null=True)),
                ('timestamp_modified', models.DateTimeField(auto_now=True)),
                ('ip_address', models.GenericIPAddressField()),
                ('meta_data', models.TextField(null=True)),
                ('app_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
                ('person_recorded_paper', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_recorded_paper', to='cpovc_registry.regperson')),
            ],
            options={
                'verbose_name': 'Persons Audit Trail',
                'verbose_name_plural': 'Persons Audit Trails',
                'db_table': 'reg_persons_audit_trail',
            },
        ),
        migrations.CreateModel(
            name='RegOrgUnitsAuditTrail',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_type_id', models.CharField(db_index=True, max_length=4, null=True)),
                ('interface_id', models.CharField(db_index=True, max_length=4, null=True)),
                ('timestamp_modified', models.DateTimeField(auto_now=True)),
                ('ip_address', models.GenericIPAddressField()),
                ('meta_data', models.TextField(null=True)),
                ('app_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('org_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regorgunit')),
            ],
            options={
                'verbose_name': 'Org Units Audit Trail',
                'verbose_name_plural': 'Org Units Audit Trails',
                'db_table': 'reg_org_units_audit_trail',
            },
        ),
        migrations.CreateModel(
            name='RegOrgUnitGeography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_linked', models.DateField(null=True)),
                ('date_delinked', models.DateField(null=True)),
                ('is_void', models.BooleanField(default=False)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_main.setupgeography')),
                ('org_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regorgunit')),
            ],
            options={
                'db_table': 'reg_org_units_geo',
            },
        ),
        migrations.CreateModel(
            name='RegOrgUnitExternalID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier_type_id', models.CharField(max_length=4)),
                ('identifier_value', models.CharField(max_length=255, null=True)),
                ('is_void', models.BooleanField(default=False)),
                ('org_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regorgunit')),
            ],
            options={
                'db_table': 'reg_org_units_external_ids',
            },
        ),
        migrations.CreateModel(
            name='RegOrgUnitContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_detail_type_id', models.CharField(max_length=20)),
                ('contact_detail', models.CharField(max_length=255)),
                ('is_void', models.BooleanField(default=False)),
                ('org_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regorgunit')),
            ],
            options={
                'db_table': 'reg_org_units_contact',
            },
        ),
        migrations.CreateModel(
            name='RegBiometric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left_iris', models.BinaryField()),
                ('right_iris', models.BinaryField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Persons Biometric',
                'verbose_name_plural': 'Persons Biometrics',
                'db_table': 'reg_biometric',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_passport', models.FileField(upload_to='photos/')),
                ('photo_fullsize', models.FileField(null=True, upload_to='photos/')),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('timestamp_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Person Photo',
                'verbose_name_plural': 'Person Photos',
                'db_table': 'reg_person_photo',
            },
        ),
        migrations.CreateModel(
            name='PersonsMaster',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('person_type', models.CharField(max_length=5, null=True)),
                ('system_id', models.CharField(max_length=100, null=True)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
            ],
            options={
                'db_table': 'reg_person_master',
            },
        ),
        migrations.CreateModel(
            name='OVCSibling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('other_names', models.CharField(default=None, max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('sex_id', models.CharField(max_length=4)),
                ('class_level', models.CharField(max_length=4, null=True)),
                ('remarks', models.CharField(max_length=250, null=True)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('timestamp_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
                ('cpims', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ovc_cpims', to='cpovc_registry.regperson')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ovc_sibling', to='cpovc_registry.regperson')),
            ],
            options={
                'db_table': 'ovc_sibling',
            },
        ),
        migrations.CreateModel(
            name='OVCHouseHold',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('members', models.TextField()),
                ('is_void', models.BooleanField(default=False)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('index_child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='index_child', to='cpovc_registry.regperson')),
            ],
            options={
                'db_table': 'reg_household',
            },
        ),
        migrations.CreateModel(
            name='OVCCheckin',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_ovc', models.BooleanField(default=True)),
                ('is_void', models.BooleanField(default=False)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('org_unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regorgunit')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ovc_checkin',
            },
        ),
    ]
