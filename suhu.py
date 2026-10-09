BATAS_PANAS = 32  

def baca_suhu(nama_file):
    data_suhu = []
    
    try:
        with open(nama_file, "r", encoding="utf-8") as file:   
            for no, baris in enumerate(file, start=1):
                teks = baris.strip()
                
                if not teks:
                    continue
                try:
                    hari, suhu = teks.split(";")
                    suhu = suhu.upper().replace("C", "").strip()   
                    data_suhu.append({"hari": hari.strip(), "suhu": int(suhu)})
                except ValueError:
                    print(f"[PERINGATAN] Baris {no} dilewati (format tidak valid): '{teks}'")
                    
    except FileNotFoundError:
        print(f"[ERROR] File '{nama_file}' tidak ditemukan. Pastikan file sudah dibuat.")
        
    return data_suhu

def hitung_rata_rata(*suhu):
    return sum(suhu) / len(suhu)

def kategori_suhu(suhu, batas=BATAS_PANAS):
    if suhu >= batas:
        return "Panas"
    else:
        return "Normal"

def analisis(data, batas_panas=BATAS_PANAS):
    list_suhu = [d["suhu"] for d in data]
    rata = hitung_rata_rata(*list_suhu)      
    tertinggi = max(data, key=lambda d: d["suhu"])           
    terendah = min(data, key=lambda d: d["suhu"])            
    kategori = []
    for d in data:
        status = kategori_suhu(d["suhu"], batas=batas_panas)
        kategori.append({
            "hari": d["hari"], 
            "suhu": d["suhu"],
            "kategori": status
        })
        
    jumlah_panas = 0
    for k in kategori:
        if k["kategori"] == "Panas":
            jumlah_panas += 1
            
    return {
        "rata_rata": rata, 
        "tertinggi": tertinggi, 
        "terendah": terendah,
        "kategori": kategori, 
        "jumlah_panas": jumlah_panas
    }

def buat_teks_laporan(hasil):
    baris = []
    baris.append("LAPORAN SUHU MINGGUAN")
    baris.append("=" * 28)
    baris.append(f"Rata-rata suhu : {hasil['rata_rata']:.2f} C")
    baris.append(f"Suhu tertinggi : {hasil['tertinggi']['suhu']} C ({hasil['tertinggi']['hari']})")
    baris.append(f"Suhu terendah  : {hasil['terendah']['suhu']} C ({hasil['terendah']['hari']})")
    baris.append("-" * 28)
    
    for k in hasil["kategori"]:
        baris.append(f"{k['hari']:<8}: {k['suhu']} C -> {k['kategori']}")
        
    baris.append("-" * 28)
    baris.append(f"Jumlah hari Panas: {hasil['jumlah_panas']}")
    
    return "\n".join(baris) + "\n"

def tulis_laporan(nama_file, teks):
    with open(nama_file, "w", encoding="utf-8") as file:     
        file.write(teks)
    print(teks)

def main():
    data = baca_suhu("suhu.txt")
    if not data:
        return
    hasil = analisis(data, batas_panas=32)                   
    laporan = buat_teks_laporan(hasil)
    tulis_laporan("laporan_suhu.txt", laporan)

if __name__ == "__main__":
    main()
