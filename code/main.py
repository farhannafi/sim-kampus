#/1/#################################################################################################
# from selenium import webdriver
# from selenium.webdriver.common.by import By

    
# options = webdriver.FirefoxOptions()
# driver = webdriver.Firefox(options=options)

# url = 'https://scholar.google.com/citations?hl=id&user=7ojrO4gAAAAJ&view_op=list_works'

# driver.get(url)

# count = driver.find_elements(By.CSS_SELECTOR, ".gsc_a_at")

# for i in range(len(count)):
#     index = i + 1
#     judul = driver.find_element(By.CSS_SELECTOR, f"tr.gsc_a_tr:nth-child({index}) > td:nth-child(1) > a")
#     dikutip = driver.find_element(By.CSS_SELECTOR, f"#gsc_a_b > tr:nth-child({index}) > td.gsc_a_c > a")
#     tahun = driver.find_element(By.CSS_SELECTOR, f"#gsc_a_b > tr:nth-child({index}) > td.gsc_a_y > span")
#     nama = driver.find_element(By.CSS_SELECTOR, "#gsc_prf_in")
#     print(f"{nama.text} -{judul.text} - {dikutip.text} - {tahun.text}\n")

# driver.quit()

#/2/ ###########################################################################################################################

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# import os

# # Inisialisasi browser Firefox
# options = webdriver.FirefoxOptions()
# options.add_argument("--headless")  # Biar tidak buka jendela browser, hapus kalau mau lihat prosesnya
# driver = webdriver.Firefox(options=options)

# # URL target
# url = 'https://scholar.google.com/citations?hl=id&user=7ojrO4gAAAAJ&view_op=list_works'
# driver.get(url)

# # Ambil data
# count = driver.find_elements(By.CSS_SELECTOR, ".gsc_a_at")
# data = []

# for i in range(len(count)):
#     index = i + 1
#     judul = driver.find_element(By.CSS_SELECTOR, f"tr.gsc_a_tr:nth-child({index}) > td:nth-child(1) > a")
#     dikutip = driver.find_element(By.CSS_SELECTOR, f"#gsc_a_b > tr:nth-child({index}) > td.gsc_a_c > a")
#     tahun = driver.find_element(By.CSS_SELECTOR, f"#gsc_a_b > tr:nth-child({index}) > td.gsc_a_y > span")
#     nama = driver.find_element(By.CSS_SELECTOR, "#gsc_prf_in")

#     data.append({
#         "Nama Dosen": nama.text,
#         "Judul Jurnal": judul.text,
#         "Dikutip Oleh": dikutip.text,
#         "Tahun": tahun.text
#     })

# # Tutup browser
# driver.quit()

# # Simpan ke Excel
# file_name = "hasil_scraping.xlsx"
# df = pd.DataFrame(data)
# df.to_excel(file_name, index=False)

# # Tampilkan lokasi file
# print("✅ File berhasil dibuat di:", os.path.abspath(file_name))

# # Buka file otomatis (Windows saja)
# os.startfile(file_name)

#/2/ ###################################################################################################################################################


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# import os

    
# options = webdriver.FirefoxOptions()
# driver = webdriver.Firefox(options=options)

# url = 'https://scholar.google.com/citations?view_op=list_works&hl=id&hl=id&user=Uw6itsEAAAAJ&pagesize=100'

# driver.get(url)

# count = driver.find_elements(By.CSS_SELECTOR, ".gsc_a_at")
# data = []

# for i in range(len(count)):
#     index = i + 1
#     judul = driver.find_element(By.CSS_SELECTOR, f"#gsc_a_b > tr:nth-child({index}) > td.gsc_a_t > a")
#     dikutip = driver.find_element(By.CSS_SELECTOR, f"#gsc_a_b > tr:nth-child({index}) > td.gsc_a_c > a")
#     tahun = driver.find_element(By.CSS_SELECTOR, f"#gsc_a_b > tr:nth-child({index}) > td.gsc_a_y > span")
#     nama = driver.find_element(By.CSS_SELECTOR, "#gsc_prf_in")

#     data.append({
#         "Nama Dosen": nama.text,
#         "Judul Jurnal": judul.text,
#         "Dikutip Oleh": dikutip.text,
#         "Tahun": tahun.text
#     })

