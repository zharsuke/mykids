# Generated by Django 3.2.4 on 2021-10-30 17:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('akta', '0018_auto_20211031_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='akta',
            name='agama',
        ),
        migrations.RemoveField(
            model_name='akta',
            name='akta_nikah',
        ),
        migrations.RemoveField(
            model_name='akta',
            name='jam',
        ),
        migrations.RemoveField(
            model_name='akta',
            name='kk',
        ),
        migrations.RemoveField(
            model_name='akta',
            name='nik_anak',
        ),
        migrations.RemoveField(
            model_name='akta',
            name='nomor_kk',
        ),
        migrations.RemoveField(
            model_name='akta',
            name='tgl_lahir',
        ),
        migrations.AddField(
            model_name='akta',
            name='akta_kawin_ortu',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='akta',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='akta',
            name='kk_ortu',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='akta',
            name='pukul',
            field=models.TimeField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='tanggal_lahir',
            field=models.DateField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='anak_ke',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='berat_badan',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='hubungan_keluarga',
            field=models.CharField(choices=[('Ayah', 'Ayah'), ('Ibu', 'Ibu'), ('Lainnya', 'Lainnya')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='jenis_kelahiran',
            field=models.CharField(choices=[('Tunggal', 'Tunggal'), ('Kembar Dua', 'Kembar Dua'), ('Kembar Tiga', 'Kembar Tiga'), ('Kembar Empat', 'Kembar Empat'), ('Kembar Banyak/Lainnya', 'Kembar Banyak/Lainnya')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='jenis_kelamin',
            field=models.CharField(choices=[('Laki-Laki', 'Laki-Laki'), ('Perempuan', 'Perempuan')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='ktp_ayah',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='akta',
            name='ktp_ibu',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='akta',
            name='ktp_saksi',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='akta',
            name='nama_anak',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='nama_ayah',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='nama_ibu',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='nama_pelapor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='nama_saksi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='nik_ayah',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='nik_ibu',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='nik_kepala_keluarga',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='nik_kepala_keluarga_pelapor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='nik_pelapor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='nik_saksi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='no_kk',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='no_kk_pelapor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='penolong_kelahiran',
            field=models.CharField(choices=[('Dokter', 'Dokter'), ('Bidan/Perawat', 'Bidan/Perawat'), ('Lainnya', 'Lainnya')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='rumah_sakit',
            field=models.CharField(choices=[('Rumah Sakit/Bersalin', 'Rumah Sakit/Bersalin'), ('Puskesmas', 'Puskesmas'), ('Polindes', 'Polindes'), ('Rumah', 'Rumah'), ('Lainnya', 'Lainnya')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='status',
            field=models.CharField(choices=[('Data Waiting', 'Data Waiting'), ('Data Confirmed', 'Data Confirmed'), ('Data Rejected', 'Data Rejected')], default='Data Waiting', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='surat_kelahiran',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='akta',
            name='tempat_lahir',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='tinggi_badan',
            field=models.CharField(max_length=100, null=True),
        ),
    ]