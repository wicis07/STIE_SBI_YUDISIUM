from django.shortcuts import render, redirect
from mahasiswa.models import *
from mahasiswa.forms import *
from django.contrib import messages

def mahasiswa(request):
    mhs = Mahasiswa.objects.all()
    context = {
        'mhs':mhs
    }
    return render(request, 'mahasiswa.html', context)

def upload(request):
    ta = Tugasakhir.objects.all()
    context = {
        'ta':ta
    }
    return render(request, 'data-upload.html', context)

def tambah_mahasiswa(request):
    if request.POST:
        form = FormMahasiswa(request.POST)
        if form.is_valid():
            form.save()
            message = "Data berhasil disimpan!"
            form = FormMahasiswa()
            
            context = {
                'form':form,
                'message':message,
            }
            return render(request, 'tambah-mahasiswa.html', context)
    else:
        form = FormMahasiswa()
        
        context = {
            'form':form
        }
    
    return render(request, 'tambah-mahasiswa.html', context)

def ubah_mahasiswa(request, id_mahasiswa):
    mahasiswa = Mahasiswa.objects.get(id=id_mahasiswa)
    template = 'ubah-mahasiswa.html'
    if request.POST:
        form = FormMahasiswa(request.POST, instance=mahasiswa)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diubah!")
            return redirect('ubah_mahasiswa', id_mahasiswa=id_mahasiswa)
    else:
        form = FormMahasiswa(instance=mahasiswa)
        context = {
            'form':form,
            'mahasiswa':mahasiswa,
        }
    return render(request, template, context)

def hapus_mahasiswa(request, id_mahasiswa):
    mahasiswa = Mahasiswa.objects.filter(id=id_mahasiswa)
    mahasiswa.delete()
    
    return redirect('mahasiswa')

def upload_syarat(request):
    if request.POST:
        form = FormUpload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Data berhasil disimpan!"
            form = FormUpload()
            
            context = {
                'form':form,
                'message':message,
            }
            return render(request, 'upload.html', context)
    else:
        form = FormUpload()
        
        context = {
            'form':form
        }
    
    return render(request, 'upload.html', context)