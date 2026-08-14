# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from datas import dosen_list
# import pandas as pd
# import os
# import time
# import random

# # Setup Firefox
# options = webdriver.FirefoxOptions()
# driver = webdriver.Firefox(options=options)

# # URL profil dosen di Google Scholar
# def convertToExcel(data, nama):
#     df = pd.DataFrame(data)
#     path = 'data'
#     # Simpan ke Excel tanpa teks tembus ke kolom lain
#     file_name = f"{nama}_{time.time_ns()}.xlsx"
#     os.makedirs(path, exist_ok=True)
#     with pd.ExcelWriter(f"{path}/{file_name}", engine="xlsxwriter") as writer:
#         df.to_excel(writer, index=False, sheet_name="Data")
#         workbook = writer.book
#         worksheet = writer.sheets["Data"]

#         # Format kolom agar auto wrap teks di "Judul Jurnal"
#         wrap_format = workbook.add_format({'text_wrap': True, 'valign': 'top'})
#         worksheet.set_column('A:D', 20, wrap_format)  # Semua kolom lebar 20

#     print("✅ File berhasil dibuat di:", os.path.abspath(file_name))

# def getData(id):
#     url = f"https://scholar.google.com/citations?view_op=list_works&hl=id&hl=id&user={id}&pagesize=100"
#     driver.get(url)
#     data = []

#     # Scroll & klik tombol "More" sampai semua data muncul
#     while True:
#         try:
#             next_button = driver.find_element(By.ID, "gsc_bpf_more")
#             if next_button.get_attribute("disabled") is not None:
#                 break
#             next_button.click()
#             time.sleep(2)
#         except:
#             break

#     # Ambil semua baris publikasi
#     rows = driver.find_elements(By.CSS_SELECTOR, "#gsc_a_b > tr")

#     for row in rows:
#         judul = row.find_element(By.CSS_SELECTOR, ".gsc_a_t a").text.strip()
#         dikutip = row.find_element(By.CSS_SELECTOR, ".gsc_a_c a").text.strip()
#         tahun = row.find_element(By.CSS_SELECTOR, ".gsc_a_y span").text.strip()
#         nama = driver.find_element(By.CSS_SELECTOR, "#gsc_prf_in").text.strip()

#         # Simpan ke list
#         data.append({
#             "Nama Dosen": nama,
#             "Judul Jurnal": judul,
#             "Dikutip Oleh": dikutip,
#             "Tahun": tahun
#         })
    
#     convertToExcel(data, nama)

# def main():
#     for dosen in dosen_list:
#         getData(dosen['id'])
#         delay = random.randint(3, 8)
#         time.sleep(delay)
#     driver.quit()
# main()
###############################################################################################################

# import requests
# import pandas as pd
# import time
# # API_FARHAN
# SERPAPI_API_KEY = "1eb991a416303d0888fee987b55b42ca60ea7fd6d75f1ee0132782515a461d36"

# # Step 1: ambil publikasi dari author_id
# def get_publications_from_author(author_id):
#     params = {
#         "engine": "google_scholar_author",
#         "author_id": author_id,
#         "hl": "id",
#         "api_key": SERPAPI_API_KEY
#     }
#     res = requests.get("https://serpapi.com/search", params=params)
#     return res.json().get("articles", [])

# # Step 2: untuk setiap judul, cari lagi di google_scholar
# def get_pdf_from_title(title):
#     params = {
#         "engine": "google_scholar",
#         "q": title,
#         "hl": "id",
#         "api_key": SERPAPI_API_KEY
#     }
#     res = requests.get("https://serpapi.com/search", params=params).json()
#     if "organic_results" in res:
#         for result in res["organic_results"]:
#             if "resources" in result:
#                 for r in result["resources"]:
#                     if r.get("file_format") == "PDF":
#                         return r.get("link")
#     return None  # kalau tidak ada PDF

# # Step 3: gabungkan
# author_id = "Uw6itsEAAAAJ"  # ganti dengan author_id dosen
# print(f"📡 Mengambil publikasi untuk Author ID: {author_id} ...")

# articles = get_publications_from_author(author_id)
# print(f"✅ Jumlah publikasi ditemukan: {len(articles)}")

# data = []
# for idx, pub in enumerate(articles, start=1):
#     title = pub.get("title")
#     print(f"\n🔍 {idx}. Judul: {title}")

#     pdf_link = get_pdf_from_title(title)
#     if pdf_link:
#         print(f"   ➡️ PDF ditemukan: {pdf_link}")
#     else:
#         print("   ⚠️ PDF tidak ditemukan, pakai link alternatif")

