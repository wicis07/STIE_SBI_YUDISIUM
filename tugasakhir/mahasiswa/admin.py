from django.contrib import admin
from mahasiswa.models import Mahasiswa, Tugasakhir

class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ['nim', 'nama', 'jurusan', 'tahun']
    search_fields = ['nim', 'nama', 'jurusan', 'tahun']
    list_per_page = 4
    
class UploadTA(admin.ModelAdmin):
    list_display = ['mahasiswa_id','judul', 'acc_ujian', 'bebas_teori', 'krs', 'cek_plagiasi', 'file_tugas_akhir', 'sk_diterima', 'sk_selesai', 'lembar_penilaian', 'kepemilikan_usaha', 'bukti_mou_spk', 'ijazah_terakhir', 'akte_kelahiran', 'ktp_kk', 'foto']
    search_fields = ['judul']
    list_per_page = 4

admin.site.register(Mahasiswa, MahasiswaAdmin)
admin.site.register(Tugasakhir, UploadTA)
