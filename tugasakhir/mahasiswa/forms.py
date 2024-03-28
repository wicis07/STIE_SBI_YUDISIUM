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
        fields = [
            'mahasiswa_id',
            'judul',
            'acc_ujian',
            'bebas_teori',
            'krs',
            'cek_plagiasi',
            'file_tugas_akhir',
            'sk_diterima',
            'sk_selesai',
            'lembar_penilaian',
            'kepemilikan_usaha',
            'bukti_mou_spk',
            'ijazah_terakhir',
            'akte_kelahiran',
            'ktp_kk',
            'foto',
            ]
        
        labels = {
            'mahasiswa_id': ('NAMA MAHASISWA '),
            'judul': ('JUDUL TUGAS AKHIR '),
            'acc_ujian': ('BUKTI ACC UJIAN SIDANG '),
            'bebas_teori': ('BUKTI BEBAS TEORI DARI DOSEN PEMBIMBING AKADEMIK '),
            'krs': ('BUKTI KRS PADA SEMESTER BERJALAN '),
            'cek_plagiasi': ('BUKTI HASIL CEK PLAGIASI '),
            'file_tugas_akhir': ('SOFT FILE TUGAS AKHIR '),
            'sk_diterima': ('SURAT KETERANGAN DITERIMA DARI TEMPAT TUGAS AKHIR '),
            'sk_selesai': ('SURAT KETERANGAN SELESAI DARI TEMPAT TUGAS AKHIR '),
            'lembar_penilaian': ('LEMBAR PENILAIAN (KHUSUS TAM) '),
            'kepemilikan_usaha': ('BUKTI KEPEMILIKAN USAHA (KHUSUS TAW) '),
            'bukti_mou_spk': ('BUKTI MoU ATAU SPK '),
            'ijazah_terakhir': ('BUKTI UJAZAH TERAKHIR '),
            'akte_kelahiran': ('BUKTI AKTE KELAHIRAN '),
            'ktp_kk': ('BUKTI KTP ATAU KK '),
            'foto': ('PAS FOTO HITAM PUTIH (2X3) '),
        }
        
        widgets = {
            'mahasiswa_id': forms.Select({'class':'form-control'}),
            'judul': forms.TextInput({'class':'form-control'}),
            'acc_ujian': forms.FileInput({'class':'form-control'}),
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