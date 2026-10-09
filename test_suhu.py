import unittest
from suhu import analisis, kategori_suhu

data = [
    {"hari": "Senin", "suhu": 31},
    {"hari": "Selasa", "suhu": 33},
    {"hari": "Rabu", "suhu": 29},
    {"hari": "Kamis", "suhu": 35},
    {"hari": "Jumat", "suhu": 32},
    {"hari": "Sabtu", "suhu": 30},
    {"hari": "Minggu", "suhu": 28},
]
class TestSuhu(unittest.TestCase):

    def test_rata_rata(self):
        hasil = analisis(data)
        self.assertEqual(round(hasil["rata_rata"], 2), 31.14)

    def test_tertinggi(self):
        hasil = analisis(data)
        self.assertEqual(hasil["tertinggi"]["suhu"], 35)
        self.assertEqual(hasil["tertinggi"]["hari"], "Kamis")

    def test_terendah(self):
        hasil = analisis(data)
        self.assertEqual(hasil["terendah"]["suhu"], 28)
        self.assertEqual(hasil["terendah"]["hari"], "Minggu")

    def test_jumlah_panas(self):
        hasil = analisis(data)
        self.assertEqual(hasil["jumlah_panas"], 3)

    def test_kategori(self):
        self.assertEqual(kategori_suhu(32), "Panas")
        self.assertEqual(kategori_suhu(31), "Normal")
unittest.main()