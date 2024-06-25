from django.core.management.base import BaseCommand
from home.models import Pengguna, Mentor, Kategori, Kelas, PaketKelas, Transaksi, DetailTransaksi, MetodePembayaran, Penilaian, PengalamanKerja, PengalamanMengajar, PengalamanOrganisasi, BerkasMentor, KontakMentor, skills, skill_mentor, project_mentor
# from home.models import *
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
        # self.seed_transaksi()
        # self.seed_detail_transaksi()
        self.seed_penilaian()
        self.seed_pengalaman_kerja()
        self.seed_pengalaman_mengajar()
        self.seed_pengalaman_organisasi() 
        self.seed_berkas_mentor()
        self.seed_kontak_mentor()
        self.seed_skills()
        self.seed_skill_mentor()
        self.seed_project_mentor()

    def seed_pengguna(self):
        Pengguna.objects.create(
            nama='Joko Suherman',
            username='joko',
            email='joko@gmail.com',
            no_telp='081192210112',
            sandi='123',
            foto='/foto_pengguna/joko.jpg',
            role='mentor'
        )

        Pengguna.objects.create(
            nama='Rini Wulandari',
            username='rini',
            email='rini@gmail.com',
            no_telp='08123456788',
            sandi='123',
            foto='/foto_pengguna/rini.jpg',
            role='mentor'
        )

        Pengguna.objects.create(
            nama='Wahyu Aji',
            username='wahyu',
            email='wahyu@gmail.com',
            no_telp='08123456788',
            sandi='123',
            foto='/foto_pengguna/wahyu.jpg',
            role='mentor'
        )

        Pengguna.objects.create(
            nama='Asep',
            username='asep',
            email='asep@gmail.com',
            no_telp='08123456788',
            sandi='123',
            foto='/foto_pengguna/asep.jpg',
            role='USER'
        )

        Pengguna.objects.create(
            nama='Budi',
            username='budi',
            email = 'budi@gmail.com',
            no_telp='08123456788',
            sandi='123',
            foto='/foto_pengguna/budi.jpg',
            role='USER'
        )
            
            

    def seed_mentor(self):
        pengguna_1 = Pengguna.objects.get(username='joko')
        pengguna_2 = Pengguna.objects.get(username='rini')
        pengguna_3 = Pengguna.objects.get(username='wahyu')

        Mentor.objects.create(
            pengguna=pengguna_1,
            tgl_bergabung=datetime.now(),
            tempat_tanggal_lahir='Sleman, 2003-01-01',
            jenis_kelamin='L',
            alamat='Alamat 1',
            domisili='Sleman, Yogyakarta',
            universitas='Universitas Gadja Mada',
            program_studi='Teknik Informatika',
            semester='Semester 6',
            nim='210112',
            status='aktif',
            bio='Seseorang yang suka matematika, fisika, dan biologi',
            video_profile='SJV88ww9R5o&t=2s'
        )

        Mentor.objects.create(
            pengguna=pengguna_2,
            tgl_bergabung=datetime.now(),
            tempat_tanggal_lahir='Bogor, 2002-02-02',
            jenis_kelamin='P',
            alamat='Bogor, Jawa Barat',
            domisili='Bogor, Jawa Barat',
            universitas='Universitas Bogor',
            program_studi='Program Studi 2',
            semester='Semester 2',
            nim='210113',
            status='aktif',
            bio='Seseorang yang suka matematika, fisika, dan biologi',
            video_profile='SJV88ww9R5o&t=2s'
        )

        Mentor.objects.create(
            pengguna=pengguna_3,
            tgl_bergabung=datetime.now(),
            tempat_tanggal_lahir='Jakarta, 2001-03-03',
            jenis_kelamin='L',
            alamat='Jakarta, DKI Jakarta',
            domisili='Jakarta, DKI Jakarta',
            universitas='Universitas Jakarta',
            program_studi='Program Studi 3',
            semester='Semester 4',
            nim='210114',
            status='aktif',
            bio='Seseorang yang suka desain web dan uiux',
            video_profile='SJV88ww9R5o&t=2s'
        )

    def seed_kategori(self):
        Kategori.objects.create(nama_kategori='Matematika')
        Kategori.objects.create(nama_kategori='Web Development')
        Kategori.objects.create(nama_kategori='Fisika')
        Kategori.objects.create(nama_kategori='UIUX')
        Kategori.objects.create(nama_kategori='Biologi')
        Kategori.objects.create(nama_kategori='Bahasa Indonesia')

    def seed_metode_pembayaran(self):
        MetodePembayaran.objects.create(
            metode_pembayaran='BNI',
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
        mentor_3 = Mentor.objects.get(id=3)

        Kategori_1 = Kategori.objects.get(id=1)
        Kategori_2 = Kategori.objects.get(id=2)
        Kategori_3 = Kategori.objects.get(id=3)
        Kategori_4 = Kategori.objects.get(id=4)
        Kategori_5 = Kategori.objects.get(id=5)

        # Create Kelas instances
        Kelas.objects.create(
            nama_kelas='Matematika Mudah',
            mentor=mentor_1,
            deskripsi='materi matematika mudah',
            kategori_kelas=Kategori_1,
            tipe_kelas='online',
            foto='/foto_kelas/matematika-1.jpg',
            silabus='https://drive.google.com/file/d/1T0M-J6_X8I0pazn5j6QYPNdDEEmHzbcJ/view'
        )

        Kelas.objects.create(
            nama_kelas='Fisika Mudah',
            mentor=mentor_1,
            deskripsi='materi fisika mudah',
            kategori_kelas=Kategori_3,
            tipe_kelas='online',
            foto='/foto_kelas/fisika-1.jpg',
            silabus='https://drive.google.com/file/d/1T0M-J6_X8I0pazn5j6QYPNdDEEmHzbcJ/view'
        )

        Kelas.objects.create(
            nama_kelas='Matematika Asyik',
            mentor=mentor_2,
            deskripsi='materi matematika mudah',
            kategori_kelas=Kategori_1,
            tipe_kelas='online',
            foto='/foto_kelas/matematika-2.jpg',
            silabus='https://drive.google.com/file/d/1T0M-J6_X8I0pazn5j6QYPNdDEEmHzbcJ/view'
        )

        Kelas.objects.create(
            nama_kelas='Biologi Mudah',
            mentor=mentor_2,
            deskripsi='materi biologi mudah',
            kategori_kelas=Kategori_5,
            tipe_kelas='online',
            foto='/foto_kelas/biologi-1.jpg',
            silabus='https://drive.google.com/file/d/1T0M-J6_X8I0pazn5j6QYPNdDEEmHzbcJ/view'
        )

        Kelas.objects.create(
            nama_kelas='Web Development',
            mentor=mentor_3,
            deskripsi='materi web development',
            kategori_kelas=Kategori_2,
            tipe_kelas='online',
            foto='/foto_kelas/web-1.jpg',
            silabus='https://drive.google.com/file/d/1T0M-J6_X8I0pazn5j6QYPNdDEEmHzbcJ/view'
        )

        Kelas.objects.create(
            nama_kelas='UIUX',
            mentor=mentor_3,
            deskripsi='materi uiux',
            kategori_kelas=Kategori_4,
            tipe_kelas='online',
            foto='/foto_kelas/uiux-1.jpg',
            silabus='https://drive.google.com/file/d/1T0M-J6_X8I0pazn5j6QYPNdDEEmHzbcJ/view'
        )

        

    def seed_paket_kelas(self):
        kelas_1 = Kelas.objects.get(id=1)
        kelas_2 = Kelas.objects.get(id=2)
        kelas_3 = Kelas.objects.get(id=3)
        kelas_4 = Kelas.objects.get(id=4)
        kelas_5 = Kelas.objects.get(id=5)
        kelas_6 = Kelas.objects.get(id=6)

        PaketKelas.objects.create(
            id_kelas=kelas_1,
            nama='1 hari matematika',
            tipe='online',
            hari='Senin',
            jam='10:00',
            jumlah_pertemuan=1,
            harga_kelas=100000
        )

        PaketKelas.objects.create(
            id_kelas=kelas_1,
            nama='3 hari matematika',
            tipe='online',
            hari='Senin, Selasa, Rabu',
            jam='19:00',
            jumlah_pertemuan=3,
            harga_kelas=100000
        )

        PaketKelas.objects.create(
            id_kelas=kelas_2,
            nama='1 hari fisika',
            tipe='online',
            hari='Senin',
            jam='10:00',
            jumlah_pertemuan=1,
            harga_kelas=100000
        )

        PaketKelas.objects.create(
            id_kelas=kelas_2,
            nama='3 hari fisika',
            tipe='online',
            hari='Senin, Selasa, Rabu',
            jam='19:00',
            jumlah_pertemuan=3,
            harga_kelas=100000
        )

        PaketKelas.objects.create(
            id_kelas=kelas_3,
            nama='1 hari math',
            tipe='online',
            hari='Senin',
            jam='10:00',
            jumlah_pertemuan=1,
            harga_kelas=100000
        )

        PaketKelas.objects.create(
            id_kelas=kelas_3,
            nama='3 hari math',
            tipe='online',
            hari='Senin, Selasa, Rabu',
            jam='19:00',
            jumlah_pertemuan=3,
            harga_kelas=100000
        )

        PaketKelas.objects.create(
            id_kelas=kelas_4,
            nama='1 hari biologi',
            tipe='online',
            hari='Senin',
            jam='10:00',
            jumlah_pertemuan=1,
            harga_kelas=100000
        )

        PaketKelas.objects.create(
            id_kelas=kelas_4,
            nama='3 hari biologi',
            tipe='online',
            hari='Senin, Selasa, Rabu',
            jam='19:00',
            jumlah_pertemuan=3,
            harga_kelas=100000
        )

        PaketKelas.objects.create(
            id_kelas=kelas_5,
            nama='1 hari web',
            tipe='online',
            hari='Senin',
            jam='10:00',
            jumlah_pertemuan=1,
            harga_kelas=100000
        )

        PaketKelas.objects.create(
            id_kelas=kelas_5,
            nama='3 hari web',
            tipe='online',
            hari='Senin, Selasa, Rabu',
            jam='19:00',
            jumlah_pertemuan=3,
            harga_kelas=100000
        )

        PaketKelas.objects.create(
            id_kelas=kelas_6,
            nama='1 hari UI UX',
            tipe='online',
            hari='Senin',
            jam='10:00',
            jumlah_pertemuan=1,
            harga_kelas=100000
        )

        PaketKelas.objects.create(
            id_kelas=kelas_6,
            nama='3 hari UI UX',
            tipe='online',
            hari='Senin, Selasa, Rabu',
            jam='19:00',
            jumlah_pertemuan=3,
            harga_kelas=100000
        )

        

    # def seed_transaksi(self):
    #     pengguna_1 = Pengguna.objects.get(username='pengguna1')
    #     metode_pembayaran_1 = MetodePembayaran.objects.get(id=1)

    #     Transaksi.objects.create(
    #         tgl_transaksi=datetime.now(),
    #         pengguna=pengguna_1,
    #         metode_pembayaran=metode_pembayaran_1,
    #         bukti_pembayaran='bukti1.jpg',
    #         status='lunas'
    #     )
    #     Transaksi.objects.create(
    #         tgl_transaksi=datetime.now(),
    #         pengguna=pengguna_1,
    #         metode_pembayaran=metode_pembayaran_1,
    #         bukti_pembayaran='bukti2.jpg',
    #         status='belum lunas'
    #     )

    # def seed_detail_transaksi(self):
    #     transaksi_1 = Transaksi.objects.get(id=1)
    #     transaksi_2 = Transaksi.objects.get(id=2)
    #     kelas_1 = Kelas.objects.get(id=1)
    #     kelas_2 = Kelas.objects.get(id=2)
    #     paket_kelas_1 = PaketKelas.objects.get(id=1)
    #     paket_kelas_2 = PaketKelas.objects.get(id=2)

    #     DetailTransaksi.objects.create(
    #         transaksi=transaksi_1,
    #         kelas=kelas_1,
    #         tipe_kelas='online',
    #         paket_kelas=paket_kelas_1,
    #         biaya_kelas=100000
    #     )
    #     DetailTransaksi.objects.create(
    #         transaksi=transaksi_2,
    #         kelas=kelas_2,
    #         tipe_kelas='offline',
    #         paket_kelas=paket_kelas_2,
    #         biaya_kelas=150000
    #     )

    def seed_penilaian(self):
        pengguna_1 = Pengguna.objects.get(username='asep')
        kelas_1 = Kelas.objects.get(id=1)
        kelas_2 = Kelas.objects.get(id=2)
        kelas_3 = Kelas.objects.get(id=3)
        kelas_4 = Kelas.objects.get(id=4)
        kelas_5 = Kelas.objects.get(id=5)
        kelas_6 = Kelas.objects.get(id=6)

        Penilaian.objects.create(
            pengguna=pengguna_1,
            kelas=kelas_1,
            penilaian='5',
            komentar='Sangat baik'
        )
        Penilaian.objects.create(
            pengguna=pengguna_1,
            kelas=kelas_2,
            penilaian='4',
            komentar='Baik'
        )
        Penilaian.objects.create(
            pengguna=pengguna_1,
            kelas=kelas_3,
            penilaian='4',
            komentar='Baik'
        )
        Penilaian.objects.create(
            pengguna=pengguna_1,
            kelas=kelas_4,
            penilaian='4',
            komentar='Baik'
        )
        Penilaian.objects.create(
            pengguna=pengguna_1,
            kelas=kelas_5,
            penilaian='4',
            komentar='Baik'
        )
        Penilaian.objects.create(
            pengguna=pengguna_1,
            kelas=kelas_6,
            penilaian='4',
            komentar='Baik'
        )

    def seed_pengalaman_kerja(self):
        mentor_1 = Mentor.objects.get(id=1)
        mentor_2 = Mentor.objects.get(id=2)
        mentor_3 = Mentor.objects.get(id=3)

        PengalamanKerja.objects.create(
            mentor=mentor_1,
            nama='QA Engineer',
            tempat='PT. ABC',
            waktu='September 2020 - Agustus 2021',
            deskripsi='QA Engineer',
            keahlian='Web Development, Testing',
            bukti='bukti_kerja1.jpg'
        )

        PengalamanKerja.objects.create(
            mentor=mentor_1,
            nama='Asisten Praktikum',
            tempat='Universitas Gadjah Mada',
            waktu='September 2019 - Agustus 2020',
            deskripsi='Asisten praktikum matematika',
            keahlian='Matematika, Fisika',
            bukti='bukti_kerja1.jpg'
        )

        PengalamanKerja.objects.create(
            mentor=mentor_2,
            nama='Editor Buku',
            tempat='PT. XYZ',
            waktu='September 2020 - Agustus 2021',
            deskripsi='Editor Buku Bahasa Indonesia',
            keahlian='Mnulis, Bahasa Indonesia',
            bukti='bukti_kerja2.jpg'
        )

        PengalamanKerja.objects.create(
            mentor=mentor_2,
            nama='Editor Buku',
            tempat='Zaman Now',
            waktu='September 2019 - Agustus 2020',
            deskripsi='Editor Buku Bahasa Indonesia',
            keahlian='Mnulis, Bahasa Indonesia',
            bukti='bukti_kerja2.jpg'
        )

        PengalamanKerja.objects.create(
            mentor=mentor_3,
            nama='Web Developer',
            tempat='rumah.com',
            waktu='September 2020 - Agustus 2021',
            deskripsi='Web Developer',
            keahlian='Web Development',
            bukti='bukti_kerja3.jpg'
        )

        PengalamanKerja.objects.create(
            mentor=mentor_3,
            nama='Frontend Developer',
            tempat='Saung.com',
            waktu='September 2019 - Agustus 2020',
            deskripsi='frontend Developer',
            keahlian='Tailwind, Bootstrap, React',
            bukti='bukti_kerja3.jpg'
        )


        

    def seed_pengalaman_mengajar(self):
        mentor_1 = Mentor.objects.get(id=1)
        mentor_2 = Mentor.objects.get(id=2)
        mentor_3 = Mentor.objects.get(id=3)

        PengalamanMengajar.objects.create(
            mentor=mentor_1,
            nama='Asisten Praktikum',
            tempat='Universitas Gadjah Mada',
            waktu='September 2020 - Agustus 2021',
            deskripsi='Mengajar Matematika',
            keahlian='Matematika, Fisika',
            bukti='bukti_mengajar1.jpg'
        )
        
        PengalamanMengajar.objects.create(
            mentor=mentor_1,
            nama='Instruktur',
            tempat='Kursus ABC',
            waktu='September 2019 - Agustus 2020',
            deskripsi='Instruktur Fisika',
            keahlian='Fisika',
            bukti='bukti_mengajar1.jpg'
        )

        PengalamanMengajar.objects.create(
            mentor=mentor_2,
            nama='Instruktur',
            tempat='Kursus XYZ',
            waktu='September 2020 - Agustus 2021',
            deskripsi='Instruktur Bahasa Indonesia',
            keahlian='Bahasa Indonesia',
            bukti='bukti_mengajar2.jpg'
        )

        PengalamanMengajar.objects.create(
            mentor=mentor_2,
            nama='Instruktur',
            tempat='Kursus Zaman Now',
            waktu='September 2019 - Agustus 2020',
            deskripsi='Instruktur Bahasa Indonesia',
            keahlian='Bahasa Indonesia',
            bukti='bukti_mengajar2.jpg'
        )

        PengalamanMengajar.objects.create(
            mentor=mentor_3,
            nama='Mentor Web Development',
            tempat='Kelas Online',
            waktu='September 2020 - Agustus 2021',
            deskripsi='Mentor Web Development',
            keahlian='Web Development',
            bukti='bukti_mengajar3.jpg'
        )

        PengalamanMengajar.objects.create(
            mentor=mentor_3,
            nama='Mentor UIUX',
            tempat='Kelas Online',
            waktu='September 2019 - Agustus 2020',
            deskripsi='Mentor UIUX',
            keahlian='UIUX',
            bukti='bukti_mengajar3.jpg'
        )
 

        

    def seed_pengalaman_organisasi(self):
        mentor_1 = Mentor.objects.get(id=1)
        mentor_2 = Mentor.objects.get(id=2)
        mentor_3 = Mentor.objects.get(id=3)

        PengalamanOrganisasi.objects.create(
            mentor=mentor_1,
            nama='Pendidikan IPA',
            tempat='Universitas QWE',
            waktu='September 2020 - Agustus 2021',
            bukti='bukti_organisasi1.jpg'
        )


        PengalamanOrganisasi.objects.create(
            mentor=mentor_2,
            nama='Pendidikan Bahasa Indonesia',
            tempat='Universitas ASD',
            waktu='September 2019 - Agustus 2020',
            bukti='bukti_organisasi2.jpg'
        )

        PengalamanOrganisasi.objects.create(
            mentor=mentor_3,
            nama='Pendidikan Web Development',
            tempat='Universitas ZXC',
            waktu='September 2020 - Agustus 2021',
            bukti='bukti_organisasi3.jpg'
        )


    def seed_berkas_mentor(self):
        mentor_1 = Mentor.objects.get(id=1)
        mentor_2 = Mentor.objects.get(id=2)
        mentor_3 = Mentor.objects.get(id=3)

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

        BerkasMentor.objects.create(
            mentor=mentor_3,
            cv='cv3.pdf',
            portofolio='portofolio3.pdf',
            ktp='ktp3.pdf',
            ktm='ktm3.pdf',
            aktif_mahasiswa='aktif_mahasiswa3.pdf',
            surat_komitmen='surat_komitmen3.pdf',
            transkrip_nilai='transkrip_nilai3.pdf'

        )




    def __str__(self):
        return f'Kontak Mentor {self.id}'

    def seed_kontak_mentor(self):
        mentor_1 = Mentor.objects.get(id=1)
        mentor_2 = Mentor.objects.get(id=2)
        mentor_3 = Mentor.objects.get(id=3)

        KontakMentor.objects.create(
            mentor=mentor_1,
            linkedin='linkedin.com/mentor1',
            instagram='instagram.com/mentor1'
        )
        
        KontakMentor.objects.create(
            mentor=mentor_2,
            linkedin='linkedin.com/mentor2',
            instagram='instagram.com/mentor2'
        )

        KontakMentor.objects.create(
            mentor=mentor_3,
            linkedin='linkedin.com/mentor3',
            instagram='instagram.com/mentor3'
        )


    def seed_skills(self):
        skills.objects.create(
            nama='Matematika',
            foto='foto_skill/math.jpg'
        )
        skills.objects.create(
            nama='Fisika',
            foto='foto_skill/fisika.jpg'
        ) 
        skills.objects.create(
            nama='Laravel',
            foto='foto_skill/laravel.jpg'
        )
        skills.objects.create(
            nama='Figma',
            foto='foto_skill/figma.jpg'
        )
        # skills.objects.create(
        #     nama_skill='React',
        #     foto='foto_skill/react.jpg'
        # )
        # skills.objects.create(
        #     nama_skill='Tailwind',
        #     foto='foto_skill/tailwind.jpg'
        # )
        # skills.objects.create(
        #     nama_skill='Bootstrap',
        #     foto='foto_skill/bootstrap.jpg'
        # )
    
    def seed_skill_mentor(self):
        mentor_1 = Mentor.objects.get(id=1)
        mentor_2 = Mentor.objects.get(id=2)
        mentor_3 = Mentor.objects.get(id=3)

        skill_1 = skills.objects.get(id=1)
        skill_2 = skills.objects.get(id=2)
        skill_3 = skills.objects.get(id=3)
        skill_4 = skills.objects.get(id=4)

        skill_mentor.objects.create(
            mentor=mentor_1,
            skill=skill_1
        )
        skill_mentor.objects.create(
            mentor=mentor_1,
            skill=skill_2
        )
        skill_mentor.objects.create(
            mentor=mentor_2,
            skill=skill_3
        )
        skill_mentor.objects.create(
            mentor=mentor_2,
            skill=skill_1
        )
        skill_mentor.objects.create(
            mentor=mentor_3,
            skill=skill_3
        )
        skill_mentor.objects.create(
            mentor=mentor_3,
            skill=skill_4
        )
            

    def seed_project_mentor(self):
        mentor_1 = Mentor.objects.get(id=1)
        mentor_2 = Mentor.objects.get(id=2)
        mentor_3 = Mentor.objects.get(id=3)

        project_mentor.objects.create(
            mentor=mentor_1,
            nama='Buku Matematika',
            foto='foto_project/buku-1.jpg'
        )
        project_mentor.objects.create(
            mentor=mentor_2,
            nama='Buku Cerita Anak',
            foto='foto_project/buku-2.jpg'
        )

        project_mentor.objects.create(
            mentor=mentor_3,
            nama='Web Kursus',
            foto='foto_project/web-1.jpg'
        )


        

    
