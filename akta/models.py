from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField
from django.utils.crypto import get_random_string

# Create your models here.

class Akta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    #Data Keluarga
    no_kk = models.CharField(max_length=250, null=True, blank=True)
    nik_kepala_keluarga = models.CharField(max_length=250, null=True, blank=True)

    #Data Pelapor
    nama_pelapor = models.CharField(max_length=250, null=True, blank=True)
    no_kk_pelapor = models.CharField(max_length=250, null=True, blank=True)
    nik_kepala_keluarga_pelapor = models.CharField(max_length=250, null=True, blank=True)
    nik_pelapor = models.CharField(max_length=250, null=True, blank=True)
    hubungan = (
        ('Ayah', 'Ayah'),
        ('Ibu', 'Ibu'),
        ('Lainnya', 'Lainnya'),
    )
    hubungan_keluarga = models.CharField(max_length=250, null=True, choices=hubungan, blank=True)

    #DATA ANAK
    nama_anak = models.CharField(max_length=250, null=True, blank=True)
    nik_anak = models.CharField(max_length=250, null=True, blank=True)
    nomor_kk = models.CharField(max_length=250, null=True, blank=True)
    anak_ke = models.BigIntegerField(null=True, blank=True)
    tempat_lahir = models.CharField(max_length=250, null=True, blank=True)
    tgl_lahir = models.DateField(max_length=250, null=True, blank=True)
    jam = models.TimeField(max_length=250, null=True, blank=True)
    berat_badan = models.BigIntegerField(null=True, blank=True)
    tinggi_badan = models.BigIntegerField(null=True, blank=True)
    rumahsakit = (
        ('Rumah Sakit/Bersalin', 'Rumah Sakit/Bersalin'),
        ('Puskesmas', 'Puskesmas'),
        ('Polindes', 'Polindes'),
        ('Rumah', 'Rumah'),
        ('Lainnya', 'Lainnya'),
    )
    rumah_sakit = models.CharField(max_length=250, null=True, choices=rumahsakit, blank=True)
    penolong = (
        ('Dokter', 'Dokter'),
        ('Bidan/Perawat', 'Bidan/Perawat'),
        ('Lainnya', 'Lainnya'),
    )
    penolong_kelahiran = models.CharField(max_length=250, null=True, choices=penolong, blank=True)
    agama_choices = (
        ('Islam', 'Islam'),
        ('Kristen', 'Kristen'),
        ('Katolik', 'Katolik'),
        ('Hindu', 'Hinhu'),
        ('Budha', 'Budha'),
        ('Konghucu', 'Konghucu'),
    )
    agama = models.CharField(max_length=250, choices=agama_choices, null=True, blank=True)
    jenis_kelamin_choices = (
        ('Laki - Laki', 'Laki - Laki'),
        ('Perempuan', 'Perempuan'),
    )
    jenis_kelamin = models.CharField(max_length=255, choices=jenis_kelamin_choices, null=True, blank=True)
    jenis = (
         ('Tunggal', 'Tunggal'),
         ('Kembar Dua', 'Kembar Dua'),
         ('Kembar Tiga', 'Kembar Tiga'),
         ('Kembar Empat', 'Kembar Empat'),
         ('Kembar Banyak/Lainnya', 'Kembar Banyak/Lainnya'),
    )

    jenis_kelahiran = models.CharField(max_length=250, null=True, choices=jenis, blank=True)

    #DATA AYAH
    nama_ayah = models.CharField(max_length=250, null=True, blank=True)
    nik_ayah = models.CharField(max_length=250, null=True, blank=True)

    # DATA IBU
    nama_ibu = models.CharField(max_length=250, null=True, blank=True)
    nik_ibu = models.CharField(max_length=250, null=True, blank=True)

    #DATA SAKSI
    nama_saksi = models.CharField(max_length=250, null=True, blank=True)
    nik_saksi = models.CharField(max_length=250, null=True, blank=True)

    #DOKUMEN
    akta_nikah = CloudinaryField(null=True, blank=True)
    surat_kelahiran = CloudinaryField(null=True, blank=True)
    kk = CloudinaryField(null=True, blank=True)
    ktp_ayah = CloudinaryField(null=True, blank=True)
    ktp_ibu = CloudinaryField(null=True, blank=True)
    ktp_saksi = CloudinaryField(null=True, blank=True)

    status_choices = (
        ('data ditunggu', 'data ditunggu'),
        ('data disetujui', 'data disetujui'),
        ('data ditolak', 'data ditolak'),
    )
    status = models.CharField(max_length=250, null=True, default='data ditunggu', choices=status_choices, blank=True)

    def save(self, *args, **kwargs):
        super(Akta, self).save(*args, **kwargs)
        self.slug = get_random_string(10, '0123456789')
        super().save()