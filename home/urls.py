from django.urls import path
from .views import *


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('register/status/', status_register_view, name='statusregister'),

    path('', beranda_view, name='beranda'),
    path('carimentor/', cari_mentor_view, name='carimentor'),
    path('carimentor/<int:mentor_id>/', detail_mentor_view, name='detailmentor'),
    path('mentor/detailkelas/<int:kelas_id>/', detail_kelas_view, name='detailkelas'),

    path('transaksi/<int:kelas_id>/<int:paket_id>/', transaksi_mentor_view, name='transaksi'),
    path('submit-transaksi/', transaksi_submit_view, name='submittransaksi'),
    path('submit-transaksi/success/', transaksi_success_view, name='transaksisuccess'),

    path('aktivitas/', aktivitas_view, name='aktivitas'),
    path('aktivitas/upload-bukti-pembayaran/<int:transaksi_id>/', upload_bukti_pembayaran, name='upload_bukti_pembayaran'),
    path('aktivitas/success/', aktivitas_success_view, name='aktivitassuccess'),
    path('aktivitas/nilai/<int:kelas_id>/', set_nilai, name='nilai'),
    path('aktivitas/nilai/success/', nilai_success_view, name='nilaisuccess'),
]