# # Tutup browser
# driver.quit()

# # Simpan ke Excel
# file_name = "hasil_scraping1.xlsx"
# df = pd.DataFrame(data)
# df.to_excel(file_name, index=False)

# # Tampilkan lokasi file
# print("✅ File berhasil dibuat di:", os.path.abspath(file_name))

# # Buka file otomatis (Windows saja)
# os.startfile(file_name)
#/3/ ################################################################################################################

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# import os
# import time

# options = webdriver.FirefoxOptions()
# driver = webdriver.Firefox(options=options)

# url = 'https://scholar.google.com/citations?hl=id&user=3s3ntdwAAAAJ'
# driver.get(url)

# data = []

# while True:
#     next_button = driver.find_element(By.ID, "gsc_bpf_more")
#     if next_button.get_attribute("disabled") is not None:
#         break
#     else:
#         next_button.click()
#     time.sleep(3)

# count = driver.find_elements(By.CSS_SELECTOR, ".gsc_a_at")
# for i in range(len(count)):
#     index = i + 1
#     judul = driver.find_element(By.CSS_SELECTOR, f"#gsc_a_b > tr:nth-child({index}) > td.gsc_a_t > a")
#     dikutip = driver.find_element(By.CSS_SELECTOR, f"#gsc_a_b > tr:nth-child({index}) > td.gsc_a_c > a")
#     tahun = driver.find_element(By.CSS_SELECTOR, f"#gsc_a_b > tr:nth-child({index}) > td.gsc_a_y > span")
#     nama = driver.find_element(By.CSS_SELECTOR, "#gsc_prf_in")
#     print(index, judul.text, dikutip.text, tahun.text, nama.text)
#     data.append({
#         "Nama Dosen": nama.text,
#         "Judul Jurnal": judul.text,
#         "Dikutip Oleh": dikutip.text,
#         "Tahun": tahun.text
#     })


# # Tutup browser
# # driver.quit()

# # Simpan ke Excel
# file_name = "hasil_scraping3.xlsx"
# df = pd.DataFrame(data)
# df.to_excel(file_name, index=False)

# # Tampilkan lokasi file
# print("✅ File berhasil dibuat di:", os.path.abspath(file_name))

# # Buka file otomatis (Windows saja)
# os.startfile(file_name)
#/4/ ##################################################################################################

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

#     # Simpan ke Excel tanpa teks tembus ke kolom lain
#     file_name = f"{nama}_{time.time_ns()}.xlsx"
#     os.makedirs("data", exist_ok=True)
#     with pd.ExcelWriter(f"data/{file_name}", engine="xlsxwriter") as writer:
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


#/5/#######################################################################################################


# import requests
# import pandas as pd
# import time
# import openpyxl  # pastikan sudah diinstall

# # API Key SerpAPI kamu
# SERPAPI_API_KEY = "04d6f9d49abd4990df53e4a4c03dcdcb52bad2d7704c8a9ec1cd788f61d52460"

# def get_publications_for_author(user_id):
#     publications = []
#     start = 0
#     while True:
#         params = {
#             "engine": "google_scholar_author",
#             "author_id": user_id,
#             "hl": "id",
#             "sort": "pubdate",  # urutkan dari yang terbaru
#             "api_key": SERPAPI_API_KEY,
#             "start": start
#         }
#         res = requests.get("https://serpapi.com/search", params=params)
#         data = res.json()
#         pubs = data.get("articles", [])
#         if not pubs:
#             break

#         for pub in pubs:
#             direct_link = pub.get("external_link") or pub.get("link")
#             pub_data = {
#                 "Judul Penelitian": pub.get("title"),
#                 "Link Publikasi": direct_link,
#                 "Tipe Link": "PDF" if direct_link and direct_link.lower().endswith(".pdf") else "Halaman Web",
#                 "Pengarang": pub.get("authors"),
#                 "Jumlah Sitasi": pub.get("cited_by", {}).get("value", 0),
#                 "Tahun Terbit": pub.get("year"),
#                 "Nama Jurnal": pub.get("publication"),
#             }
#             publications.append(pub_data)

#         start += len(pubs)
#         time.sleep(1)

