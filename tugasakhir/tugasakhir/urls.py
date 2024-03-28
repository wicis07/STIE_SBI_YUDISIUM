from django.contrib import admin
from django.urls import path
from mahasiswa.views import *
from django.contrib.auth.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('mahasiswa/', mahasiswa, name='mahasiswa'),
    path('tambah-mahasiswa/', tambah_mahasiswa, name='tambah_mahasiswa'),
    path('mahasiswa/ubah/<int:id_mahasiswa>', ubah_mahasiswa, name='ubah_mahasiswa'),
    path('mahasiswa/hapus/<int:id_mahasiswa>', hapus_mahasiswa, name='hapus_mahasiswa'),
    path('data-upload/', upload, name='data_upload'),
    path('upload/', upload_syarat, name='upload'),
    path('upload/hapus/<int:id_tugasakhir>', hapus_ta, name='hapus_tugasakhir'),
    path('upload/ubah/<int:id_tugasakhir>', ubah_ta, name='ubah_tugasakhir'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)