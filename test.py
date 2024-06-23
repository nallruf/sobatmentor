import bcrypt

# Misalnya Anda memiliki `sandi` dari request dan `stored_password` dari database
sandi = '123'
stored_password = b"$2b$12$2MHO.r5qFIzPerOVx4NgEutk5olFWR4PB1CEL/dStV/nvdw2y5m3a"

# Encode sandi ke dalam bytes menggunakan UTF-8
sandi_bytes = sandi.encode('utf-8')

print(sandi_bytes)
# Verifikasi password menggunakan bcrypt
if bcrypt.checkpw(sandi_bytes, stored_password):
    print("Password benar!")
else:
    print("Password salah.")