#     link_final = pdf_link if pdf_link else pub.get("external_link") or pub.get("link")

#     data.append({
#         "Judul Penelitian": title,
#         "Link Publikasi": link_final,
#         "Tipe Link": "PDF" if pdf_link else "Halaman Web",
#         "Pengarang": pub.get("authors"),
#         "Jumlah Sitasi": pub.get("cited_by", {}).get("value", 0),
#         "Tahun Terbit": pub.get("year"),
#         "Nama Jurnal": pub.get("publication"),
#     })
#     time.sleep(2)  # jeda biar aman

# # Simpan ke Excel dengan hyperlink
# df = pd.DataFrame(data)
# output_file = "publikasi_dosen_hyperlink.xlsx"

# with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
#     df.to_excel(writer, sheet_name="Sheet1", index=False)

#     workbook  = writer.book
#     worksheet = writer.sheets["Sheet1"]

#     # buat kolom Link Publikasi jadi hyperlink
#     for row in range(1, len(df) + 1):
#         url = df.loc[row-1, "Link Publikasi"]
#         if pd.notna(url):
#             worksheet.write_url(row, 1, url, string=url)  # tampilkan url penuh

# print("\n📂 File Excel berhasil disimpan: publikasi_dosen_hyperlink.xlsx")

###########################################################################################################################################


# import requests
# import pandas as pd
# import time
# import openpyxl  # untuk save Excel

# # API Key SerpAPI
# SERPAPI_API_KEY = "1eb991a416303d0888fee987b55b42ca60ea7fd6d75f1ee0132782515a461d36"

# # === Ambil semua publikasi per dosen (pagination) ===
# def get_publications_for_author(user_id, max_results=500):
#     publications = []
#     start = 0

#     while True:
#         params = {
#             "engine": "google_scholar_author",
#             "author_id": user_id,
#             "hl": "id",
#             "sort": "pubdate",
#             "api_key": SERPAPI_API_KEY,
#             "start": start
#         }
#         res = requests.get("https://serpapi.com/search", params=params)
#         data = res.json()

#         # Cek error API
#         if "error" in data:
#             print(f"❌ Error API: {data['error']}")
#             break

#         pubs = data.get("articles", [])
#         if not pubs:
#             break

#         publications.extend(pubs)
#         start += len(pubs)

#         if len(publications) >= max_results:
#             break

#         time.sleep(2)

#     return publications

# # === Cari PDF dari judul publikasi ===
# def get_pdf_from_title(title):
#     params = {
#         "engine": "google_scholar",
#         "q": title,
#         "hl": "id",
#         "api_key": SERPAPI_API_KEY
#     }
#     res = requests.get("https://serpapi.com/search", params=params).json()

#     if "organic_results" in res:
#         for result in res["organic_results"]:
#             if "resources" in result:
#                 for r in result["resources"]:
#                     if r.get("file_format", "").upper() == "PDF":
#                         return r.get("link")
#     return None

# # === Daftar Dosen ===
# dosen_list = [
#     {"id": "Q3SexakAAAAJ", "nama": "Siti Nurul Afiyah"},
# ]

# # === Looping setiap dosen ===
# for dosen in dosen_list:
#     print(f"\n📄 Mengambil publikasi untuk {dosen['nama']} (ID: {dosen['id']})...")
#     articles = get_publications_for_author(dosen["id"])

#     if not articles:
#         print(f"❌ Tidak ada publikasi ditemukan untuk {dosen['nama']}.")
#         continue

#     data = []
#     for idx, pub in enumerate(articles, start=1):
#         title = pub.get("title")
#         print(f"\n🔍 {idx}. Judul: {title}")

#         pdf_link = get_pdf_from_title(title)
#         if pdf_link:
#             print(f"   ➡️ PDF ditemukan: {pdf_link}")
#         else:
#             print("   ⚠️ PDF tidak ditemukan, pakai link alternatif")

#         link_final = pdf_link if pdf_link else pub.get("external_link") or pub.get("link")

#         data.append({
#             "Judul Penelitian": title,
#             "Link Publikasi": link_final,
#             "Tipe Link": "PDF" if pdf_link else "Halaman Web",
#             "Pengarang": pub.get("authors"),
#             "Jumlah Sitasi": pub.get("cited_by", {}).get("value", 0),
#             "Tahun Terbit": pub.get("year"),
#             "Nama Jurnal": pub.get("publication"),
#         })

