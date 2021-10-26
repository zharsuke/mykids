from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField
from django.db.models.fields import CharField
# Create your models here.

class Akta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #DATA ANAK
    nama_anak = models.CharField(max_length=250, null=True)
    nik_anak = models.CharField(max_length=250, null=True)
    nomor_kk = models.CharField(max_length=250, null=True)
    tempat_lahir = models.CharField(max_length=250, null=True)
    tgl_lahir = models.DateField(null=True)
    jam = models.TimeField(null=True)
    berat_badan = models.CharField(max_length=250, null=True)
    tinggi_badan = models.CharField(max_length=350, null=True)
    anak_ke = models.IntegerField(null=True)
    rumah_sakit = models.CharField(max_length=250, null=True)
    agama_choices = (
        ('Islam', 'Islam'),
        ('Kristen', 'Kristen'),
        ('Katolik', 'Katolik'),
        ('Hindu', 'Hinhu'),
        ('Budha', 'Budha'),
        ('Konghucu', 'Konghucu'),
    )
    agama = models.CharField(max_length=250, choices=agama_choices, null=True)
    jenis_kelamin_choices = (
        ('Pria', 'Pria'),
        ('Wanita', 'Wanita'),
    )
    jenis_kelamin = models.CharField(max_length=255, choices=jenis_kelamin_choices, null=True)

    #DATA AYAH
    nama_ayah = models.CharField(max_length=250, null=True)
    nik_ayah = models.CharField(max_length=250, null=True)

    # DATA IBU
    nama_ibu = models.CharField(max_length=250, null=True)
    nik_ibu = models.CharField(max_length=250, null=True)

    #DATA SAKSI
    nama_saksi = models.CharField(max_length=250, null=True)
    nik_saksi = models.CharField(max_length=250, null=True)

    #DOKUMEN
    akta_nikah = CloudinaryField(null=True)
    kk = CloudinaryField(null=True)
    ktp_ayah = CloudinaryField(null=True)
    ktp_ibu = CloudinaryField(null=True)
    ktp_saksi = CloudinaryField(null=True)


    def save(self, *args, **kwargs):
        super(Akta, self).save(*args, **kwargs)
        super().save()