#     return publications

# # === Eksekusi Utama ===
# author_id = "MnF3ZR4AAAAJ&hl"
# author_name = "Titania Dwi Andini"

# print(f"📄 Mengambil publikasi untuk {author_name} (ID: {author_id})...")
# publications = get_publications_for_author(author_id)

# if not publications:
#     print("❌ Tidak ada publikasi ditemukan.")
# else:
#     df = pd.DataFrame(publications)
#     # Simpan ke Excel
#     file_name = "Titania Dwi Andini.xlsx"
#     df.to_excel(file_name, index=False, engine="openpyxl")
#     print(f"✅ Data berhasil disimpan ke file: {file_name}")
###############################################################################################################

import requests
import pandas as pd
import time
import openpyxl  # pastikan sudah diinstall

# API Key SerpAPI
SERPAPI_API_KEY = "1eb991a416303d0888fee987b55b42ca60ea7fd6d75f1ee0132782515a461d36"

def get_publications_for_author(user_id):
    publications = []
    start = 0
    while True:
        params = {
            "engine": "google_scholar_author",
            "author_id": user_id,
            "hl": "id",
            "sort": "pubdate",  # urutkan dari yang terbaru
            "api_key": SERPAPI_API_KEY,
            "start": start
        }
        res  = requests.get("https://serpapi.com/search", params=params)
        data = res.json()
        
        # Cek error API
        if "error" in data:
            print(f"❌ Error API: {data['error']}")
            break

        pubs = data.get("articles", [])
        if not pubs:
            break

        for pub in pubs:
            direct_link = pub.get("external_link") or pub.get("link")
            pub_data = {
                "Judul Penelitian": pub.get("title"),
                "Link Publikasi": direct_link,
                "Tipe Link": "PDF" if direct_link and direct_link.lower().endswith(".pdf") else "Halaman Web",
                "Pengarang": pub.get("authors"),
                "Jumlah Sitasi": pub.get("cited_by", {}).get("value", 0),
                "Tahun Terbit": pub.get("year"),
                "Nama Jurnal": pub.get("publication"),
            }
            publications.append(pub_data)

        start += len(pubs)
        time.sleep(1)  # jeda agar tidak kena rate limit

    return publications

