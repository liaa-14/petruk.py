BATAS_LULUS = 70  

def hitung_rata_rata(daftar_nilai):
    """Fungsi untuk menghitung rata-rata dari sebuah list nilai"""
    if len(daftar_nilai) == 0:
        return 0
    return sum(daftar_nilai) / len(daftar_nilai)

def tentukan_status(rata, batas=BATAS_LULUS):
    """Fungsi untuk menentukan status kelulusan berdasarkan batas nilai"""
    if rata >= batas:
        return "Lulus"
    else:
        return "Tidak Lulus"

def tampilkan_laporan(nama, daftar_nilai, batas=BATAS_LULUS):
    """Fungsi untuk menampilkan output laporan mahasiswa"""
    rata = hitung_rata_rata(daftar_nilai)  
    status = tentukan_status(rata, batas)
    
    print(f"Nama      : {nama}")
    print(f"Rata-rata : {round(rata, 2)}")
    print(f"Status    : {status}")
    print("-" * 25)
    
if __name__ == "__main__":
    print("== Pengujian hitung.py ==")
    assert abs(hitung_rata_rata([80, 75, 90]) - 81.67) < 0.01
    assert tentukan_status(70) == "Lulus"
    assert tentukan_status(69.9) == "Tidak Lulus"
    tampilkan_laporan("Budi", [80, 75, 90])
    tampilkan_laporan("Sari", [60, 65, 55, 70])
    print("Semua pengujian lolos")
