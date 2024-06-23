CREATE TABLE `detail_transaksi`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `transaksi` INT NOT NULL,
    `kelas` INT NOT NULL,
    `tipe_kelas` VARCHAR(255) NOT NULL,
    `paket_kelas` INT NOT NULL,
    `biaya_kelas` INT NOT NULL
);
CREATE TABLE `pengalaman_kerja`(
    `id` INT NOT NULL,
    `mentor` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `nama` VARCHAR(255) NOT NULL,
    `bukti` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`id`)
);
CREATE TABLE `metode_pembayaran`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `metode_pembayaran` VARCHAR(255) NOT NULL,
    `nomor_rekening` VARCHAR(255) NOT NULL,
    `tipe` ENUM("mentor", "admin") NOT NULL
);
CREATE TABLE `pengalaman_mengajar`(
    `id` INT NOT NULL,
    `mentor` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `nama` VARCHAR(255) NOT NULL,
    `bukti` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`id`)
);
CREATE TABLE `pengguna`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nama` VARCHAR(255) NOT NULL,
    `username` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) NOT NULL,
    `no_telp` VARCHAR(255) NOT NULL,
    `sandi` VARCHAR(255) NOT NULL,
    `foto` VARCHAR(255) NOT NULL,
    `role` ENUM("admin", "USER", "mentor") NOT NULL
);
CREATE TABLE `kategori`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nama_kategori` VARCHAR(255) NOT NULL
);
CREATE TABLE `penilaian`(
    `id` INT NOT NULL,
    `pengguna` INT NOT NULL,
    `kelas` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `penilaian` ENUM("1", "2", "3", "4", "5") NOT NULL,
    `komentar` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`id`)
);
CREATE TABLE `paket_kelas`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_kelas` INT NOT NULL,
    `nama` VARCHAR(255) NOT NULL,
    `tipe` ENUM('"offline"', '"online"') NOT NULL,
    `hari` VARCHAR(255) NOT NULL,
    `jam` VARCHAR(255) NOT NULL,
    `harga_kelas` INT NOT NULL
);
CREATE TABLE `mentor`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `pengguna` INT NOT NULL,
    `tgl_bergabung` DATE NOT NULL,
    `tempat_tanggal_lahir` VARCHAR(255) NOT NULL,
    `jenis_kelamin` ENUM("L", "P") NOT NULL,
    `alamat` VARCHAR(255) NOT NULL,
    `domisili` VARCHAR(255) NOT NULL,
    `universitas` VARCHAR(255) NOT NULL,
    `program_studi` VARCHAR(255) NOT NULL,
    `semester` VARCHAR(255) NOT NULL,
    `nim` VARCHAR(255) NOT NULL,
    `status` ENUM("aktif", "pending") NOT NULL DEFAULT 'pending'
);
CREATE TABLE `kategori_kelas`(
    `kelas` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `kategori` INT NOT NULL,
    PRIMARY KEY(`kategori`)
);
CREATE TABLE `berkas_mentor`(
    `id` INT NOT NULL,
    `mentor` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `cv` VARCHAR(255) NOT NULL,
    `portofolio` VARCHAR(255) NOT NULL,
    `ktp` VARCHAR(255) NOT NULL,
    `ktm` VARCHAR(255) NOT NULL,
    `aktif_mahasiswa` VARCHAR(255) NOT NULL,
    `surat_komitmen` VARCHAR(255) NOT NULL,
    `transkrip_nilai` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`id`)
);
CREATE TABLE `transaksi`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `tgl_transaksi` DATETIME NOT NULL,
    `pengguna` INT NOT NULL,
    `metode_pembayaran` INT NOT NULL,
    `bukti_pembayaran` VARCHAR(255) NOT NULL,
    `status` ENUM(
        '"mengunggu"',
        '"lunas"',
        '"belum lunas"'
    ) NOT NULL
);
CREATE TABLE `kelas`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nama_kelas` VARCHAR(255) NOT NULL,
    `kategori_kelas` INT NOT NULL,
    `mentor` INT NOT NULL,
    `deskripsi` VARCHAR(255) NOT NULL,
    `tipe_kelas` ENUM("hybrid","online","offline") NOT NULL
);
CREATE TABLE `kontak_mentor`(
    `id` VARCHAR(255) NOT NULL,
    `mentor` BIGINT NOT NULL,
    `linkedin` VARCHAR(255) NOT NULL,
    `instagram` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`id`)
);
CREATE TABLE `pengalaman_organisasi`(
    `id` INT NOT NULL,
    `mentor` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `nama` VARCHAR(255) NOT NULL,
    `bukti` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`id`)
);
ALTER TABLE
    `kategori` ADD CONSTRAINT `kategori_id_foreign` FOREIGN KEY(`id`) REFERENCES `kategori_kelas`(`kategori`);