# === Daftar Dosen ===
dosen_list = [
                          #DOSEN FTD
    # {"id": "rX8zRcwAAAAJ", "nama": "Abd Hadi"},                 #1
    # {"id": "Gdik0nIAAAAJ", "nama": "Abdul loh Eizzi Irsyada"},  #2
    # {"id": "CoAA0oAAAAAJ", "nama": "Achmad Noercholis"},        #3
    # {"id": "pCcxzLoAAAAJ", "nama": "Azwar Riza Habibi"},        #4
    # {"id": "Y3TMwyUAAAAJ", "nama": "Danang Arbian Sulistyo"},   #5
    # {"id": "pFQaOPQAAAAJ", "nama": "Lia Farokhah"},             #6
    # {"id": "QHoOc30AAAAJ", "nama": "Dr.Puji Subekti"},          #7
    # {"id": "BKfiMAgAAAAJ", "nama": "Tri Wahyuni"},              #8
    # {"id": "4O6_G7sAAAAJ", "nama": "Fadhli Almu'iini Ahda"},    #9
    # {"id": "5CjAe3QAAAAJ", "nama": "Faldi Hendrawan"},          #10
    # {"id": "D0KYQ0oAAAAJ", "nama": "Fransiska Sisilia Mukti"},  #11
    # {"id": "3ZEzr0EAAAAJ", "nama": "Handry Rochmad Dwi Happy"},   #12
    # {"id": "fpyqPioAAAAJ", "nama": "Ida Wahyuni"},              #13
    # {"id": "JxY0zO0AAAAJ", "nama": "Jaenal Arifin"},            #14
    # {"id": "iBHpmqMAAAAJ", "nama": "Lely Surya Wardani"},       #15
    # {"id": "SxacVdAAAAAJ", "nama": "Lilis Widayanti"},          #16
    # {"id": "jvx-Qn0AAAAJ", "nama": "Lukman Hakim"},             #17
    # {"id": "bI3v9ZMAAAAJ", "nama": "MOHAMMAD ZAINUDDIN"},       #18
    # {"id": "5aXswucAAAAJ", "nama": "mufidatul Islamiyah"},      #19
    # {"id": "4bw9WgUAAAAJ", "nama": "Muhammad Rofiq"},           #20
    # {"id": "5jjDKXcAAAAJ", "nama": "Wayong Kabalen"},           #21
    # {"id": "O35F8U4AAAAJ", "nama": "Nur Lailatul Aqromi"},      #22
    # {"id": "ObDUmdAAAAAJ", "nama": "Philip Faster Eka "},       #23
    # {"id": "AKZfru0AAAAJ", "nama": "Rina Dewi Indahsari"},      #24
    # {"id": "XlsTPe4AAAAJ", "nama": "Samsul Arifin"},            #25
    # {"id": "A3fFhoIAAAAJ", "nama": "Sean Elbert Jeremiah"},     #26
    # {"id": "Qa0jRdsAAAAJ", "nama": "Setyorini"},                #27
    # {"id": "Q3SexakAAAAJ", "nama": "Siti Nurul Afiyah"},        #28
    # {"id": "3s3ntdwAAAAJ", "nama": "Suastika Yulia Riska"},     #29
    # {"id": "dZePwOQAAAAJ", "nama": "Sunu Jatmika"},             #30
    # {"id": "MnF3ZR4AAAAJ", "nama": "Titania Dwiandini"},        #31                              
    # {"id": "c7sKLWQAAAAJ", "nama": "Vivi Aida Fitria"},         #32
    # {"id": "_7uXJTQAAAAJ", "nama": "Yogi Widya Saka Warsaa"},   #33
    # {"id": "tt5iBlUAAAAJ", "nama": "Yudistira Sapoetra"},       #34
    #                         #DOSEN FEB
    # {"id": "eQPeIZEAAAAJ", "nama": "Mariana Puspa Dewi"},       #35
    # {"id": "OQYeShEAAAAJ", "nama": "MEGA MIRASAPUTRI CAHYANTI"},#36
    # {"id": "hwzcl4gAAAAJ", "nama": "MULYANINGTYAS"},            #37
    # {"id": "0IwUvkUAAAAJ", "nama": "PIPIT ROSITA ANDARSARI"},   #38
    # {"id": "IabXZ4wAAAAJ", "nama": "RISA SANTOSO"},             #39
    # {"id": "yCUmstgAAAAJ", "nama": "Widiya Dewi Anjaningrum"},  #40
    # {"id": "WgoEnSwAAAAJ", "nama": "WIDYA ADHARIYANTY RAHAYU"}, #41
    # {"id": "RAan8qcAAAAJ", "nama": "Zainul Muchlas"},           #42
    # {"id": "HCFgmC8AAAAJ", "nama": "Mohammad Bukhori"},         #43
    # {"id": "1Sq8y4kAAAAJ", "nama": "Murtianingsih Aning"},      #44
    # {"id": "Kj8hjp8AAAAJ", "nama": "Rifki Hanif"},              #45
    # {"id": "ce0Y2tMAAAAJ", "nama": "Theresia Pradiani"},        #46
    # {"id": "w3J3wEkAAAAJ", "nama": "Tin Agustina Karnawati"},   #47
    # {"id": "iBN2CwUAAAAJ", "nama": "Widi Dewi"},                #48
    # {"id": "138bEEIAAAAJ", "nama": "Yunus Handoko"},            #49
    # {"id": "bVSBxIQAAAAJ", "nama": "fadilla cahyaningtyas"},    #50
    # {"id": "MVC7XSQAAAAJ", "nama": "Hironimus Hari Kurniawan"}, #51
    # {"id": "SxacVdAAAAAJ", "nama": "LILIS WIDAYANTI"},          #52
    # {"id": "-XwBxUgAAAAJ", "nama": "LUSSIA MARIESTI ANDRIANY"}, #53
    # {"id": "lXxg0eMAAAAJ","nama": "Abdul Aziz Muslim"},         #54
    # {"id": "300WG1AAAAAJ", "nama": "Aditya Hermawan"},          #55
    # {"id": "c7sKLWQAAAAJ", "nama": "adriani kala'lembang"},     #56
    # {"id": "iprgtdgAAAAJ", "nama": "Agus Purnomo Sidi"},        #57
    # {"id": "k6pC2rYAAAAJ", "nama": "AGUS RAHMAN ALAMSYAH"},     #58
    # {"id": "ATYgw1cAAAAJ", "nama": "AHMAD NIZAR YOGATAMA"},     #59
    # {"id": "Z0dCd9MAAAAJ", "nama": "ANIEK MURNIATI"},           #60
    # {"id": "s9uJJ_IAAAAJ", "nama": "DITYA WARDANA"},            #61
    # {"id": "_iGgAAAAJ",    "nama": "Dr.FATHORRAHMAN"},          #62
    # {"id": "Uw6itsEAAAAJ", "nama": "Ike Kusdyah Rachmawati"},   #63
    # {"id": "u3nUmSEAAAAJ", "nama": "TEGUH WIDODO"},             #64
    # {"id": "ZzuMv60AAAAJ", "nama": "justita dura"},             #65
   

]

