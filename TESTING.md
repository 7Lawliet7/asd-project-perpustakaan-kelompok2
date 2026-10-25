# Checklist pengujian manual — Sistem Perpustakaan Mini

Jalankan `python main.py`, lalu lakukan pengujian berikut dan ambil screenshot terminal untuk laporan.

1. Menu utama muncul dan pilihan tidak valid ditolak.
2. F1: tambah buku valid; pastikan status awal `Tersedia`.
3. F1: uji kode kosong, kode duplikat, judul kosong, pengarang kosong, genre kosong.
4. F1: uji tahun berupa teks, nol/negatif, dan tahun lebih besar dari tahun sekarang.
5. F2: tampilkan koleksi kosong; lalu tampilkan koleksi yang sudah berisi buku dan periksa ringkasan status.
6. F3: cari kode yang ditemukan dan tidak ditemukan; cari judul dengan kata kunci sebagian dan beda kapitalisasi; uji kata kunci kosong.
7. F4: ubah status `Tersedia` menjadi `Dipinjam`, batalkan dengan `n`, lalu ubah kembali menjadi `Tersedia`; uji kode tidak ditemukan.
8. F5: filter genre dengan kapitalisasi berbeda dan kata kunci sebagian; uji genre kosong dan genre yang tidak cocok.
9. F6: hapus buku `Tersedia` setelah konfirmasi `y`; batalkan dengan `n`; pastikan buku `Dipinjam` ditolak; uji kode tidak ditemukan.
10. Pastikan setiap fitur selesai kembali ke menu utama.

Catat hasil aktual pengujian. Jangan menulis bahwa suatu skenario berhasil sebelum benar-benar dicoba.
