def baca_data(nama_file):
    data = []
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for no, baris in enumerate(file, start=1):
                if baris.strip() == "":          
                    continue
                try:
                    npm, nama, nilai = baris.strip().split(";")
                    data.append({"npm": npm, "nama": nama, "nilai": int(nilai)})
                except ValueError:           
                    print(f"[PERINGATAN] Baris {no} dilewati (tidak valid): {baris.strip()}")
    except FileNotFoundError:
        print(f"[ERROR] File '{nama_file}' belum ada. Buat dulu file-nya.")
    return data
if __name__ == "__main__":
    hasil = baca_data("nilai.txt")
    print(hasil)
    baca_data("tidak_ada.txt")
