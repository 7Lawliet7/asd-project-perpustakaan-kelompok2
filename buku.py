"""
Modul Data dan Logika Bisnis - Sistem Perpustakaan Mini
Mengelola Array of Struct (list of dict) dan operasi CRUD.
"""
from datetime import date

# Array of Struct: Penyimpanan utama data buku (List of Dictionary)
koleksi_buku = []

    # Linear Search O(n): telusuri list dari indeks 0, bandingkan kode dengan case-insensitive exact match.
def cari_index_kode(kode_buku):
    """
    [Algoritma] Linear Search O(n) untuk mencari index buku.
    Menggunakan case-insensitive exact match.
    Return: index (int) jika ditemukan, -1 jika tidak.
    """
    for index, buku in enumerate(koleksi_buku):
        if buku["kode_buku"].casefold() == kode_buku.casefold():
            return index
    return -1

    # Rendering tabel dinamis: lebar tiap kolom dihitung dari string terpanjang agar output rapi.
def tampilkan_tabel(daftar_buku, tampilkan_ringkasan=False):
    """
    [UI] Menampilkan daftar buku dalam format tabel teks dinamis.
    Menggunakan algoritma pencarian lebar kolom maksimum (Max Width).
    """
    if not daftar_buku:
        print("Belum ada buku dalam koleksi.")
        return

    headers = ["No", "Kode", "Judul", "Pengarang", "Genre", "Tahun", "Status"]
    rows = []
    for nomor, buku in enumerate(daftar_buku, start=1):
        rows.append([
            str(nomor), 
            buku["kode_buku"], 
            buku["judul"], 
            buku["pengarang"],
            buku["genre"], 
            str(buku["tahun_terbit"]), 
            f'[{buku["status"].upper()}]'
        ])

    # Kalkulasi lebar kolom dinamis agar tabel rapi berapapun panjang datanya
    widths = [
        max(len(headers[i]), *(len(row[i]) for row in rows))
        for i in range(len(headers))
    ]

    def garis():
        print("+-" + "-+-".join("-" * width for width in widths) + "-+")

    def cetak_baris(values):
        print("| " + " | ".join(values[i].ljust(widths[i]) for i in range(len(values))) + " |")

    garis()
    cetak_baris(headers)
    garis()
    for row in rows:
        cetak_baris(row)
    garis()

    if tampilkan_ringkasan:
        total = len(daftar_buku)
        # List Comprehension untuk counting (O(n))
        tersedia = sum(1 for buku in daftar_buku if buku["status"] == "Tersedia")
        dipinjam = sum(1 for buku in daftar_buku if buku["status"] == "Dipinjam")
        print(f"Total buku: {total} | Tersedia: {tersedia} | Dipinjam: {dipinjam}")

def tambah_buku():
    """[F1] Menambahkan buku dengan validasi komprehensif (Input Sanitization)."""
    print("\n=== TAMBAH BUKU BARU ===")
    kode = input("Kode buku: ").strip()
    if not kode:
        print("Error: kode buku tidak boleh kosong.")
        return
    if cari_index_kode(kode) != -1:
        print(f"Error: kode buku '{kode}' sudah digunakan (Duplikasi Primary Key).")
        return

    judul = input("Judul: ").strip()
    if not judul:
        print("Error: judul tidak boleh kosong.")
        return

    pengarang = input("Pengarang: ").strip()
    if not pengarang:
        print("Error: pengarang tidak boleh kosong.")
        return

    genre = input("Genre: ").strip()
    if not genre:
        print("Error: genre tidak boleh kosong.")
        return

    tahun_input = input("Tahun terbit: ").strip()
    # Exception Handling untuk validasi tipe data (Type-Casting Guard)
    try:
        tahun = int(tahun_input)
    except ValueError:
        print("Error: tahun terbit harus berupa angka bulat.")
        return

    tahun_sekarang = date.today().year
    if tahun <= 0:
        print("Error: tahun terbit harus berupa bilangan bulat positif.")
        return
    if tahun > tahun_sekarang:
        print(f"Error: tahun terbit tidak boleh lebih besar dari {tahun_sekarang}.")
        return

    # Instansiasi Struct (Dictionary)
    buku = {
        "kode_buku": kode,
        "judul": judul,
        "pengarang": pengarang,
        "genre": genre,
        "tahun_terbit": tahun,
        "status": "Tersedia",
    }
    koleksi_buku.append(buku) # O(1) Insertion di akhir array
    print(f"Buku '{judul}' dengan kode {kode} berhasil ditambahkan ke koleksi.")

def tampilkan_semua_buku():
    """[F2] Menampilkan seluruh koleksi dan ringkasan status."""
    print("\n=== SEMUA BUKU ===")
    if not koleksi_buku:
        print("Belum ada buku dalam koleksi.")
        return
    tampilkan_tabel(koleksi_buku, tampilkan_ringkasan=True)