# === Looping setiap dosen ===
for dosen in dosen_list:
    print(f"\n📄 Mengambil publikasi untuk {dosen['nama']} (ID: {dosen['id']})...")
    publications = get_publications_for_author(dosen["id"])

    if not publications:
        print(f"❌ Tidak ada publikasi ditemukan untuk {dosen['nama']}.")
    else:
        df = pd.DataFrame(publications)
        file_name = f"{dosen['nama']}.xlsx"
        df.to_excel(file_name, index=False, engine="openpyxl")
        print(f"✅ Data {dosen['nama']} berhasil disimpan ke file: {file_name}")

################################################################################BARU###############################################################

# import requests
# import pandas as pd
# import time
# import openpyxl  # pastikan sudah diinstall
# from bs4 import BeautifulSoup

# # API Key SerpAPI
# SERPAPI_API_KEY = "1eb991a416303d0888fee987b55b42ca60ea7fd6d75f1ee0132782515a461d36"

# def get_publications_for_author(user_id):
#     publications = []
#     start = 0
#     while True:
#         params = {
#             "engine": "google_scholar_author",
#             "author_id": user_id,
#             "hl": "id",
#             "sort": "pubdate",  # urutkan dari yang terbaru
#             "api_key": SERPAPI_API_KEY,
#             "start": start
#         }
#         res  = requests.get("https://serpapi.com/search", params=params)
#         data = res.json()
        
#         # Cek error API
#         if "error" in data:
#             print(f"❌ Error API: {data['error']}")
#             break

#         pubs = data.get("articles", [])
#         if not pubs:
#             break

#         for pub in pubs:
#             direct_link = pub.get("external_link") or pub.get("link")
#             # pdf_link = None

#             # # scraping tambahan citation page
#             # try:
#             #     page = requests.get(pub["link"], timeout=10)
#             #     print(page.text)
                
#             #     soup = BeautifulSoup(page.text, "html.parser")
#             #     pdf_anchor = soup.find("a", string=lambda t: t and "[PDF]" in t)
#             #     if pdf_anchor:
#             #         pdf_link = pdf_anchor["href"]

#             #         # ✅ jeda waktu dinamis (antara 2–5 detik per request)
#             #     delay = random.uniform(5, 20)
#             #     # print(f"⏳ Jeda {delay:.2f} detik sebelum lanjut...")
#             #     time.sleep(delay)

#             # except Exception as e:
#             #     print(f"❌ Gagal ambil PDF untuk {pub.get('title')}: {e}")
#             # return
#             pdf_link = None
#             # cek apakah ada resources PDF
#             if "resources" in pub:
#                 for r in pub["resources"]:
#                      if r.get("file_format", "").upper() == "PDF":
#                          pdf_link = r.get("link")
#                          break
#             # fallback ke external_link atau link
#             final_link = pdf_link if pdf_link else direct_link
#             pub_data = {
#                 "Judul Penelitian": pub.get("title"),
#                 "Link Publikasi": final_link, 
#                 "Tipe Link": "PDF" if pdf_link else "Halaman Web",
#                 "Pengarang": pub.get("authors"),
#                 "Jumlah Sitasi": pub.get("cited_by", {}).get("value", 0),
#                 "Tahun Terbit": pub.get("year"),
#                 "Nama Jurnal": pub.get("publication"),
#             }
#             publications.append(pub_data)

