from django.contrib import admin
from django.urls import path
from mahasiswa.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mahasiswa/', mahasiswa, name='mahasiswa'),
    path('upload/', upload_syarat, name='upload'),
    path('tambah-mahasiswa/', tambah_mahasiswa, name='tambah_buku'),
    path('mahasiswa/ubah/<int:id_mahasiswa>', ubah_mahasiswa, name='ubah_mahasiswa'),
    path('mahasiswa/hapus/<int:id_mahasiswa>', hapus_mahasiswa, name='hapus_mahasiswa'),
]
