from django.contrib import admin
from .models import Dosen, Publikasi, StatistikSitasi

class PublikasiInline(admin.TabularInline):
    model = Publikasi
    extra = 0
    readonly_fields = ('judul', 'tahun', 'jumlah_sitasi', 'nama_jurnal')
    can_delete = False
    show_change_link = True

class StatistikInline(admin.TabularInline):
    model = StatistikSitasi
    extra = 0
    readonly_fields = ('tahun', 'jumlah')

class DosenAdmin(admin.ModelAdmin):
    list_display = ('nama', 'author_id','fakultas', 'afiliasi', 'total_sitasi', 'last_updated')
    search_fields = ('nama', 'author_id')
    # 2. Tambahkan filter samping agar bisa klik "FEB" atau "FTD"
    list_filter = ('fakultas',)
    # Ini yang bikin keren, ada tabel anak di dalam tabel induk
    inlines = [StatistikInline, PublikasiInline]

class PublikasiAdmin(admin.ModelAdmin):
    list_display = ('judul_pendek', 'dosen', 'tahun', 'jumlah_sitasi')
    search_fields = ('judul', 'dosen__nama')
    list_filter = ('tahun',)

    def judul_pendek(self, obj):
        return obj.judul[:80] + "..." if len(obj.judul) > 80 else obj.judul

admin.site.register(Dosen, DosenAdmin)
admin.site.register(Publikasi, PublikasiAdmin)
# Statistik gak perlu register terpisah, karena udah nempel di Dosen