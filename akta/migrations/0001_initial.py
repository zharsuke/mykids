# Generated by Django 3.2.4 on 2021-10-31 10:00

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Akta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('no_kk', models.CharField(blank=True, max_length=250, null=True)),
                ('nik_kepala_keluarga', models.CharField(blank=True, max_length=250, null=True)),
                ('nama_pelapor', models.CharField(blank=True, max_length=250, null=True)),
                ('no_kk_pelapor', models.CharField(blank=True, max_length=250, null=True)),
                ('nik_kepala_keluarga_pelapor', models.CharField(blank=True, max_length=250, null=True)),
                ('nik_pelapor', models.CharField(blank=True, max_length=250, null=True)),
                ('hubungan_keluarga', models.CharField(blank=True, choices=[('Ayah', 'Ayah'), ('Ibu', 'Ibu'), ('Lainnya', 'Lainnya')], max_length=250, null=True)),
                ('nama_anak', models.CharField(blank=True, max_length=250, null=True)),
                ('nik_anak', models.CharField(blank=True, max_length=250, null=True)),
                ('nomor_kk', models.CharField(blank=True, max_length=250, null=True)),
                ('anak_ke', models.BigIntegerField(blank=True, null=True)),
                ('tempat_lahir', models.CharField(blank=True, max_length=250, null=True)),
                ('tgl_lahir', models.DateField(blank=True, max_length=250, null=True)),
                ('jam', models.TimeField(blank=True, max_length=250, null=True)),
                ('rumah_sakit', models.CharField(blank=True, choices=[('Rumah Sakit/Bersalin', 'Rumah Sakit/Bersalin'), ('Puskesmas', 'Puskesmas'), ('Polindes', 'Polindes'), ('Rumah', 'Rumah'), ('Lainnya', 'Lainnya')], max_length=250, null=True)),
                ('penolong_kelahiran', models.CharField(blank=True, choices=[('Dokter', 'Dokter'), ('Bidan/Perawat', 'Bidan/Perawat'), ('Lainnya', 'Lainnya')], max_length=250, null=True)),
                ('agama', models.CharField(blank=True, choices=[('Islam', 'Islam'), ('Kristen', 'Kristen'), ('Katolik', 'Katolik'), ('Hindu', 'Hinhu'), ('Budha', 'Budha'), ('Konghucu', 'Konghucu')], max_length=250, null=True)),
                ('jenis_kelamin', models.CharField(blank=True, choices=[('Laki - Laki', 'Laki - Laki'), ('Perempuan', 'Perempuan')], max_length=255, null=True)),
                ('jenis_kelahiran', models.CharField(blank=True, choices=[('Tunggal', 'Tunggal'), ('Kembar Dua', 'Kembar Dua'), ('Kembar Tiga', 'Kembar Tiga'), ('Kembar Empat', 'Kembar Empat'), ('Kembar Banyak/Lainnya', 'Kembar Banyak/Lainnya')], max_length=250, null=True)),
                ('nama_ayah', models.CharField(blank=True, max_length=250, null=True)),
                ('nik_ayah', models.CharField(blank=True, max_length=250, null=True)),
                ('nama_ibu', models.CharField(blank=True, max_length=250, null=True)),
                ('nik_ibu', models.CharField(blank=True, max_length=250, null=True)),
                ('nama_saksi', models.CharField(blank=True, max_length=250, null=True)),
                ('nik_saksi', models.CharField(blank=True, max_length=250, null=True)),
                ('akta_nikah', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('surat_kelahiran', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('kk', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('ktp_ayah', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('ktp_ibu', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('ktp_saksi', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, choices=[('data ditunggu', 'data ditunggu'), ('data disetujui', 'data disetujui'), ('data ditolak', 'data ditolak')], default='data ditunggu', max_length=250, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
