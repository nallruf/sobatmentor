from django.db import models
import bcrypt


class DetailTransaksi(models.Model):
    id = models.AutoField(primary_key=True)
    transaksi = models.ForeignKey('Transaksi', on_delete=models.CASCADE)
    kelas = models.ForeignKey('Kelas', on_delete=models.CASCADE)
    tipe_kelas = models.CharField(max_length=255)
    paket_kelas = models.ForeignKey('PaketKelas', on_delete=models.CASCADE)
    biaya_kelas = models.IntegerField()

    def __str__(self):
        return f'Detail Transaksi {self.id}'


class PengalamanKerja(models.Model):
    id = models.AutoField(primary_key=True)
    mentor = models.ForeignKey('Mentor', on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    bukti = models.CharField(max_length=255)

    def __str__(self):
        return f'Pengalaman Kerja {self.id}'


class MetodePembayaran(models.Model):
    id = models.AutoField(primary_key=True)
    metode_pembayaran = models.CharField(max_length=255)
    nomor_rekening = models.CharField(max_length=255)
    tipe = models.CharField(max_length=10, choices=[('mentor', 'mentor'), ('admin', 'admin')])

    def __str__(self):
        return self.metode_pembayaran


class PengalamanMengajar(models.Model):
    id = models.AutoField(primary_key=True)
    mentor = models.ForeignKey('Mentor', on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    bukti = models.CharField(max_length=255)

    def __str__(self):
        return f'Pengalaman Mengajar {self.id}'


class Pengguna(models.Model):
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    no_telp = models.CharField(max_length=255)
    sandi = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='foto_pengguna/', blank=True, null=True)
    role = models.CharField(max_length=10, choices=[('admin', 'admin'), ('USER', 'USER'), ('mentor', 'mentor')])

    # def save(self, *args, **kwargs):
    #     if self._state.adding:
    #         self.sandi = bcrypt.hashpw(self.sandi.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.nama


class Kategori(models.Model):
    id = models.AutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_kategori


class Penilaian(models.Model):
    id = models.AutoField(primary_key=True)
    pengguna = models.ForeignKey('Pengguna', on_delete=models.CASCADE)
    kelas = models.ForeignKey('Kelas', on_delete=models.CASCADE)
    penilaian = models.CharField(max_length=1, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    komentar = models.CharField(max_length=255)

    def __str__(self):
        return f'Penilaian {self.id}'


class PaketKelas(models.Model):
    id = models.AutoField(primary_key=True)
    id_kelas = models.ForeignKey('Kelas', on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    tipe = models.CharField(max_length=10, choices=[('offline', 'offline'), ('online', 'online')])
    hari = models.CharField(max_length=255)
    jam = models.CharField(max_length=255)
    harga_kelas = models.IntegerField()

    def __str__(self):
        return self.nama


class Mentor(models.Model):
    id = models.AutoField(primary_key=True)
    pengguna = models.ForeignKey('Pengguna', on_delete=models.CASCADE)
    tgl_bergabung = models.DateField()
    tempat_tanggal_lahir = models.CharField(max_length=255)
    jenis_kelamin = models.CharField(max_length=1, choices=[('L', 'L'), ('P', 'P')])
    alamat = models.CharField(max_length=255)
    domisili = models.CharField(max_length=255)
    universitas = models.CharField(max_length=255)
    program_studi = models.CharField(max_length=255)
    semester = models.CharField(max_length=255)
    nim = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=[('aktif', 'aktif'), ('pending', 'pending')], default='pending')

    def __str__(self):
        return self.pengguna.nama



class BerkasMentor(models.Model):
    id = models.AutoField(primary_key=True)
    mentor = models.ForeignKey('Mentor', on_delete=models.CASCADE)
    cv = models.CharField(max_length=255)
    portofolio = models.CharField(max_length=255)
    ktp = models.CharField(max_length=255)
    ktm = models.CharField(max_length=255)
    aktif_mahasiswa = models.CharField(max_length=255)
    surat_komitmen = models.CharField(max_length=255)
    transkrip_nilai = models.CharField(max_length=255)

    def __str__(self):
        return f'Berkas Mentor {self.id}'


class Transaksi(models.Model):
    id = models.AutoField(primary_key=True)
    tgl_transaksi = models.DateTimeField()
    pengguna = models.ForeignKey('Pengguna', on_delete=models.CASCADE)
    metode_pembayaran = models.ForeignKey('MetodePembayaran', on_delete=models.CASCADE)
    bukti_pembayaran = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[('mengunggu', 'mengunggu'), ('lunas', 'lunas'), ('belum lunas', 'belum lunas')])

    def __str__(self):
        return f'Transaksi {self.id}'


class Kelas(models.Model):
    id = models.AutoField(primary_key=True)
    nama_kelas = models.CharField(max_length=255)
    kategori_kelas = models.OneToOneField('Kategori', on_delete=models.CASCADE, related_name='kelas_detail')
    mentor = models.ForeignKey('Mentor', on_delete=models.CASCADE)
    deskripsi = models.CharField(max_length=255)
    tipe_kelas = models.CharField(max_length=10, choices=[('hybrid', 'hybrid'), ('online', 'online'), ('offline', 'offline')])

    def __str__(self):
        return self.nama_kelas


class KontakMentor(models.Model):
    id = models.AutoField(primary_key=True)
    mentor = models.ForeignKey('Mentor', on_delete=models.CASCADE)
    linkedin = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)

    def __str__(self):
        return f'Kontak Mentor {self.id}'


class PengalamanOrganisasi(models.Model):
    id = models.AutoField(primary_key=True)
    mentor = models.ForeignKey('Mentor', on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    bukti = models.CharField(max_length=255)

    def __str__(self):
        return f'Pengalaman Organisasi {self.id}'
