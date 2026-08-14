from django.db import models

# 1. TABEL UTAMA: DOSEN
class Dosen(models.Model):
    # --- [BAGIAN BARU 1] PILIHAN FAKULTAS ---
    JENIS_FAKULTAS = [
        ('FEB', 'Fakultas Ekonomi & Bisnis'),
        ('FTD', 'Fakultas Teknik & Desain'),
    ]
    author_id = models.CharField(max_length=50, primary_key=True)
    nama = models.CharField(max_length=255)
    # --- [BAGIAN BARU 2] KOLOM FAKULTAS ---
    # Kita kasih default='FTD' supaya data lama gak error saat migrasi
    fakultas = models.CharField(max_length=3, choices=JENIS_FAKULTAS, default='FTD')
    afiliasi = models.CharField(max_length=255, null=True, blank=True)
    foto_url = models.URLField(max_length=500, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    bidang_minat = models.CharField(max_length=500, null=True, blank=True)
    
    # Data Statistik Ringkas
    total_sitasi = models.IntegerField(default=0)
    h_index = models.IntegerField(default=0)
    i10_index = models.IntegerField(default=0)
    
    last_updated = models.DateTimeField(auto_now=True)

# --- STATISTIK (SEJAK 2020) - BARU! ---
    total_sitasi_sejak_2020 = models.IntegerField(default=0)
    h_index_sejak_2020 = models.IntegerField(default=0)
    i10_index_sejak_2020 = models.IntegerField(default=0)
    

    def __str__(self):
        return self.nama

# 2. TABEL ANAK: PUBLIKASI (One-to-Many ke Dosen)
class Publikasi(models.Model):
    dosen = models.ForeignKey(Dosen, on_delete=models.CASCADE, related_name='publikasi')
    judul = models.CharField(max_length=500)
    link_jurnal = models.URLField(max_length=500, null=True, blank=True)
    authors = models.CharField(max_length=500, null=True, blank=True)
    nama_jurnal = models.CharField(max_length=255, null=True, blank=True)
    tahun = models.CharField(max_length=10, null=True, blank=True) # Pakai Char karena kadang isinya "-"
    jumlah_sitasi = models.IntegerField(default=0)

    def __str__(self):
        return self.judul[:50]

# 3. TABEL ANAK: STATISTIK SITASI PER TAHUN (Untuk Grafik)
class StatistikSitasi(models.Model):
    dosen = models.ForeignKey(Dosen, on_delete=models.CASCADE, related_name='statistik')
    tahun = models.IntegerField()
    jumlah = models.IntegerField(default=0)

    class Meta:
        ordering = ['tahun'] # Biar grafik urut tahunnya