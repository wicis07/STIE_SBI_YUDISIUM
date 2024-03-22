from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
    nim = models.CharField(max_length=15)
    nama = models.CharField(max_length=50)
    jurusan = models.CharField(max_length=40)
    tahun = models.IntegerField(null=True)
    
def __str__(self):
    return self.nim

class Tugasakhir(models.Model):
    judul = models.CharField(max_length=50)
    acc_ujian = models.ImageField(upload_to='bukti_acc_ujian/', null=True)
    bebas_teori = models.ImageField(upload_to='bukti_bebas_teori/', null=True)
    krs = models.ImageField(upload_to='bukti_krs/', null=True)
    cek_plagiasi = models.ImageField(upload_to='bukti_hasil_cek-plagiasi/', null=True)
    file_tugas_akhir = models.ImageField(upload_to='file_tugas_akhir/', null=True)
    sk_diterima = models.ImageField(upload_to='sk_diterima/', null=True)
    sk_selesai = models.ImageField(upload_to='sk_selesai/', null=True)
    lembar_penilaian = models.ImageField(upload_to='lembar_penilian/', null=True)
    kepemilikan_usaha = models.ImageField(upload_to='bukti_usaha/', null=True)
    bukti_mou_spk = models.ImageField(upload_to='bukti_mou_spk/', null=True)
    ijazah_terakhir = models.ImageField(upload_to='bukti_ijazah_terakhir/', null=True)
    akte_kelahiran = models.ImageField(upload_to='bukti_akte_kelahiran/', null=True)
    ktp_kk = models.ImageField(upload_to='bukti_ktp_kk/', null=True)
    foto = models.ImageField(upload_to='pas_foto/', null=True)
    tanggal = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.judul
    