# Generated by Django 4.2.13 on 2024-06-23 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nama_kategori', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nama_kelas', models.CharField(max_length=255)),
                ('deskripsi', models.CharField(max_length=255)),
                ('tipe_kelas', models.CharField(choices=[('hybrid', 'hybrid'), ('online', 'online'), ('offline', 'offline')], max_length=10)),
                ('kategori_kelas', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='kelas_detail', to='home.kategori')),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tgl_bergabung', models.DateField()),
                ('tempat_tanggal_lahir', models.CharField(max_length=255)),
                ('jenis_kelamin', models.CharField(choices=[('L', 'L'), ('P', 'P')], max_length=1)),
                ('alamat', models.CharField(max_length=255)),
                ('domisili', models.CharField(max_length=255)),
                ('universitas', models.CharField(max_length=255)),
                ('program_studi', models.CharField(max_length=255)),
                ('semester', models.CharField(max_length=255)),
                ('nim', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('aktif', 'aktif'), ('pending', 'pending')], default='pending', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MetodePembayaran',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('metode_pembayaran', models.CharField(max_length=255)),
                ('nomor_rekening', models.CharField(max_length=255)),
                ('tipe', models.CharField(choices=[('mentor', 'mentor'), ('admin', 'admin')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pengguna',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('no_telp', models.CharField(max_length=255)),
                ('sandi', models.CharField(max_length=255)),
                ('foto', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('admin', 'admin'), ('USER', 'USER'), ('mentor', 'mentor')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tgl_transaksi', models.DateTimeField()),
                ('bukti_pembayaran', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('mengunggu', 'mengunggu'), ('lunas', 'lunas'), ('belum lunas', 'belum lunas')], max_length=20)),
                ('metode_pembayaran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.metodepembayaran')),
                ('pengguna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.pengguna')),
            ],
        ),
        migrations.CreateModel(
            name='Penilaian',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('penilaian', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1)),
                ('komentar', models.CharField(max_length=255)),
                ('kelas', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.kelas')),
                ('pengguna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.pengguna')),
            ],
        ),
        migrations.CreateModel(
            name='PengalamanOrganisasi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=255)),
                ('bukti', models.CharField(max_length=255)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.mentor')),
            ],
        ),
        migrations.CreateModel(
            name='PengalamanMengajar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=255)),
                ('bukti', models.CharField(max_length=255)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.mentor')),
            ],
        ),
        migrations.CreateModel(
            name='PengalamanKerja',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=255)),
                ('bukti', models.CharField(max_length=255)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.mentor')),
            ],
        ),
        migrations.CreateModel(
            name='PaketKelas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=255)),
                ('tipe', models.CharField(choices=[('offline', 'offline'), ('online', 'online')], max_length=10)),
                ('hari', models.CharField(max_length=255)),
                ('jam', models.CharField(max_length=255)),
                ('harga_kelas', models.IntegerField()),
                ('id_kelas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.kelas')),
            ],
        ),
        migrations.AddField(
            model_name='mentor',
            name='pengguna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.pengguna'),
        ),
        migrations.CreateModel(
            name='KontakMentor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('linkedin', models.CharField(max_length=255)),
                ('instagram', models.CharField(max_length=255)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.mentor')),
            ],
        ),
        migrations.AddField(
            model_name='kelas',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.mentor'),
        ),
        migrations.CreateModel(
            name='DetailTransaksi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipe_kelas', models.CharField(max_length=255)),
                ('biaya_kelas', models.IntegerField()),
                ('kelas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.kelas')),
                ('paket_kelas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.paketkelas')),
                ('transaksi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.transaksi')),
            ],
        ),
        migrations.CreateModel(
            name='BerkasMentor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cv', models.CharField(max_length=255)),
                ('portofolio', models.CharField(max_length=255)),
                ('ktp', models.CharField(max_length=255)),
                ('ktm', models.CharField(max_length=255)),
                ('aktif_mahasiswa', models.CharField(max_length=255)),
                ('surat_komitmen', models.CharField(max_length=255)),
                ('transkrip_nilai', models.CharField(max_length=255)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.mentor')),
            ],
        ),
    ]
