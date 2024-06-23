# import bcrypt

from django.contrib.auth.hashers import make_password, check_password
import jwt
import datetime
# import bcrypt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .models import Pengguna, Mentor, Kelas, Kategori

def register_view(request):
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

    return render(request, 'register.html')

def login_view(request):
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

    return render(request, 'login.html')

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


    return render(request, 'home.html', content)

def index_view(request):
    return render(request, 'index.html')