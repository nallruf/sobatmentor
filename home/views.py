# import bcrypt

from django.contrib.auth.hashers import make_password, check_password
import jwt
import datetime
# import bcrypt
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
# from .models import Pengguna, Mentor, Kelas, Kategori, Mentor, Kelas, Kategori, PengalamanKerja, PengalamanMengajar, KontakMentor, skill_mentor, project_mentor, PaketKelas
from .models import *
from django.db.models import Prefetch
from django.utils import timezone

def register_view(request):
    # if login redirect to home
    token = request.COOKIES.get('jwt')
    if token:
        return redirect('home')
    

    if request.method == 'POST':
        nama = request.POST.get('nama')
        username = request.POST.get('username')
        email = request.POST.get('email')
        no_telp = request.POST.get('no_telp')
        sandi = request.POST.get('sandi')
        foto = request.FILES.get('foto')
        role = request.POST.get('role')

        # Hash the password before saving and decode to string
        # hashed_password = bcrypt.hashpw(sandi.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        pengguna = Pengguna(nama=nama, username=username, email=email, no_telp=no_telp, sandi=sandi, foto=foto, role=role)
        pengguna.save()

        return redirect('login')

    return render(request, 'register_z.html')

def login_view(request):
    # if login redirect to home
    token = request.COOKIES.get('jwt')
    if token:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        sandi = request.POST.get('sandi')

        try:
            pengguna = Pengguna.objects.get(username=username)
        except Pengguna.DoesNotExist:
            return HttpResponse('Invalid username or password', status=400)

        # Verifikasi password        if bcrypt.checkpw(sandi.encode('utf-8'), pengguna.sandi.encode('utf-8')):
        # if bcrypt.checkpw(sandi.encode('utf-8'), pengguna.sandi.encode('utf-8')):
        if (sandi == pengguna.sandi):
            # Buat payload JWT
            payload = {
                'id': pengguna.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
            }
            # Encode JWT token
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

            # Set cookie JWT pada respons redirect
            response = redirect('home')  # Ubah 'home_view' dengan nama view setelah login
            response.set_cookie('jwt', token, httponly=True)  # Secure=True jika menggunakan HTTPS
            return response
        else:
            return HttpResponse('Invalid username or password', status=400)

    return render(request, 'login_z.html')

def logout_view(request):
    response = redirect('login')
    response.delete_cookie('jwt')
    return response

def home_view(request):
    token = request.COOKIES.get('jwt')
    if not token:
        return redirect('login')
    
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return redirect('login')
    
    pengguna = Pengguna.objects.get(id=payload['id'])

    total_mentor = Mentor.objects.count()
    total_kelas = Kelas.objects.count()
    list_kategori = Kategori.objects.all()
    top_mentors = Mentor.objects.all()[:3] 
    for mentor in top_mentors:
        # Mengambil salah satu kelas yang diajar oleh mentor
        kelas_mentor = Kelas.objects.filter(mentor=mentor).first()

        # Menambahkan informasi ke dalam instance mentor
        mentor.foto_pengguna = mentor.pengguna.foto  # Asumsikan 'foto' adalah field yang menyimpan URL foto pengguna
        mentor.salah_satu_kelas = kelas_mentor       # Menyimpan objek Kelas sebagai salah satu kelas yang diajar oleh mentor
        mentor.total_kelas = mentor.kelas_set.count()

    content = {
        'pengguna': pengguna,
        'total_mentor': total_mentor,
        'total_kelas': total_kelas,
        'list_kategori': list_kategori,
        'top_mentors': top_mentors,
    }
    return render(request, 'home_z.html', content)
 

