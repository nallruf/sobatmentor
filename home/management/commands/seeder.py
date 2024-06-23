from django.core.management.base import BaseCommand
from home.models import Pengguna, Mentor, Kategori, Kelas, PaketKelas, Transaksi, DetailTransaksi, MetodePembayaran, Penilaian, PengalamanKerja, PengalamanMengajar, PengalamanOrganisasi, BerkasMentor, KontakMentor
from datetime import datetime

class Command(BaseCommand):
    help = 'Seed database with initial data'

    def handle(self, *args, **options):
        self.seed_pengguna()
        self.seed_mentor()
        self.seed_kategori()
        self.seed_metode_pembayaran()
        self.seed_kelas()
        self.seed_paket_kelas()
        self.seed_transaksi()
        self.seed_detail_transaksi()
        self.seed_penilaian()
        self.seed_pengalaman_kerja()
        self.seed_pengalaman_mengajar()
        self.seed_pengalaman_organisasi()
        self.seed_berkas_mentor()
        self.seed_kontak_mentor()

    def seed_pengguna(self):
        Pengguna.objects.create(
            nama='Pengguna 1',
            username='pengguna1',
            email='pengguna1@example.com',
            no_telp='08123456789',
            sandi='password1',
            foto='foto1.jpg',
            role='USER'
        )
        Pengguna.objects.create(
            nama='Pengguna 2',
            username='pengguna2',
            email='pengguna2@example.com',
            no_telp='08123456788',
            sandi='password2',
            foto='foto2.jpg',
            role='mentor'
        )

    def seed_mentor(self):
        pengguna_1 = Pengguna.objects.get(username='pengguna1')
        pengguna_2 = Pengguna.objects.get(username='pengguna2')

        Mentor.objects.create(
            pengguna=pengguna_1,
            tgl_bergabung=datetime.now(),
            tempat_tanggal_lahir='Tempat Lahir 1, 1990-01-01',
            jenis_kelamin='L',
            alamat='Alamat 1',
            domisili='Domisili 1',
            universitas='Universitas 1',
            program_studi='Program Studi 1',
            semester='Semester 1',
            nim='NIM1',
            status='aktif'
        )
        Mentor.objects.create(
            pengguna=pengguna_2,
            tgl_bergabung=datetime.now(),
            tempat_tanggal_lahir='Tempat Lahir 2, 1992-02-02',
            jenis_kelamin='P',
            alamat='Alamat 2',
            domisili='Domisili 2',
            universitas='Universitas 2',
            program_studi='Program Studi 2',
            semester='Semester 2',
            nim='NIM2',
            status='pending'
        )

    def seed_kategori(self):
        Kategori.objects.create(nama_kategori='Kategori 1')
        Kategori.objects.create(nama_kategori='Kategori 2')

    def seed_metode_pembayaran(self):
        MetodePembayaran.objects.create(
            metode_pembayaran='Transfer Bank',
            nomor_rekening='1234567890',
            tipe='admin'
        )
        MetodePembayaran.objects.create(
            metode_pembayaran='Gopay',
            nomor_rekening='0987654321',
            tipe='mentor'
        )

    def seed_kelas(self):
        mentor_1 = Mentor.objects.get(id=1)
        mentor_2 = Mentor.objects.get(id=2)

        Kategori_1 = Kategori.objects.get(id=1)
        Kategori_2 = Kategori.objects.get(id=2)

        # Create Kelas instances
        Kelas.objects.create(
            nama_kelas='Kelas 1',
            mentor=mentor_1,
            deskripsi='Deskripsi Kelas 1',
            kategori_kelas=Kategori_1,
            tipe_kelas='online'
        )
        Kelas.objects.create(
            nama_kelas='Kelas 2',
            mentor=mentor_2,
            kategori_kelas=Kategori_2,
            deskripsi='Deskripsi Kelas 2',
            tipe_kelas='offline'
        )

    def seed_paket_kelas(self):
        kelas_1 = Kelas.objects.get(id=1)
        kelas_2 = Kelas.objects.get(id=2)

        PaketKelas.objects.create(
            id_kelas=kelas_1,
            nama='Paket 1',
            tipe='online',
            hari='Senin',
            jam='10:00',
            harga_kelas=100000
        )
        PaketKelas.objects.create(
            id_kelas=kelas_2,
            nama='Paket 2',
            tipe='offline',
            hari='Selasa',
            jam='14:00',
            harga_kelas=150000
        )

    def seed_transaksi(self):
        pengguna_1 = Pengguna.objects.get(username='pengguna1')
        metode_pembayaran_1 = MetodePembayaran.objects.get(id=1)

        Transaksi.objects.create(
            tgl_transaksi=datetime.now(),
            pengguna=pengguna_1,
            metode_pembayaran=metode_pembayaran_1,
            bukti_pembayaran='bukti1.jpg',
            status='lunas'
        )
        Transaksi.objects.create(
            tgl_transaksi=datetime.now(),
            pengguna=pengguna_1,
            metode_pembayaran=metode_pembayaran_1,
            bukti_pembayaran='bukti2.jpg',
            status='belum lunas'
        )

    def seed_detail_transaksi(self):
        transaksi_1 = Transaksi.objects.get(id=1)
        transaksi_2 = Transaksi.objects.get(id=2)
        kelas_1 = Kelas.objects.get(id=1)
        kelas_2 = Kelas.objects.get(id=2)
        paket_kelas_1 = PaketKelas.objects.get(id=1)
        paket_kelas_2 = PaketKelas.objects.get(id=2)

        DetailTransaksi.objects.create(
            transaksi=transaksi_1,
            kelas=kelas_1,
            tipe_kelas='online',
            paket_kelas=paket_kelas_1,
            biaya_kelas=100000
        )
        DetailTransaksi.objects.create(
            transaksi=transaksi_2,
            kelas=kelas_2,
            tipe_kelas='offline',
            paket_kelas=paket_kelas_2,
            biaya_kelas=150000
        )

    def seed_penilaian(self):
        pengguna_1 = Pengguna.objects.get(username='pengguna1')
        kelas_1 = Kelas.objects.get(id=1)

        Penilaian.objects.create(
            pengguna=pengguna_1,
            kelas=kelas_1,
            penilaian='5',
            komentar='Sangat baik'
        )
        Penilaian.objects.create(
            pengguna=pengguna_1,
            kelas=kelas_1,
            penilaian='4',
            komentar='Baik'
        )

    def seed_pengalaman_kerja(self):
        mentor_1 = Mentor.objects.get(id=1)
        mentor_2 = Mentor.objects.get(id=2)

        PengalamanKerja.objects.create(
            mentor=mentor_1,
            nama='Pengalaman Kerja 1',
            bukti='bukti_kerja1.jpg'
        )
        PengalamanKerja.objects.create(
            mentor=mentor_2,
            nama='Pengalaman Kerja 2',
            bukti='bukti_kerja2.jpg'
        )

    def seed_pengalaman_mengajar(self):
        mentor_1 = Mentor.objects.get(id=1)
        mentor_2 = Mentor.objects.get(id=2)

        PengalamanMengajar.objects.create(
            mentor=mentor_1,
            nama='Pengalaman Mengajar 1',
            bukti='bukti_mengajar1.jpg'
        )
        PengalamanMengajar.objects.create(
            mentor=mentor_2,
            nama='Pengalaman Mengajar 2',
            bukti='bukti_mengajar2.jpg'
        )
        

    def seed_pengalaman_organisasi(self):
        mentor_1 = Mentor.objects.get(id=1)
        mentor_2 = Mentor.objects.get(id=2)

        PengalamanOrganisasi.objects.create(
            mentor=mentor_1,
            nama='Pengalaman Organisasi 1',
            bukti='bukti_organisasi1.jpg'
        )
        PengalamanOrganisasi.objects.create(
            mentor=mentor_2,
            nama='Pengalaman Organisasi 2',
            bukti='bukti_organisasi2.jpg'
        )


    def seed_berkas_mentor(self):
        mentor_1 = Mentor.objects.get(id=1)
        mentor_2 = Mentor.objects.get(id=2)

        BerkasMentor.objects.create(
            mentor=mentor_1,
            cv='cv1.pdf',
            portofolio='portofolio1.pdf',
            ktp='ktp1.pdf',
            ktm='ktm1.pdf',
            aktif_mahasiswa='aktif_mahasiswa1.pdf',
            surat_komitmen='surat_komitmen1.pdf',
            transkrip_nilai='transkrip_nilai1.pdf'

        )
        BerkasMentor.objects.create(
            mentor=mentor_2,
            cv='cv2.pdf',
            portofolio='portofolio2.pdf',
            ktp='ktp2.pdf',
            ktm='ktm2.pdf',
            aktif_mahasiswa='aktif_mahasiswa2.pdf',
            surat_komitmen='surat_komitmen2.pdf',
            transkrip_nilai='transkrip_nilai2.pdf'

        )


    def __str__(self):
        return f'Kontak Mentor {self.id}'

    def seed_kontak_mentor(self):
        mentor_1 = Mentor.objects.get(id=1)
        mentor_2 = Mentor.objects.get(id=2)

        KontakMentor.objects.create(
            mentor=mentor_1,
            linkedin='linkedin.com/mentor1',
            instagram='@mentor1'
        )
        KontakMentor.objects.create(
            mentor=mentor_2,
            linkedin='linkedin.com/mentor2',
            instagram='@mentor2'
        )
