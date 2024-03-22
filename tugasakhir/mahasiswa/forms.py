from django.forms import ModelForm
from mahasiswa.models import *
from django import forms

class FormMahasiswa(ModelForm):
    class Meta:
        model = Mahasiswa
        fields = '__all__'
        
        widgets = {
            'nim': forms.TextInput({'class':'form-control'}),
            'nama': forms.TextInput({'class':'form-control'}),
            'jurusan': forms.TextInput({'class':'form-control'}),
            'tahun': forms.TextInput({'class':'form-control'}),
        }
        
class FormUpload(ModelForm):
    class Meta:
        model = Tugasakhir
        fields = '__all__'
        
        
        widgets = {
            'judul': forms.TextInput({'class':'form-control','name':"Judul Tugas Akhir"}),
            'acc_ujian': forms.FileInput({'class':'form-control','label':'Judul Tugas Akhir'}),
            'bebas_teori': forms.FileInput({'class':'form-control'}),
            'krs': forms.FileInput({'class':'form-control'}),
            'cek_plagiasi': forms.FileInput({'class':'form-control'}),
            'file_tugas_akhir': forms.FileInput({'class':'form-control'}),
            'sk_diterima': forms.FileInput({'class':'form-control'}),
            'sk_selesai': forms.FileInput({'class':'form-control'}),
            'lembar_penilaian': forms.FileInput({'class':'form-control'}),
            'kepemilikan_usaha': forms.FileInput({'class':'form-control'}),
            'bukti_mou_spk': forms.FileInput({'class':'form-control'}),
            'ijazah_terakhir': forms.FileInput({'class':'form-control'}),
            'akte_kelahiran': forms.FileInput({'class':'form-control'}),
            'ktp_kk': forms.FileInput({'class':'form-control'}),
            'foto': forms.FileInput({'class':'form-control'}),
            
        }