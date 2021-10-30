from django import forms
from django.forms import ModelForm, widgets
from django import forms
from . models import *

class AktaForm(ModelForm):
    class Meta:
        model = Akta
        fields = [
            'id',
            # DATA KELUARGA
            'no_kk', 'nik_kepala_keluarga',

            # DATA PELAPOR
            'nama_pelapor', 'no_kk_pelapor', 'nik_kepala_keluarga_pelapor', 'nik_pelapor', 'hubungan_keluarga',

            # DATA ANAK
            'nama_anak', 'nik_anak', 'nomor_kk', 'anak_ke', 'tempat_lahir', 'tgl_lahir', 'jam', 'berat_badan', 'tinggi_badan', 'rumah_sakit', 'penolong_kelahiran', 'agama', 'jenis_kelamin', 'jenis_kelahiran', 

            # DATA AYAH
            'nama_ayah', 'nik_ayah',

            # DATA IBU
            'nama_ibu', 'nik_ibu',

            # DATA SAKSI
            'nama_saksi', 'nik_saksi',

            # DOKUMEN
            'akta_nikah', 'surat_kelahiran', 'kk', 'ktp_ayah', 'ktp_ibu', 'ktp_saksi',
        ]
        widgets = {
            # DATA ANAK
            'nama_anak' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'Nama Anak'}),
            'nik_anak' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'NIK Anak'}),
            'nomor_kk' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'Nomor KK'}),
            'anak_ke' : forms.TextInput( attrs={'class':'form-control', 'type':'number', 'min':'1', 'placeholder':'Anak Ke'}),
            'tempat_lahir' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'Tempat Lahir'}),
            'tgl_lahir' : forms.TextInput( attrs={'class':'form-control', 'type':'date'}),
            'jam' : forms.TextInput( attrs={'class':'form-control', 'type':'time'}),
            'berat_badan' : forms.TextInput( attrs={'class':'form-control', 'type':'number', 'placeholder':'Satuan kg', 'min':'1'}),
            'tinggi_badan' : forms.TextInput( attrs={'class':'form-control', 'type':'number', 'placeholder':'Satuan cm', 'min':'1'}),
            'rumah_sakit' : forms.Select( attrs={'class':'form-control'}),
            'penolong_kelahiran' : forms.Select( attrs={'class':'form-control'}),
            'agama' : forms.Select( attrs={'class':'form-control'}),
            'jenis_kelamin' : forms.Select( attrs={'class':'form-control'}),
            'jenis_kelahiran' : forms.Select( attrs={'class':'form-control'}),

            # DATA AYAH
            'nama_ayah' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'Nama Ayah'}),
            'nik_ayah' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'NIK Ayah'}),

            # DATA IBU
            'nama_ibu' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'Nama Ibu'}),
            'nik_ibu' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'NIK Ibu'}),

            # DATA SAKSI
            'nama_saksi' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'Nama Saksi'}),
            'nik_saksi' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'NIK Saksi'}),

            # DATA KELUARGA
            'no_kk' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'Nomor Kartu Keluarga'}),
            'nik_kepala_keluarga' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'NIK Kepala Keluarga'}),

            # DATA PELAPOR
            'nama_pelapor' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'Nama Pelapor'}),
            'no_kk_pelapor' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'Nomor Kartu Keluarga Pelapor'}),
            'nik_kepala_keluarga_pelapor' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'NIK Kepala Keluarga Pelapor'}),
            'nik_pelapor' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'NIK Pelapor'}),
            'hubungan_keluarga' : forms.Select( attrs={'class':'form-control'}),
        }