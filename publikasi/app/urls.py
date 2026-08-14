from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Halaman Dashboard (Home)
    path("", views.dashboard_view, name="dashboard"),

    # FITUR BARU: Tambah & Hapus Dosen
    path("kelola-dosen/", views.kelola_dosen_view, name="kelola_dosen"),
    path("hapus-dosen/<str:author_id>/", views.hapus_dosen_view, name="hapus_dosen"),
    path("edit-dosen/<str:author_id>/", views.edit_dosen_view, name="edit_dosen"),
    
    # Halaman Pencarian Dosen (Fitur Lama dipindah ke sini)
    path("data-dosen/", views.author_view, name="data_dosen"),
    
    # Fitur Massal
    path("update-all/", views.update_all_data, name="update_all"),
    path("download-all/", views.download_all_excel, name="download_all"),
    
    # Direktori
    path("direktori/", views.dosen_list_view, name="dosen_list"),

    # URL BARU: PERINGKAT
    path("peringkat/", views.leaderboard_view, name="leaderboard"),

    # URL BARU: DETAIL DOSEN (Menangkap ID Dosen)
    path("detail/<str:author_id>/", views.detail_dosen_view, name="detail_dosen"),

    # 👇 2. TAMBAHKAN DUA BARIS INI (URL Login & Logout)
    path("login/", auth_views.LoginView.as_view(template_name='registration/login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),

    # Fitur Massal
    path("update-all/", views.update_all_data, name="update_all"),
    path("download-all/", views.download_all_excel, name="download_all"),
    # TAMBAHKAN BARIS INI:
    path("cancel-update/", views.cancel_update_view, name="cancel_update"),
]