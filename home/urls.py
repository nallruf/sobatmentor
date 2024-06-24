from django.urls import path
# from .views import register_view, status_register_view, login_view, home_view , logout_view, beranda_view, cari_mentor_view, detail_mentor_view, status_transaksi_view, transaksi_view, detail_kelas_view, aktivitas_view, cari_mentor_view, detail_kelas_view, detail_mentor_view
from .views import *


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
    # path('', index_view, name='home'),

    # path('mentor/<int:mentor_id>/', detail_mentor_view, name='detail_mentor'),
    path('kelas/<int:kelas_id>/', detail_kelas_view, name='detail_kelas'),
    path('booking/<int:kelas_id>/<int:paket_id>/', booking_view, name='booking'),
    path('success/', transaksi_success_view, name='success'),
    path('aktifitas/', mentoring_aktip, name='aktifitas'),
    path('upload-bukti-pembayaran/<int:transaksi_id>/', upload_bukti_pembayaran, name='upload_bukti_pembayaran'),
    path('submit-booking/', booking_submit_view, name='submit_booking'),
]