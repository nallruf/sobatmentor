from django.urls import path
# from .views import register_view, login_view, home_view , logout_view, index_view, cari_mentor_view, detail_kelas_view, detail_mentor_view
from .views import *


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    # path('', index_view, name='home'),
    path('mentor/', cari_mentor_view , name='cari_mentor'),
    path('mentor/<int:mentor_id>/', detail_mentor_view, name='detail_mentor'),
    path('kelas/<int:kelas_id>/', detail_kelas_view, name='detail_kelas'),
    path('booking/<int:kelas_id>/<int:paket_id>/', booking_view, name='booking'),
    path('success/', transaksi_success_view, name='success'),
    path('aktifitas/', mentoring_aktip, name='aktifitas'),
    path('upload-bukti-pembayaran/<int:transaksi_id>/', upload_bukti_pembayaran, name='upload_bukti_pembayaran'),
    path('submit-booking/', booking_submit_view, name='submit_booking'),


]