
# app/scraping.py
import requests
import time
import random
from bs4 import BeautifulSoup
from django.conf import settings

# Header Browser Modern (Agar tidak diblokir)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# =======================================================================
#  1. SCRAPING MANUAL (Untuk Tampilan Web)
# =======================================================================
def scrape_profile_from_scholar(author_id):
    url = f"https://scholar.google.com/citations?user={author_id}&hl=id"
    try:
        r = requests.get(url, headers=HEADERS, timeout=30)
        r.raise_for_status()
    except Exception:
        # Jika koneksi gagal, kembalikan kosong
        return {"profile": {}, "publications": [], "graph": []}

    soup = BeautifulSoup(r.text, "html.parser")

    # --- 1. AMBIL NAMA (Wajib Ada) ---
    name_el = soup.select_one("#gsc_prf_in") or soup.select_one(".gsc_prf_in")
    if not name_el:
        return {"profile": {}, "publications": [], "graph": []}

    # --- 2. AMBIL FOTO (FIX BROKEN IMAGE) ---
    foto_el = soup.select_one("#gsc_prf_pup-img")
    foto = ""
    if foto_el:
        src = foto_el.get("src")
        if src:
            # Jika URL diawali / (relatif), tambahkan domain google
            if src.startswith("/"):
                foto = "https://scholar.google.com" + src
            else:
                foto = src 

    # --- 3. AMBIL INFO (Afiliasi, Email, Bidang) ---
    aff_text = ""
    email_text = ""
    interests = []

    # Loop semua baris info
    info_lines = soup.select(".gsc_prf_il")
    for line in info_lines:
        text = line.get_text(strip=True)
        
        # Cek Email
        if "Email" in text or "diverifikasi" in text:
            email_text = text
            continue
        
        # Cek Bidang (Cari link di dalamnya)
        links = line.select("a")
        if links:
            # Jika baris ini isinya link, ini pasti Bidang
            found = [l.get_text(strip=True) for l in links]
            if found:
                interests = found
                continue
        
        # Sisanya adalah Afiliasi
        if not aff_text:
            aff_text = text

    # FALLBACK BIDANG: Jika masih kosong, cari di container khusus
    if not interests:
        inta_div = soup.select_one(".gsc_prf_inta")
        if inta_div:
            # Coba ambil link
            links = inta_div.select("a")
            if links:
                interests = [l.get_text(strip=True) for l in links]
            else:
                # Ambil teks biasa
                interests = [inta_div.get_text(strip=True)]

    profile = {
        "nama": name_el.get_text(strip=True),
        "afiliasi": aff_text,
        "email": email_text,
        "bidang": ", ".join(interests),
        "foto": foto
    }

    # --- 4. AMBIL PUBLIKASI (FIX TABLE) ---
    publications = []
    rows = soup.select(".gsc_a_tr")
    
    for r_tr in rows:
        try:
            title_el = r_tr.select_one(".gsc_a_at")
            if not title_el: continue
            
            title = title_el.get_text(strip=True)
            link = "https://scholar.google.com" + title_el["href"] if title_el.has_attr("href") else ""
            
            # Penulis & Jurnal
            gray_cols = r_tr.select(".gs_gray")
            authors = gray_cols[0].get_text(strip=True) if len(gray_cols) > 0 else ""
            journal = gray_cols[1].get_text(strip=True) if len(gray_cols) > 1 else ""

            # Tahun
            year_el = r_tr.select_one(".gsc_a_y")
            year = year_el.get_text(strip=True) if year_el else ""

            # Sitasi
            cit_el = r_tr.select_one(".gsc_a_c")
            citations = cit_el.get_text(strip=True) if cit_el else "0"
            if not citations.isnumeric(): citations = "0"

            publications.append({
                "title": title,
                "authors": authors,
                "year": year,
                "citations": citations,
                "journal": journal,
                "link": link
            })
        except:
            continue

    # --- 5. AMBIL GRAFIK ---
    graph = []
    try:
        year_elements = soup.select(".gsc_g_t")
        score_elements = soup.select(".gsc_g_al")
        limit = min(len(year_elements), len(score_elements))
        for i in range(limit):
            y_text = year_elements[i].get_text(strip=True)
            c_text = score_elements[i].get_text(strip=True)
            if y_text.isdigit() and c_text.isdigit():
                graph.append({"year": int(y_text), "citations": int(c_text)})     
    except:
        pass

    return {
        "profile": profile,
        "publications": publications,
        "graph": graph
    }


# =======================================================================
#  2. SERPAPI FULL DATA (LOGIKA EXCEL - TETAP)
# =======================================================================
def get_full_data_via_serpapi(author_id):
    api_key = settings.SERPAPI_KEY
    base_url = "https://serpapi.com/search"

    all_pubs = []
    start = 0
    first_page_data = None 

    while True:
        params = {
            "engine": "google_scholar_author",
            "author_id": author_id,
            "hl": "id",
            "api_key": api_key,
            "start": start
        }
        res = requests.get(base_url, params=params)
        res.raise_for_status()
        data = res.json()
        
        if first_page_data is None:
            first_page_data = data
            
        pubs = data.get("articles", [])
        all_pubs.extend(pubs)

        if "next" not in data.get("serpapi_pagination", {}):
            break
            
        time.sleep(1)
        start += 20
    
    return {
        "author_json": first_page_data, 
        "all_articles": all_pubs
    }

# Helper
def get_display_data(author_id):
    return scrape_profile_from_scholar(author_id)