#         time.sleep(2)  # jeda supaya aman

#     # Simpan ke Excel
#     df = pd.DataFrame(data)
#     file_name = f"{dosen['nama']}.xlsx"
#     df.to_excel(file_name, index=False, engine="openpyxl")
#     print(f"✅ Data {dosen['nama']} berhasil disimpan ke file: {file_name}")

    ####################################################################### CODE UNTUK AMBIL PDF DOSEN  ####################################
# import requests
# import pandas as pd
# import time
# import openpyxl  # untuk save Excel

# # API Key SerpAPI
# SERPAPI_API_KEY = "1eb991a416303d0888fee987b55b42ca60ea7fd6d75f1ee0132782515a461d36"

# # === Ambil semua publikasi per dosen (pagination) ===
# def get_publications_for_author(user_id, max_results=500):
#     publications = []
#     start = 0

#     while True:
#         params = {
#             "engine": "google_scholar_author",
#             "author_id": user_id,
#             "hl": "id",
#             "sort": "pubdate",
#             "api_key": SERPAPI_API_KEY,
#             "start": start
#         }
#         res = requests.get("https://serpapi.com/search", params=params)
#         data = res.json()

#         # Cek error API
#         if "error" in data:
#             print(f"❌ Error API: {data['error']}")
#             break

#         pubs = data.get("articles", [])
#         if not pubs:
#             break

#         publications.extend(pubs)
#         start += len(pubs)

#         if len(publications) >= max_results:
#             break

#         time.sleep(2)

#     return publications

# # === Cari PDF dari judul publikasi ===
# def get_pdf_from_title(title):
#     params = {
#         "engine": "google_scholar",
#         "q": title,
#         "hl": "id",
#         "api_key": SERPAPI_API_KEY
#     }
#     res = requests.get("https://serpapi.com/search", params=params).json()

#     if "organic_results" in res:
#         for result in res["organic_results"]:
#             if "resources" in result:
#                 for r in result["resources"]:
#                     if r.get("file_format", "").upper() == "PDF":
#                         return r.get("link")
#     return None

# # === Ambil detail tambahan dari citation_id ===
# def get_details_from_citation(citation_id):
#     params = {
#         "engine": "google_scholar_cite",
#         "citation_id": citation_id,
#         "hl": "id",
#         "api_key": SERPAPI_API_KEY
#     }
#     res = requests.get("https://serpapi.com/search", params=params).json()

#     # Simpan hanya field yang ada
#     return {
#         "Pengarang Lengkap": res.get("author"),
#         "Tanggal Terbit Lengkap": res.get("publication_date"),
#         "Halaman": res.get("pages"),
#         "Total Kutipan Lengkap": res.get("total_citations")
#     }

# # === Daftar Dosen ===
# dosen_list = [
#     {"id": "IabXZ4wAAAAJ", "nama": "RISA SANTOSO"},
# ]

# # === Looping setiap dosen ===
# for dosen in dosen_list:
#     print(f"\n📄 Mengambil publikasi untuk {dosen['nama']} (ID: {dosen['id']})...")
#     articles = get_publications_for_author(dosen["id"])

#     if not articles:
#         print(f"❌ Tidak ada publikasi ditemukan untuk {dosen['nama']}.")
#         continue

#     data = []
#     for idx, pub in enumerate(articles, start=1):
#         title = pub.get("title")
#         citation_id = pub.get("citation_id")
#         print(f"\n🔍 {idx}. Judul: {title}")

#         # Cari link PDF
#         pdf_link = get_pdf_from_title(title)
#         if pdf_link:
#             print(f"   ➡️ PDF ditemukan: {pdf_link}")
#         else:
#             print("   ⚠️ PDF tidak ditemukan, pakai link alternatif")

#         link_final = pdf_link if pdf_link else pub.get("external_link") or pub.get("link")

#         # Ambil detail tambahan (jika ada citation_id)
#         extra = {}
#         if citation_id:
#             extra = get_details_from_citation(citation_id)
#             time.sleep(2)

#         # Gabungkan ke satu baris data
#         row = {
#             "Judul Penelitian": title,
#             "Link Publikasi": link_final,
#             "Tipe Link": "PDF" if pdf_link else "Halaman Web",
#             "Pengarang": pub.get("authors"),
#             "Jumlah Sitasi": pub.get("cited_by", {}).get("value", 0),
#             "Tahun Terbit": pub.get("year"),
#             "Nama Jurnal": pub.get("publication"),
#         }
#         row.update(extra)

