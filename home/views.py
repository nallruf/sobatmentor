# import bcrypt

from django.contrib.auth.hashers import make_password, check_password
import jwt
import datetime
import bcrypt
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from .models import *
from django.db.models import Prefetch
from django.utils import timezone

def login_view(request):
    token = request.COOKIES.get('jwt')
    if token:
        return redirect('beranda')

    if request.method == 'POST':
        username = request.POST.get('username')
        sandi = request.POST.get('sandi')

        try:
            pengguna = Pengguna.objects.get(username=username)
        except Pengguna.DoesNotExist:
            return redirect('login')
        
        if bcrypt.checkpw(sandi.encode('utf-8'), pengguna.sandi.encode('utf-8')):
            payload = {
                'id': pengguna.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
            }
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

            response = redirect('beranda')
            response.set_cookie('jwt', token, httponly=True) 
            return response
        else:
            return redirect('login')
        
    context = {
        'page_title': 'Login'
    }
    return render(request, 'login.html', context)

def logout_view(request):
    response = redirect('login')
    response.delete_cookie('jwt')
    return response

def register_view(request):
    token = request.COOKIES.get('jwt')
    if token:
        return redirect('beranda')
    
    if request.method == 'POST':
        nama_pengguna = request.POST.get('nama')
        username = request.POST.get('username')
        email = request.POST.get('email')
        no_telp = request.POST.get('no_telp')
        sandi = request.POST.get('sandi')
        role = "user"

        if nama_pengguna and username and email and no_telp and sandi:
            if Pengguna.objects.filter(email=email).exists():
                return render(request, 'register.html', {'error': 'Email sudah digunakan'})
            
            hashed_password = bcrypt.hashpw(sandi.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            pengguna = Pengguna(nama=nama_pengguna, username=username, email=email, no_telp=no_telp, sandi=hashed_password, role=role)
            pengguna.save()
            return redirect('statusregister')
    
    context = {
        'page_title': 'Register'
    }
    return render(request, 'register.html', context)

def status_register_view(request):
    context = {
        'page_title': 'Status Register'
    }
    return render(request, 'status_register.html', context)

def beranda_view(request):
    token = request.COOKIES.get('jwt')
    pengguna = None

    if token:
        try:
            if isinstance(token, str):
                token = token.encode('utf-8')
            
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            pengguna = Pengguna.objects.get(id=payload['id'])
        except jwt.ExpiredSignatureError:
            return redirect('login')
        except jwt.InvalidTokenError:
            return redirect('login')

    total_mentor = Mentor.objects.count()
    total_kelas = Kelas.objects.count()
    list_kategori = Kategori.objects.all()
    top_mentors = Mentor.objects.all()[:3]
    for mentor in top_mentors:
        kelas_mentor = Kelas.objects.filter(mentor=mentor).first()
        mentor.foto_pengguna = mentor.pengguna.foto 
        mentor.salah_satu_kelas = kelas_mentor 
        mentor.total_kelas = mentor.kelas_set.count()

    context = {
        'pengguna': pengguna,
        'total_mentor': total_mentor,
        'total_kelas': total_kelas,
        'list_kategori': list_kategori,
        'top_mentors': top_mentors,
        'page_title': 'Home',
        
    }

    return render(request, 'beranda.html', context)

def cari_mentor_view(request):
    token = request.COOKIES.get('jwt')
    pengguna = None

    if token:
        try:
            if isinstance(token, str):
                token = token.encode('utf-8')
            
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            pengguna = Pengguna.objects.get(id=payload['id'])
        except jwt.ExpiredSignatureError:
            return redirect('login')
        except jwt.InvalidTokenError:
            return redirect('login')
        
    list_kategori = Kategori.objects.all()
    kategori_id = request.GET.get('kategori')
    nama_mentor = request.GET.get('nama_mentor')
    mentors = Mentor.objects.all()

    if kategori_id:
        mentors = mentors.filter(kelas__kategori_kelas_id=kategori_id).distinct()

    if nama_mentor:
        mentors = mentors.filter(pengguna__nama__icontains=nama_mentor).distinct()
    
    for mentor in mentors:
        mentor.foto_pengguna = mentor.pengguna.foto
        mentor.total_kelas = mentor.kelas_set.count()
        mentor.kategori_kelas_list = list(set(kelas.kategori_kelas for kelas in mentor.kelas_set.all()))

    context = {
        'pengguna': pengguna,
        'list_kategori': list_kategori,
        'mentors': mentors,
        'selected_kategori': kategori_id,
        'nama_mentor': nama_mentor,
        'page_title': 'Cari Mentor'
    }
    
    return render(request, 'cari_mentor.html', context)

def detail_mentor_view(request, mentor_id):
    token = request.COOKIES.get('jwt')
    if not token:
        return redirect('login')
    
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return redirect('login')
    
    pengguna = Pengguna.objects.get(id=payload['id'])
    mentor = get_object_or_404(Mentor, id=mentor_id)
    kelas_list = Kelas.objects.filter(mentor=mentor)
    pengalaman_kerja_list = PengalamanKerja.objects.filter(mentor=mentor)
    pengalaman_mengajar_list = PengalamanMengajar.objects.filter(mentor=mentor)
    pengalaman_organisasi_list = PengalamanOrganisasi.objects.filter(mentor=mentor)
    kontak = KontakMentor.objects.get(mentor=mentor)
    skills_list = skill_mentor.objects.filter(mentor=mentor)
    projects_list = project_mentor.objects.filter(mentor=mentor)
    penilaian_list = Penilaian.objects.filter(kelas__mentor=mentor)[:1]

    for kelas in kelas_list:
        kelas.jumlah_jadwal = PaketKelas.objects.filter(id_kelas=kelas).count()

    context = {
        'mentor': mentor,
        'kelas_list': kelas_list,
        'pengalaman_kerja_list': pengalaman_kerja_list,
        'pengalaman_mengajar_list': pengalaman_mengajar_list,
        'pengalaman_organisasi_list': pengalaman_organisasi_list,
        'kontak': kontak,
        'skills_list': skills_list,
        'projects_list': projects_list,
        'penilaian_list': penilaian_list,
        'pengguna': pengguna,
        'page_title': 'Detail Mentor'
    }

    return render(request, 'detail_mentor.html', context)

def detail_kelas_view(request, kelas_id):
    token = request.COOKIES.get('jwt')
    if not token:
        return redirect('login')
    
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return redirect('login')
    
    pengguna = Pengguna.objects.get(id=payload['id'])
    kelas = get_object_or_404(Kelas, id=kelas_id)
    paket_kelas = PaketKelas.objects.filter(id_kelas=kelas)

    context = {
        'kelas': kelas,
        'pengguna': pengguna,
        'paket_kelas': paket_kelas,
        'page_title': 'Detail Kelas'
    }
    return render(request, 'detail_kelas.html', context)

def transaksi_mentor_view(request, kelas_id, paket_id):
    token = request.COOKIES.get('jwt')
    if not token:
        return redirect('login')
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return redirect('login')
    except jwt.InvalidTokenError:
        return HttpResponse('Invalid token', status=400)

    user = Pengguna.objects.get(id=payload['id'])
    kelas = Kelas.objects.get(id=kelas_id)
    paket = PaketKelas.objects.get(id=paket_id)
    mentor = kelas.mentor
    metode_pembayaran = mentor.metode_pembayaran

    context = {
        'user': user,
        'pengguna': user,
        'kelas': kelas,
        'paket': paket,
        'mentor': mentor,
        'metode_pembayaran': metode_pembayaran,
        'page_title': 'Transaksi'
    }

    return render(request, 'transaksi.html', context)

def transaksi_submit_view(request):
    token = request.COOKIES.get('jwt')
    if not token:
        return redirect('login')
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return redirect('login')
    except jwt.InvalidTokenError:
        return HttpResponse('Invalid token', status=400)
    
    kelas_id = request.POST.get('kelas_id')
    paket_id = request.POST.get('paket_id')
    user = Pengguna.objects.get(id=payload['id'])
    kelas = Kelas.objects.get(id=kelas_id)
    paket = PaketKelas.objects.get(id=paket_id)
    mentor = kelas.mentor
    metode_pembayaran = mentor.metode_pembayaran

    if request.method == "POST":
        alamat = request.POST.get('alamat')
        transaksi = Transaksi.objects.create(
            tgl_transaksi=timezone.now(),
            pengguna=user,
            metode_pembayaran=metode_pembayaran,
            alamat=alamat,
            status='menunggu'
        )
        DetailTransaksi.objects.create(
            transaksi=transaksi,
            kelas=kelas,
            tipe_kelas=kelas.tipe_kelas,
            paket_kelas=paket,
            biaya_kelas=paket.harga_kelas
        )
        return redirect('transaksisuccess')

def transaksi_success_view(request):
    context = {
        'page_title': 'Status Transaksi'
    }

    return render(request, 'status_transaksi.html', context)

def aktivitas_view(request):
    token = request.COOKIES.get('jwt')
    if not token:
        return redirect('login')
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return redirect('login')
    except jwt.InvalidTokenError:
        return HttpResponse('Invalid token', status=400)
    
    user = Pengguna.objects.get(id=payload['id'])
   
    transaksi_list = Transaksi.objects.filter(pengguna=user).prefetch_related(
        Prefetch('detailtransaksi_set', queryset=DetailTransaksi.objects.select_related(
            'kelas__mentor__pengguna',  # Memuat objek Pengguna mentor
        ))
    
    )
    
    transaksi_selected = None
    transaksi_selected_id = None
    detail_transaksi_id = None
    penilaian_list = None
    penilaian_user = None
    penilaian_final = None
    kelas_id = None

    transaksi_id = request.GET.get('transaksi')

    if transaksi_id:
        transaksi_selected = transaksi_list.filter(id=transaksi_id)
        transaksi_selected_id = transaksi_list.filter(id=transaksi_id).first()
        detail_transaksi_id = DetailTransaksi.objects.filter(id=transaksi_selected_id.id).first()
        kelas_id = Kelas.objects.filter(id=detail_transaksi_id.kelas_id).first()
        # kelas_id = detail_transaksi_id.kelas_id

    # penilaian_list = Penilaian.objects.filter(pengguna=user, kelas=kelas_id)

    print(kelas_id)
    if kelas_id:
        penilaian_list = Penilaian.objects.all()    
        # print(f'Penilaian List1: {penilaian_list}') 
        penilaian_user = Penilaian.objects.filter(pengguna=user.id)
        # print(f'Penilaian List2: {penilaian_user}') 
        penilaian_final = penilaian_user.filter(kelas_id=kelas_id.id).first()
        # print(f'Penilaian List3: {penilaian_final}') 

    context = {
        'transaksi_selected_id': transaksi_selected_id,
        'transaksi_selected': transaksi_selected,
        'transaksi_list': transaksi_list,
        'penilaian_list': penilaian_final,
        'pengguna': user,
        'page_title': 'Aktivitas'
    }


    return render(request, 'aktivitas.html', context)

def upload_bukti_pembayaran(request, transaksi_id):
    transaksi = get_object_or_404(Transaksi, pk=transaksi_id)

    if request.method == 'POST':
        bukti_pembayaran_file = request.FILES.get('bukti_pembayaran')

        if bukti_pembayaran_file:
            transaksi.bukti_pembayaran = bukti_pembayaran_file
            transaksi.status = 'lunas'
            transaksi.save()

            messages.success(request, 'Bukti pembayaran berhasil diunggah.')
        
        else:
            messages.error(request, 'Gagal mengunggah bukti pembayaran.')

    return redirect('aktivitassuccess')

def set_nilai(request, kelas_id):
    token = request.COOKIES.get('jwt')
    if not token:
        return redirect('login')
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return redirect('login')
    except jwt.InvalidTokenError:
        return HttpResponse('Invalid token', status=400)

    user = Pengguna.objects.get(id=payload['id'])
    kelas = Kelas.objects.get(id=kelas_id)
    mentor = kelas.mentor

    if request.method == 'POST':
        penilaian = request.POST.get('penilaian')
        komentar = request.POST.get('komentar')

        Penilaian.objects.create(
            kelas=kelas,
            pengguna=user,
            penilaian=penilaian,
            komentar=komentar
        )

        return redirect('nilaisuccess')

def aktivitas_success_view(request):
    context = {
        'page_title': 'Upload Pembayaran Transaksi'
    }

    return render(request, 'status_upload.html', context)

def nilai_success_view(request):
    context = {
        'page_title': 'Penilaian Kelas'
    }

    return render(request, 'status_penilaian.html', context)

