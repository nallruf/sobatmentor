from django.urls import path
from .views import register_view, status_register_view, login_view, home_view , logout_view, beranda_view, cari_mentor_view, detail_mentor_view, status_transaksi_view, transaksi_view, detail_kelas_view, aktivitas_view

urlpatterns = [
    path('', beranda_view, name='beranda'),
    path('carimentor/', cari_mentor_view, name='carimentor'),
    path('carimentor/detailmentor/', detail_mentor_view, name='detailmentor'),
    path('carimentor/detailmentor/detailkelas', detail_kelas_view, name='detailkelas'),
    path('transaksi/', transaksi_view, name='transaksi'),
    path('transaksi/status/', status_transaksi_view, name='statustransaksi'),
    path('aktivitas/', aktivitas_view, name='aktivitas'),
    
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('register/status/', status_register_view, name='statusregister'),
    path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
]