#         start += len(pubs)
#         time.sleep(1)  # jeda agar tidak kena rate limit

#     return publications

# # === Daftar Dosen ===
# dosen_list = [
#                           #DOSEN FTD
#     #  {"id": "rX8zRcwAAAAJ", "nama": "Abd Hadi"},                 #1
#     # {"id": "Gdik0nIAAAAJ", "nama": "Abdul loh Eizzi Irsyada"},  #2
#     # {"id": "CoAA0oAAAAAJ", "nama": "Achmad Noercholis"},        #3
#     # {"id": "pCcxzLoAAAAJ", "nama": "Azwar Riza Habibi"},        #4
#     # {"id": "Y3TMwyUAAAAJ", "nama": "Danang Arbian Sulistyo"},   #5
#     # {"id": "pFQaOPQAAAAJ", "nama": "Lia Farokhah"},             #6
#     # {"id": "QHoOc30AAAAJ", "nama": "Dr.Puji Subekti"},          #7
#     # {"id": "BKfiMAgAAAAJ", "nama": "Tri Wahyuni"},              #8
#     # {"id": "4O6_G7sAAAAJ", "nama": "Fadhli Almu'iini Ahda"},    #9
#     # {"id": "5CjAe3QAAAAJ", "nama": "Faldi Hendrawan"},          #10
#     # {"id": "D0KYQ0oAAAAJ", "nama": "Fransiska Sisilia Mukti"},  #11
#     # {"id": "3ZEzr0EAAAAJ", "nama": "Handry Rochmad Dwi Happy"}, #12
#     # {"id": "fpyqPioAAAAJ", "nama": "Ida Wahyuni"},              #13
#     # {"id": "JxY0zO0AAAAJ", "nama": "Jaenal Arifin"},            #14
#     # {"id": "iBHpmqMAAAAJ", "nama": "Lely Surya Wardani"},       #15
#     # {"id": "SxacVdAAAAAJ", "nama": "Lilis Widayanti"},          #16
#     # {"id": "jvx-Qn0AAAAJ", "nama": "Lukman Hakim"},             #17
#     # {"id": "bI3v9ZMAAAAJ", "nama": "MOHAMMAD ZAINUDDIN"},       #18
#     # {"id": "5aXswucAAAAJ", "nama": "mufidatul Islamiyah"},      #19
#     # {"id": "4bw9WgUAAAAJ", "nama": "Muhammad Rofiq"},           #20
#     # {"id": "5jjDKXcAAAAJ", "nama": "Wayong Kabalen"},           #21
#     # {"id": "O35F8U4AAAAJ", "nama": "Nur Lailatul Aqromi"},      #22
#     # {"id": "ObDUmdAAAAAJ", "nama": "Philip Faster Eka "},       #23
#     # {"id": "AKZfru0AAAAJ", "nama": "Rina Dewi Indahsari"},      #24
#     # {"id": "XlsTPe4AAAAJ", "nama": "Samsul Arifin"},            #25
#     # {"id": "A3fFhoIAAAAJ", "nama": "Sean Elbert Jeremiah"},     #26
#     # {"id": "Qa0jRdsAAAAJ", "nama": "Setyorini"},                #27
#     # {"id": "Q3SexakAAAAJ", "nama": "Siti Nurul Afiyah"},        #28
#     # {"id": "3s3ntdwAAAAJ", "nama": "Suastika Yulia Riska"},     #29
#     # {"id": "dZePwOQAAAAJ", "nama": "Sunu Jatmika"},             #30
#     # {"id": "MnF3ZR4AAAAJ", "nama": "Titania Dwiandini"},        #31                              
#     # {"id": "c7sKLWQAAAAJ", "nama": "Vivi Aida Fitria"},         #32
#     # {"id": "_7uXJTQAAAAJ", "nama": "Yogi Widya Saka Warsaa"},   #33
#     # {"id": "tt5iBlUAAAAJ", "nama": "Yudistira Sapoetra"},       #34
#     #                         #DOSEN FEB
#     # {"id": "eQPeIZEAAAAJ", "nama": "Mariana Puspa Dewi"},       #35
#     # {"id": "OQYeShEAAAAJ", "nama": "MEGA MIRASAPUTRI CAHYANTI"},#36
#     # {"id": "hwzcl4gAAAAJ", "nama": "MULYANINGTYAS"},            #37
#     # {"id": "0IwUvkUAAAAJ", "nama": "PIPIT ROSITA ANDARSARI"},   #38
#     # {"id": "IabXZ4wAAAAJ", "nama": "RISA SANTOSO"},             #39
#     # {"id": "yCUmstgAAAAJ", "nama": "Widiya Dewi Anjaningrum"},  #40
#     # {"id": "WgoEnSwAAAAJ", "nama": "WIDYA ADHARIYANTY RAHAYU"}, #41
#     # {"id": "RAan8qcAAAAJ", "nama": "Zainul Muchlas"},           #42
#     # {"id": "HCFgmC8AAAAJ", "nama": "Mohammad Bukhori"},         #43
#     # {"id": "1Sq8y4kAAAAJ", "nama": "Murtianingsih Aning"},      #44
#     # {"id": "Kj8hjp8AAAAJ", "nama": "Rifki Hanif"},              #45
#     # {"id": "ce0Y2tMAAAAJ", "nama": "Theresia Pradiani"},        #46
#     # {"id": "w3J3wEkAAAAJ", "nama": "Tin Agustina Karnawati"},   #47
#     # {"id": "iBN2CwUAAAAJ", "nama": "Widi Dewi"},                #48
#     # {"id": "138bEEIAAAAJ", "nama": "Yunus Handoko"},            #49
#     # {"id": "bVSBxIQAAAAJ", "nama": "fadilla cahyaningtyas"},    #50
#     # {"id": "MVC7XSQAAAAJ", "nama": "Hironimus Hari Kurniawan"}, #51
#     # {"id": "SxacVdAAAAAJ", "nama": "LILIS WIDAYANTI"},          #53
#     # {"id": "-XwBxUgAAAAJ", "nama": "LUSSIA MARIESTI ANDRIANY"}, #54
#     # {"id": "lXxg0eMAAAAJ","nama": "Abdul Aziz Muslim"},         #55
#     # {"id": "300WG1AAAAAJ", "nama": "Aditya Hermawan"},          #56
#     # {"id": "c7sKLWQAAAAJ", "nama": "adriani kala'lembang"},     #57
#     # {"id": "iprgtdgAAAAJ", "nama": "Agus Purnomo Sidi"},        #58
#     # {"id": "k6pC2rYAAAAJ", "nama": "AGUS RAHMAN ALAMSYAH"},     #59
#     # {"id": "ATYgw1cAAAAJ", "nama": "AHMAD NIZAR YOGATAMA"},     #60
#     # {"id": "Z0dCd9MAAAAJ", "nama": "ANIEK MURNIATI"},           #61
#     # {"id": "s9uJJ_IAAAAJ", "nama": "DITYA WARDANA"},            #62
#     # {"id": "_iGgAAAAJ",    "nama": "Dr.FATHORRAHMAN"},          #63
#      {"id": "Uw6itsEAAAAJ", "nama": "Ike Kusdyah Rachmawati"},   #64
#     # {"id": "u3nUmSEAAAAJ", "nama": "TEGUH WIDODO"},             #65
#     # {"id": "ZzuMv60AAAAJ", "nama": "justita dura"},             #66
   

# ]

# # === Looping setiap dosen ===
# for dosen in dosen_list:
#     print(f"\n📄 Mengambil publikasi untuk {dosen['nama']} (ID: {dosen['id']})...")
#     publications = get_publications_for_author(dosen["id"])

#     if not publications:
#         print(f"❌ Tidak ada publikasi ditemukan untuk {dosen['nama']}.")
#     else:
#         df = pd.DataFrame(publications)
#         file_name = f"{dosen['nama']}.xlsx"
#         df.to_excel(file_name, index=False, engine="openpyxl")
#         print(f"✅ Data {dosen['nama']} berhasil disimpan ke file: {file_name}")