#         data.append(row)
#         time.sleep(2)

#     # Simpan ke Excel (1 sheet)
#     df = pd.DataFrame(data)
#     file_name = f"{dosen['nama']}_publikasi.xlsx"
#     df.to_excel(file_name, index=False, engine="openpyxl")
#     print(f"✅ Data {dosen['nama']} berhasil disimpan ke file: {file_name}")


############################################################################################################################################################

                                                                        #UJU COBA BARU
import requests
import pandas as pd
import time
import openpyxl

SERPAPI_API_KEY = "1eb991a416303d0888fee987b55b42ca60ea7fd6d75f1ee0132782515a461d36"

def get_author_info(user_id):
    params = {
        "engine": "google_scholar_author",
        "author_id": user_id,
        "hl": "id",
        "api_key": SERPAPI_API_KEY
    }
    res = requests.get("https://serpapi.com/search", params=params)
    return res.json()

def get_publications_for_author(user_id):
    publications = []
    start = 0

    while True:
        params = {
            "engine": "google_scholar_author",
            "author_id": user_id,
            "hl": "id",
            "api_key": SERPAPI_API_KEY,
            "start": start
        }
        res = requests.get("https://serpapi.com/search", params=params)
        data = res.json()
        pubs = data.get("articles", [])
        if not pubs:
            break

        for pub in pubs:
            link = pub.get("external_link") or pub.get("link")
            publications.append({
                "Judul Penelitian": pub.get("title"),
                "Link Publikasi": link,
                "Tipe Link": "PDF" if link and link.endswith(".pdf") else "Halaman Web",
                "Pengarang": pub.get("authors"),
                "Jumlah Sitasi": pub.get("cited_by", {}).get("value", 0),
                "Tahun Terbit": pub.get("year"),
                "Nama Jurnal": pub.get("publication")
            })

        start += len(pubs)
        time.sleep(1)

    return publications

def extract_citation_stats(author_info):
    """Ambil total kutipan, h-index, dan i10-index dari struktur JSON SerpAPI (versi Indonesia)."""
    cited_by = author_info.get("cited_by", {})
    table = cited_by.get("table", [])

    total_kutipan = 0
    h_index = 0
    i10_index = 0

    try:
        total_kutipan = table[0].get("kutipan", {}).get("all", 0)
        h_index = table[1].get("indeks_h", {}).get("all", 0)
        i10_index = table[2].get("indeks_i10", {}).get("all", 0)
    except Exception:
        pass

    return total_kutipan, h_index, i10_index

# === Daftar Dosen ===
dosen_list = [
    {"id": "3ZEzr0EAAAAJ", "nama": "Handry Rochmad Dwi Happy"},
    {"id": "IabXZ4wAAAAJ", "nama": "RISA SANTOSO"},
]

for dosen in dosen_list:
    print(f"\n📄 Mengambil data untuk {dosen['nama']} (ID: {dosen['id']})...")

    author_info = get_author_info(dosen["id"])
    total_kutipan, h_index, i10_index = extract_citation_stats(author_info)
    publications = get_publications_for_author(dosen["id"])

    if not publications:
        print(f"⚠️ Tidak ada publikasi ditemukan untuk {dosen['nama']}.")
        continue

    # Buat DataFrame publikasi
    df_pub = pd.DataFrame(publications)

    # Tambahkan info dosen di sheet baru
    df_info = pd.DataFrame({
        "Nama Dosen": [author_info.get("author", {}).get("name", dosen["nama"])],
        "Afiliasi": [author_info.get("author", {}).get("affiliations", "")],
        "Email": [author_info.get("author", {}).get("email", "")],
        "Bidang": [", ".join([i.get("title", "") for i in author_info.get("author", {}).get("interests", [])])],
        "Total Kutipan": [total_kutipan],
        "h-index": [h_index],
        "i10-index": [i10_index]
    })

    # Simpan ke Excel
    file_name = f"{dosen['nama']}_publikasi.xlsx"
    with pd.ExcelWriter(file_name, engine="openpyxl") as writer:
        df_info.to_excel(writer, index=False, sheet_name="Profil Dosen")
        df_pub.to_excel(writer, index=False, sheet_name="Daftar Publikasi")

    print(f"✅ Data {dosen['nama']} berhasil disimpan ke file: {file_name}")
    print(f"📊 Total Kutipan: {total_kutipan} | h-index: {h_index} | i10-index: {i10_index}")










