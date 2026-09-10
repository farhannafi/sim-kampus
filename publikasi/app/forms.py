# app/forms.py
from django import forms
from .models import Dosen
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

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

    # 👇 TAMBAHKAN CLASS INI DI BAGIAN BAWAH FORMS.PY 👇
class GantiAkunForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username baru...'})
    )
    password_baru1 = forms.CharField(
        label="Password Baru (Opsional)",
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Kosongkan jika tidak ingin mengubah password'})
    )
    password_baru2 = forms.CharField(
        label="Konfirmasi Password Baru",
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ulangi password baru'})
    )

    class Meta:
        model = User
        fields = ['username']

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password_baru1")
        p2 = cleaned_data.get("password_baru2")
        
        if p1 or p2:
            if p1 != p2:
                raise forms.ValidationError("Password baru yang Anda masukkan tidak cocok!")
        return cleaned_data