ALTER TABLE
    `penilaian` ADD CONSTRAINT `penilaian_pengguna_foreign` FOREIGN KEY(`pengguna`) REFERENCES `pengguna`(`id`);
ALTER TABLE
    `paket_kelas` ADD CONSTRAINT `paket_kelas_id_kelas_foreign` FOREIGN KEY(`id_kelas`) REFERENCES `kelas`(`id`);
ALTER TABLE
    `kontak_mentor` ADD CONSTRAINT `kontak_mentor_mentor_foreign` FOREIGN KEY(`mentor`) REFERENCES `mentor`(`id`);
ALTER TABLE
    `detail_transaksi` ADD CONSTRAINT `detail_transaksi_transaksi_foreign` FOREIGN KEY(`transaksi`) REFERENCES `transaksi`(`id`);
ALTER TABLE
    `transaksi` ADD CONSTRAINT `transaksi_pengguna_foreign` FOREIGN KEY(`pengguna`) REFERENCES `pengguna`(`id`);
ALTER TABLE
    `pengalaman_mengajar` ADD CONSTRAINT `pengalaman_mengajar_mentor_foreign` FOREIGN KEY(`mentor`) REFERENCES `mentor`(`id`);
ALTER TABLE
    `pengalaman_organisasi` ADD CONSTRAINT `pengalaman_organisasi_mentor_foreign` FOREIGN KEY(`mentor`) REFERENCES `mentor`(`id`);
ALTER TABLE
    `detail_transaksi` ADD CONSTRAINT `detail_transaksi_kelas_foreign` FOREIGN KEY(`kelas`) REFERENCES `kelas`(`id`);
ALTER TABLE
    `berkas_mentor` ADD CONSTRAINT `berkas_mentor_mentor_foreign` FOREIGN KEY(`mentor`) REFERENCES `mentor`(`id`);
ALTER TABLE
    `mentor` ADD CONSTRAINT `mentor_pengguna_foreign` FOREIGN KEY(`pengguna`) REFERENCES `pengguna`(`id`);
ALTER TABLE
    `pengalaman_kerja` ADD CONSTRAINT `pengalaman_kerja_mentor_foreign` FOREIGN KEY(`mentor`) REFERENCES `mentor`(`id`);
ALTER TABLE
    `kelas` ADD CONSTRAINT `kelas_kategori_kelas_foreign` FOREIGN KEY(`kategori_kelas`) REFERENCES `kategori_kelas`(`kelas`);
ALTER TABLE
    `detail_transaksi` ADD CONSTRAINT `detail_transaksi_paket_kelas_foreign` FOREIGN KEY(`paket_kelas`) REFERENCES `paket_kelas`(`id`);
ALTER TABLE
    `kelas` ADD CONSTRAINT `kelas_mentor_foreign` FOREIGN KEY(`mentor`) REFERENCES `mentor`(`id`);
ALTER TABLE
    `transaksi` ADD CONSTRAINT `transaksi_metode_pembayaran_foreign` FOREIGN KEY(`metode_pembayaran`) REFERENCES `metode_pembayaran`(`id`);