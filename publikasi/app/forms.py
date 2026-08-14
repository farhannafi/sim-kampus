# app/forms.py
from django import forms
from .models import Dosen
from django.core.exceptions import ValidationError

class DosenForm(forms.ModelForm):
    class Meta:
        model = Dosen
        fields = ['nama', 'author_id', 'fakultas']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Lengkap Dosen'}),
            'author_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contoh: xYz123AAAAJ'}),
            'fakultas': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'author_id': 'ID Google Scholar',
            'nama': 'Nama Dosen',
            'fakultas': 'Pilih Fakultas'
        }

        # --- 2. TAMBAHKAN FUNGSI INI DI BAWAH ---
    def clean_author_id(self):
        id_input = self.cleaned_data.get('author_id')
        
        # Logika: Jika sedang EDIT dan ID-nya SAMA dengan sebelumnya, loloskan saja.
        if self.instance.pk and self.instance.pk == id_input:
            return id_input 

        # Logika: Jika ID berubah (atau tambah baru), cek dulu apakah ID itu sudah dipakai orang lain?
        if Dosen.objects.filter(author_id=id_input).exists():
            raise ValidationError("ID Dosen ini sudah terdaftar! Gunakan ID lain.")
            
        return id_input