def cari_buku():
    """[F3] Pencarian Hybrid: Exact Match (Kode) & Partial Match (Judul)."""
    print("\n=== CARI BUKU ===")
    print("1. Berdasarkan kode buku (Exact Match)")
    print("2. Berdasarkan judul buku (Partial Match)")
    pilihan = input("Pilih mode pencarian (1/2): ").strip()
    if pilihan not in ("1", "2"):
        print("Error: pilihan pencarian harus 1 atau 2.")
        return

    kata_kunci = input("Masukkan kata kunci: ").strip()
    if not kata_kunci:
        print("Error: kata kunci tidak boleh kosong.")
        return

    if pilihan == "1":
        index = cari_index_kode(kata_kunci)
        hasil = [koleksi_buku[index]] if index != -1 else []
        jenis = "kode"
    else:
        # List Comprehension dengan filter case-insensitive
        hasil = [
            buku for buku in koleksi_buku
            if kata_kunci.casefold() in buku["judul"].casefold()
        ]
        jenis = "judul"

    if not hasil:
        print(f"Buku dengan {jenis} '{kata_kunci}' tidak ditemukan dalam koleksi.")
        return

    if pilihan == "1":
        print("Detail buku ditemukan:")
        buku = hasil[0]
        for atribut, nilai in buku.items():
            print(f"{atribut}: {nilai}")
    else:
        print(f"Jumlah hasil ditemukan: {len(hasil)}")
        tampilkan_tabel(hasil)

def update_status_buku():
    """[F4] State Transition: Toggle status pinjam/kembali dengan konfirmasi."""
    print("\n=== UPDATE STATUS BUKU ===")
    kode = input("Masukkan kode buku: ").strip()
    if not kode:
        print("Error: kode buku tidak boleh kosong.")
        return

    index = cari_index_kode(kode)
    if index == -1:
        print(f"Error: buku dengan kode '{kode}' tidak ditemukan dalam koleksi.")
        return

    buku = koleksi_buku[index]
    print(f"Judul     : {buku['judul']}")
    print(f"Pengarang : {buku['pengarang']}")
    print(f"Status saat ini: {buku['status']}")
    konfirmasi = input("Lanjutkan perubahan status? (y/n): ").strip().casefold()
    if konfirmasi != "y":
        print("Perubahan status dibatalkan.")
        return

    status_lama = buku["status"]
    if status_lama == "Tersedia":
        buku["status"] = "Dipinjam"
        print(f"Buku '{buku['judul']}' berhasil dipinjam. Status diubah: Tersedia -> Dipinjam.")
    else:
        buku["status"] = "Tersedia"
        print(f"Buku '{buku['judul']}' berhasil dikembalikan. Status diubah: Dipinjam -> Tersedia.")

def filter_buku_genre():
    """[F5] Filtering data berdasarkan kategori (Partial Match)."""
    print("\n=== FILTER BUKU BERDASARKAN GENRE ===")
    genre = input("Masukkan genre yang dicari: ").strip()
    if not genre:
        print("Error: genre tidak boleh kosong.")
        return

    # Filtering O(n): partial match case-insensitive menggunakan casefold().
    hasil = [
        buku for buku in koleksi_buku
        if genre.casefold() in buku["genre"].casefold()
    ]
    if not hasil:
        print(f"Tidak ada buku dengan genre '{genre}' dalam koleksi.")
        return

    print(f"Menampilkan buku genre: {genre} ({len(hasil)} buku ditemukan).")
    tampilkan_tabel(hasil)

def hapus_buku():
    """[F6] Deletion dengan State Validation dan konfirmasi."""
    print("\n=== HAPUS BUKU ===")
    kode = input("Masukkan kode buku yang akan dihapus: ").strip()
    if not kode:
        print("Error: kode buku tidak boleh kosong.")
        return

    index = cari_index_kode(kode)
    if index == -1:
        print(f"Buku dengan kode '{kode}' tidak ditemukan dalam koleksi.")
        return

    buku = koleksi_buku[index]
    print(f"Judul    : {buku['judul']}")
    print(f"Pengarang: {buku['pengarang']}")
    print(f"Genre    : {buku['genre']}")
    print(f"Status   : {buku['status']}")

    # State Validation: Buku dipinjam tidak boleh dihapus
    if buku["status"] == "Dipinjam":
        print(
            f"Buku '{buku['judul']}' tidak dapat dihapus karena sedang dalam status Dipinjam. "
            "Pastikan buku dikembalikan terlebih dahulu."
        )
        return

    konfirmasi = input("Yakin menghapus buku ini? (y/n): ").strip().casefold()
    if konfirmasi != "y":
        print("Penghapusan dibatalkan.")
        return

    judul = buku["judul"]
    kode_buku = buku["kode_buku"]
    del koleksi_buku[index] # O(n) Deletion (shifting elemen array)
    print(f"Buku '{judul}' dengan kode {kode_buku} berhasil dihapus dari koleksi.")