def cari_mentor_view(request):
    # Mengambil semua kategori kelas
    list_kategori = Kategori.objects.all()
    
    # Mengambil filter kategori dari parameter URL jika ada
    kategori_id = request.GET.get('kategori')
    nama_mentor = request.GET.get('nama_mentor')

    mentors = Mentor.objects.all()

    if kategori_id:
        mentors = mentors.filter(kelas__kategori_kelas_id=kategori_id).distinct()

    if nama_mentor:
        mentors = mentors.filter(pengguna__nama__icontains=nama_mentor).distinct()

    # Menambahkan informasi tambahan untuk setiap mentor
    for mentor in mentors:
        mentor.foto_pengguna = mentor.pengguna.foto
        mentor.total_kelas = mentor.kelas_set.count()
        # Mengambil semua kategori kelas yang diajar oleh mentor
        mentor.kategori_kelas_list = list(set(kelas.kategori_kelas for kelas in mentor.kelas_set.all()))

    context = {
        'list_kategori': list_kategori,
        'mentors': mentors,
        'selected_kategori': kategori_id,
        'nama_mentor': nama_mentor,
    }
    
    return render(request, 'cari_mentor_z.html', context)

def detail_mentor_view(request, mentor_id):
    mentor = get_object_or_404(Mentor, id=mentor_id)
    kelas_list = Kelas.objects.filter(mentor=mentor)
    pengalaman_kerja_list = PengalamanKerja.objects.filter(mentor=mentor)
    pengalaman_mengajar_list = PengalamanMengajar.objects.filter(mentor=mentor)
    kontak = KontakMentor.objects.get(mentor=mentor)
    skills_list = skill_mentor.objects.filter(mentor=mentor)
    projects_list = project_mentor.objects.filter(mentor=mentor)

    for kelas in kelas_list:
        kelas.jumlah_jadwal = PaketKelas.objects.filter(id_kelas=kelas).count()

    context = {
        'mentor': mentor,
        'kelas_list': kelas_list,
        'pengalaman_kerja_list': pengalaman_kerja_list,
        'pengalaman_mengajar_list': pengalaman_mengajar_list,
        'kontak': kontak,
        'skills_list': skills_list,
        'projects_list': projects_list,
    }

    return render(request, 'detail_mentor_z.html', context)

def detail_kelas_view(request, kelas_id):
    kelas = get_object_or_404(Kelas, id=kelas_id)
    paket_kelas = PaketKelas.objects.filter(id_kelas=kelas)

    context = {
        'kelas': kelas,
        'paket_kelas': paket_kelas,
    }
    return render(request, 'detail_kelas_z.html', context)


def booking_view(request, kelas_id, paket_id):
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

    return render(request, 'booking_z.html', {
        'user': user,
        'kelas': kelas,
        'paket': paket,
        'mentor': mentor,
        'metode_pembayaran': metode_pembayaran
    })

def booking_submit_view(request):
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
        return redirect('success')

def transaksi_success_view(request):
    return render(request, 'success_z.html')

def mentoring_aktip(request):

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

    # Ambil semua transaksi
    # transaksi_list = Transaksi.objects.filter(pengguna=user)
    transaksi_list = Transaksi.objects.filter(pengguna=user).prefetch_related(
        Prefetch('detailtransaksi_set', queryset=DetailTransaksi.objects.select_related(
            'kelas__mentor__pengguna',  # Memuat objek Pengguna mentor
        ))
    )


    context = {
        'transaksi_list': transaksi_list,
    }

    return render(request, 'aktifitas_z.html', context)

def upload_bukti_pembayaran(request, transaksi_id):
    transaksi = get_object_or_404(Transaksi, pk=transaksi_id)

    if request.method == 'POST':
        # Ambil data dari POST request
        bukti_pembayaran_file = request.FILES.get('bukti_pembayaran')

        # Simpan bukti pembayaran ke transaksi
        if bukti_pembayaran_file:
            transaksi.bukti_pembayaran = bukti_pembayaran_file
            transaksi.status = 'lunas'  # Ubah status menjadi lunas setelah upload bukti pembayaran
            transaksi.save()

            messages.success(request, 'Bukti pembayaran berhasil diunggah.')
        
        else:
            messages.error(request, 'Gagal mengunggah bukti pembayaran.')

    # Redirect kembali ke halaman mentoring aktip setelah proses upload
    return redirect('aktifitas')


def index_view(request):
    return render(request, 'index.html')