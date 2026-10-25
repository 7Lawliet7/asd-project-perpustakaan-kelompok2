"""
Sistem Perpustakaan Mini
Tahap 1: Array of Struct (list of dict) dan enam fitur wajib.
Entry point aplikasi (CLI Menu).
Jalankan dengan: python main.py
"""

# Import modul logika dan data dari buku.py
from buku import (
    tambah_buku,
    tampilkan_semua_buku,
    cari_buku,
    update_status_buku,
    filter_buku_genre,
    hapus_buku
)

def tampilkan_menu():
    """Menampilkan antarmuka menu utama (CLI)."""
    print("\n" + "=" * 48)
    print("       SISTEM PERPUSTAKAAN MINI")
    print("=" * 48)
    print("1. Tambah buku baru")
    print("2. Tampilkan semua buku")
    print("3. Cari buku")
    print("4. Update status buku (pinjam/kembali)")
    print("5. Filter buku berdasarkan genre")
    print("6. Hapus buku")
    print("0. Keluar")
    print("-" * 48)

def main():
    """
    Main Loop: Mengendalikan alur navigasi menu.
    Menggunakan while True untuk maintain aplikasi tetap berjalan.
    """
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (0-6): ").strip()
        
        if pilihan == "1":
            tambah_buku()
        elif pilihan == "2":
            tampilkan_semua_buku()
        elif pilihan == "3":
            cari_buku()
        elif pilihan == "4":
            update_status_buku()
        elif pilihan == "5":
            filter_buku_genre()
        elif pilihan == "6":
            hapus_buku()
        elif pilihan == "0":
            print("Terima kasih. Program Sistem Perpustakaan Mini selesai.")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka 0 sampai 6.")

if __name__ == "__main__":
    main()