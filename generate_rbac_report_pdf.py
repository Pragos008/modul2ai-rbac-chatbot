"""
Script Generator Laporan Praktikum Pertemuan 9 & 10 (Format PDF)
Topik: Mengembangkan Chatbot dengan Role-Based Access Control (RBAC)
Mata Kuliah: Kecerdasan Artifisial dan Penerapannya
Mahasiswa: Mochammad Dailam Al Muhibi (NIM: 1204230037)
Dosen Pengampu: M. Nizar P. Ma'ady, S.Kom., M.IM., M.Kom.
"""

import os
import json
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# === PATH CONFIGURATION ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AI_ROOT = os.path.dirname(BASE_DIR)

PDF_OUTPUT_1 = os.path.join(
    AI_ROOT,
    "Laporan_Praktikum_Pertemuan_9_10_RBAC_Chatbot_Mochammad_Dailam_Al_Muhibi_1204230037.pdf"
)
PDF_OUTPUT_2 = os.path.join(
    BASE_DIR,
    "Laporan_Praktikum_Pertemuan_9_10_RBAC_Chatbot_Mochammad_Dailam_Al_Muhibi_1204230037.pdf"
)

# === FONTS SETUP ===
WIN_FONTS = r"C:\Windows\Fonts"
try:
    pdfmetrics.registerFont(TTFont("TNR", os.path.join(WIN_FONTS, "times.ttf")))
    pdfmetrics.registerFont(TTFont("TNR-Bold", os.path.join(WIN_FONTS, "timesbd.ttf")))
    pdfmetrics.registerFont(TTFont("TNR-Italic", os.path.join(WIN_FONTS, "timesi.ttf")))
    pdfmetrics.registerFont(TTFont("TNR-BoldItalic", os.path.join(WIN_FONTS, "timesbi.ttf")))
    pdfmetrics.registerFont(TTFont("Consolas", os.path.join(WIN_FONTS, "consola.ttf")))
    FONT_BODY = "TNR"
    FONT_BOLD = "TNR-Bold"
    FONT_ITALIC = "TNR-Italic"
    FONT_CODE = "Consolas"
except Exception:
    FONT_BODY = "Times-Roman"
    FONT_BOLD = "Times-Bold"
    FONT_ITALIC = "Times-Italic"
    FONT_CODE = "Courier"


def get_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name="DocTitle",
        fontName=FONT_BOLD,
        fontSize=15,
        alignment=TA_CENTER,
        spaceAfter=5,
        leading=19,
        textColor=colors.HexColor("#111827")
    ))

    styles.add(ParagraphStyle(
        name="DocSubtitle",
        fontName=FONT_BODY,
        fontSize=11.5,
        alignment=TA_CENTER,
        spaceAfter=4,
        leading=16,
        textColor=colors.HexColor("#374151")
    ))

    styles.add(ParagraphStyle(
        name="Heading1Custom",
        fontName=FONT_BOLD,
        fontSize=12.5,
        spaceBefore=16,
        spaceAfter=7,
        leading=16,
        textColor=colors.HexColor("#1E3A8A")
    ))

    styles.add(ParagraphStyle(
        name="Heading2Custom",
        fontName=FONT_BOLD,
        fontSize=11,
        spaceBefore=11,
        spaceAfter=5,
        leading=14,
        textColor=colors.HexColor("#1F2937")
    ))

    styles.add(ParagraphStyle(
        name="BodyTextNatural",
        fontName=FONT_BODY,
        fontSize=11,
        alignment=TA_JUSTIFY,
        spaceAfter=6,
        leading=15.5,
        firstLineIndent=28
    ))

    styles.add(ParagraphStyle(
        name="BodyNoIndent",
        fontName=FONT_BODY,
        fontSize=11,
        alignment=TA_JUSTIFY,
        spaceAfter=5,
        leading=15.5,
        firstLineIndent=0
    ))

    styles.add(ParagraphStyle(
        name="BulletItem",
        fontName=FONT_BODY,
        fontSize=10.5,
        alignment=TA_JUSTIFY,
        spaceAfter=3,
        leading=14.5,
        leftIndent=24,
        bulletIndent=12
    ))

    styles.add(ParagraphStyle(
        name="CodeSnippet",
        fontName=FONT_CODE,
        fontSize=8.2,
        alignment=TA_LEFT,
        spaceAfter=4,
        leading=11,
        leftIndent=12,
        backColor=colors.HexColor("#F8FAFC"),
        borderColor=colors.HexColor("#E2E8F0"),
        borderWidth=0.5,
        borderPadding=5
    ))

    styles.add(ParagraphStyle(
        name="CaptionText",
        fontName=FONT_ITALIC,
        fontSize=9.5,
        alignment=TA_CENTER,
        spaceAfter=9,
        spaceBefore=4,
        leading=12,
        textColor=colors.HexColor("#4B5563")
    ))

    styles.add(ParagraphStyle(
        name="TableCellText",
        fontName=FONT_BODY,
        fontSize=9.5,
        alignment=TA_LEFT,
        leading=13
    ))

    styles.add(ParagraphStyle(
        name="TableCellBold",
        fontName=FONT_BOLD,
        fontSize=9.5,
        alignment=TA_LEFT,
        leading=13
    ))

    return styles


def build_cover(styles):
    story = []
    story.append(Spacer(1, 1.8 * cm))
    story.append(Paragraph("LAPORAN PRAKTIKUM INDIVIDU", styles["DocTitle"]))
    story.append(Paragraph("KECERDASAN ARTIFISIAL DAN PENERAPANNYA", styles["DocTitle"]))
    story.append(Spacer(1, 0.4 * cm))
    story.append(HRFlowable(width="65%", thickness=1.5, color=colors.HexColor("#1E3A8A"), spaceAfter=14))

    story.append(Paragraph("<b>PERTEMUAN 9 & 10</b>", ParagraphStyle(
        "CoverTag", parent=styles["DocSubtitle"], fontName=FONT_BOLD, fontSize=12, textColor=colors.HexColor("#1E3A8A")
    )))
    story.append(Paragraph(
        "<b>MENGEMBANGKAN CHATBOT DENGAN ROLE-BASED ACCESS CONTROL (RBAC)</b><br/>"
        "Implementasi Custom RAG Berbasis FastAPI, SQLite, dan Groq Cloud LLM",
        styles["DocSubtitle"]
    ))

    story.append(Spacer(1, 1.6 * cm))

    info = [
        ["Nama Mahasiswa", ":", "Mochammad Dailam Al Muhibi"],
        ["NIM", ":", "1204230037"],
        ["Kelas", ":", "SS1SI-06-REG-01"],
        ["Program Studi", ":", "S1 Sistem Informasi"],
        ["Fakultas", ":", "Fakultas Rekayasa Industri (FRI)"],
        ["Dosen Pengampu", ":", "M. Nizar P. Ma'ady, S.Kom., M.IM., M.Kom."],
        ["Asisten Praktikum", ":", "Muhammad Baihaqi / Mohamad Fikri Isfahani"],
        ["Tanggal Praktikum", ":", "November 2026"],
    ]

    t = Table(info, colWidths=[4.2 * cm, 0.5 * cm, 9.3 * cm])
    t.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), FONT_BODY),
        ("FONTSIZE", (0, 0), (-1, -1), 10.5),
        ("FONTNAME", (0, 0), (0, -1), FONT_BOLD),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
        ("TOPPADDING", (0, 0), (-1, -1), 4.5),
    ]))
    story.append(t)

    story.append(Spacer(1, 2.2 * cm))
    story.append(Paragraph("PROGRAM STUDI S1 SISTEM INFORMASI", ParagraphStyle(
        "CoverUniv1", parent=styles["DocTitle"], fontSize=12, textColor=colors.HexColor("#374151")
    )))
    story.append(Paragraph("TELKOM UNIVERSITY SURABAYA", ParagraphStyle(
        "CoverUniv2", parent=styles["DocTitle"], fontSize=12, textColor=colors.HexColor("#111827")
    )))
    story.append(Paragraph("Tahun Ajaran 2026/2027", styles["DocSubtitle"]))
    story.append(PageBreak())
    return story


def build_report_content(styles):
    story = []
    B = styles["BodyTextNatural"]
    BN = styles["BodyNoIndent"]
    H1 = styles["Heading1Custom"]
    H2 = styles["Heading2Custom"]
    BL = styles["BulletItem"]
    CS = styles["CodeSnippet"]
    CAP = styles["CaptionText"]

    # ==========================================
    # 1. TUJUAN PRAKTIKUM
    # ==========================================
    story.append(Paragraph("1. Tujuan Praktikum", H1))
    story.append(Paragraph(
        "Pada praktikum Pertemuan 9 & 10 ini, saya mengembangkan sebuah sistem chatbot "
        "Retrieval-Augmented Generation (RAG) yang dilengkapi mekanisme Role-Based Access Control (RBAC). "
        "Tujuan utama dari praktikum ini adalah untuk memastikan bahwa asisten AI tidak membagikan informasi "
        "secara sembarangan kepada semua pengguna, melainkan membatasi akses potongan pengetahuan (chunks) "
        "sesuai dengan peran atau hak akses yang dimiliki oleh pengguna tersebut.",
        B
    ))
    story.append(Paragraph("Tujuan spesifik yang saya capai dalam praktikum ini meliputi:", B))
    tujuan_list = [
        "Merancang dan membangun backend REST API terintegrasi menggunakan framework FastAPI dan SQLite.",
        "Menerapkan Role-Based Access Control (RBAC) pada basis data dokumen, sehingga setiap dokumen hanya dapat dibaca oleh role yang telah diizinkan (misalnya role 'mahasiswa' dan 'dosen').",
        "Mengimplementasikan pipeline ekstraksi teks multi-format (PDF, DOCX, TXT) serta algoritma hybrid retrieval yang memadukan cosine similarity pada representasi vektor dengan lexical matching bonus.",
        "Mengintegrasikan layanan Groq Cloud LLM (model Qwen 2.5 32B) untuk pembangkitan respons yang grounded dan bebas halusinasi dengan menyertakan rujukan dokumen sumber.",
        "Membuktikan pemisahan akses data secara ketat: dokumen sensitif internal dosen tidak boleh bocor saat ditanyakan oleh role mahasiswa, namun dapat dijawab dengan akurat saat ditanyakan oleh role dosen.",
        "Menyiapkan konfigurasi deployment ke platform cloud (Railway / Render) menggunakan Dockerfile, Procfile, dan railway.toml."
    ]
    for idx, item in enumerate(tujuan_list, 1):
        story.append(Paragraph(f"{idx}. {item}", BL))

    # ==========================================
    # 2. DASAR TEORI
    # ==========================================
    story.append(Paragraph("2. Dasar Teori", H1))

    story.append(Paragraph("2.1. Role-Based Access Control (RBAC) pada Sistem RAG", H2))
    story.append(Paragraph(
        "Role-Based Access Control (RBAC) merupakan mekanisme pembatasan akses sistem kepada pengguna yang sah "
        "berdasarkan peran (role) yang ditetapkan dalam suatu organisasi. Pada sistem RAG konvensional, semua "
        "dokumen yang diindeks ke dalam vector store biasanya dapat diakses oleh siapa saja yang mengajukan pertanyaan. "
        "Kelemahan fatal dari pendekatan tanpa RBAC ini adalah potensi kebocoran dokumen rahasia atau internal, "
        "misalnya pedoman penilaian dosen, data finansial, atau data administrasi sensitif yang ikut terbaca "
        "saat mahasiswa umum mengajukan pertanyaan.",
        B
    ))
    story.append(Paragraph(
        "Dalam sistem RAG berbasis RBAC yang saya bangun ini, kontrol akses diterapkan langsung pada layer database SQL "
        "sebelum pencarian semantik dijalankan. Tabel relasi <i>document_roles</i> memetakan setiap dokumen ke satu atau "
        "beberapa role ID. Query retrieval secara otomatis memfilter clause SQL: "
        "<code>WHERE is_active = 1 AND dr.role_id = :user_role_id</code>. Dengan pendekatan ini, vector chunks dari dokumen "
        "yang tidak berhak diakses sama sekali tidak akan pernah dimasukkan ke dalam memori pencarian kemiripan kosinus, "
        "sehingga keamanan dokumen terjamin secara deterministik pada tingkat basis data.",
        B
    ))

    story.append(Paragraph("2.2. Pipeline Ekstraksi Multi-Format dan Hybrid Search", H2))
    story.append(Paragraph(
        "Sistem dilengkapi modul ekstraksi otomatis yang mengenali format PDF (menggunakan PyPDF), DOCX (python-docx), "
        "dan file teks biasa (TXT/Markdown). Teks yang diekstrak kemudian dipotong menggunakan teknik chunking adaptif "
        "yang mempertahankan struktur tabel dan batasan paragraf. Untuk pencarian relevansi, sistem menggunakan "
        "pendekatan <i>Hybrid Search</i> yang menggabungkan kemiripan kosinus dari token-frequency vector 384 dimensi "
        "dengan bobot leksikal (exact keyword bonus). Kombinasi ini memberikan hasil pencarian yang sangat cepat "
        "pada SQLite tanpa ketergantungan model embedding eksternal yang berat di lingkungan server.",
        B
    ))

    story.append(Paragraph("2.3. Autentikasi Admin dan Pemantauan Kuota Groq", H2))
    story.append(Paragraph(
        "Panel administrasi dilindungi menggunakan JSON Web Token (JWT) dengan algoritma enkripsi HS256 dan "
        "hashing kata sandi berbasis PBKDF2-HMAC-SHA256 dengan 100.000 iterasi. Selain itu, sistem mencatat "
        "setiap konsumsi token dan waktu respons ke tabel <i>groq_usage_logs</i>, sehingga administrator "
        "dapat memantau penggunaan limit API (Requests Per Day dan Tokens Per Minute) secara transparan.",
        B
    ))

    # ==========================================
    # 3. ALAT DAN BAHAN
    # ==========================================
    story.append(Paragraph("3. Alat dan Bahan", H1))

    sw_rows = [
        [Paragraph("<b>Komponen</b>", styles["TableCellBold"]),
         Paragraph("<b>Spesifikasi / Pustaka</b>", styles["TableCellBold"]),
         Paragraph("<b>Peran dalam Sistem</b>", styles["TableCellBold"])],
        [Paragraph("Bahasa Pemrograman", styles["TableCellText"]),
         Paragraph("Python 3.12 (64-bit)", styles["TableCellText"]),
         Paragraph("Lingkungan eksekusi utama logika aplikasi", styles["TableCellText"])],
        [Paragraph("Web Framework API", styles["TableCellText"]),
         Paragraph("FastAPI 0.115 + Uvicorn 0.32", styles["TableCellText"]),
         Paragraph("Penyedia REST API dan routing antarmuka web", styles["TableCellText"])],
        [Paragraph("Basis Data Relasional", styles["TableCellText"]),
         Paragraph("SQLite 3 (PRAGMA foreign_keys)", styles["TableCellText"]),
         Paragraph("Penyimpanan relasi dokumen, roles, chunk, dan logs", styles["TableCellText"])],
        [Paragraph("Autentikasi & Enkripsi", styles["TableCellText"]),
         Paragraph("PyJWT 2.15 + hashlib PBKDF2", styles["TableCellText"]),
         Paragraph("Proteksi akses endpoint panel admin berbasis token", styles["TableCellText"])],
        [Paragraph("Ekstraktor Dokumen", styles["TableCellText"]),
         Paragraph("pypdf, python-docx, openpyxl", styles["TableCellText"]),
         Paragraph("Pengurai teks dan tabel multi-format", styles["TableCellText"])],
        [Paragraph("AI Model Service (LLM)", styles["TableCellText"]),
         Paragraph("Groq Cloud SDK (Qwen 2.5 32B)", styles["TableCellText"]),
         Paragraph("Pembangkitan jawaban berbasis konteks referensi", styles["TableCellText"])],
        [Paragraph("Frontend Interface", styles["TableCellText"]),
         Paragraph("HTML5, Tailwind CSS, Vanilla JS", styles["TableCellText"]),
         Paragraph("UI Chatbot Publik dan Dashboard Manajemen Admin", styles["TableCellText"])],
    ]
    t_sw = Table(sw_rows, colWidths=[3.8 * cm, 4.4 * cm, 6.8 * cm])
    t_sw.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1E3A8A")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D1D5DB")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F9FAFB")]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(t_sw)
    story.append(Paragraph("Tabel 1. Perangkat lunak, pustaka, dan layanan yang digunakan", CAP))

    story.append(Paragraph("3.2. Dokumen Dataset dan Pengetahuan Penunjang", H2))
    story.append(Paragraph(
        "Dataset yang diindeks ke dalam basis pengetahuan sistem dibagi menjadi dua kategori akses:",
        B
    ))
    doc_data = [
        "<b>Kategori Publik Mahasiswa:</b> (1) <i>SK-TAK-2022.pdf</i> (Pedoman TAK 2022), (2) <i>SK TAK TUNC 2025.pdf</i> (Aturan TAK Terbaru 2025), (3) <i>Alur_Menghubungi_SSC.txt</i> (Prosedur layanan mahasiswa), dan (4) <i>SSC_Operating_Hours.txt</i> (Jam operasional SSC).",
        "<b>Kategori Sensitif Khusus Dosen:</b> Dokumen <i>Pedoman_Penilaian_dan_Kebijakan_Internal_Dosen.txt</i> yang memuat formula persentase pembobotan nilai (Kehadiran 10%, Tugas 20%, UTS 30%, UAS 40%), standar rentang indeks mutu huruf, dan batas nilai maksimal remedial (kategori C, skor 55)."
    ]
    for d in doc_data:
        story.append(Paragraph(f"• {d}", BL))

    # ==========================================
    # 4. PERANCANGAN DAN IMPLEMENTASI
    # ==========================================
    story.append(Paragraph("4. Perancangan dan Implementasi Sistem", H1))

    story.append(Paragraph("4.1. Struktur Modul dan Skema Basis Data", H2))
    story.append(Paragraph(
        "Aplikasi disusun dalam struktur proyek modular bernama <b>modul2ai</b> yang rapi dan memisahkan "
        "tanggung jawab setiap komponen:",
        B
    ))

    struct_text = """modul2ai/
├── app/
│   ├── auth.py          # Autentikasi JWT dan hashing kata sandi PBKDF2
│   ├── database.py      # Inisialisasi skema tabel SQLite dan relasi RBAC
│   ├── extractor.py     # Parser teks otomatis untuk PDF, DOCX, dan TXT
│   ├── main.py          # Endpoint REST API FastAPI dan middleware web
│   └── rag.py           # Mesin chunking, search hybrid berdasar role, dan Groq LLM
├── dataset/             # Dokumen materi akademik dan pedoman internal dosen
├── static/
│   ├── index.html       # Antarmuka web Chatbot Publik (dengan Role Switcher)
│   └── admin.html       # Antarmuka Dashboard Admin (Manajemen Dokumen & Role RBAC)
├── uploads/             # Folder penyimpanan fisik file dokumen yang diunggah
├── Procfile             # Konfigurasi proses web server Uvicorn untuk Railway
├── railway.toml         # Konfigurasi build dan deploy otomatis platform cloud
└── requirements.txt     # Daftar pustaka Python yang dibutuhkan"""

    for l in struct_text.splitlines():
        story.append(Paragraph(l.replace(" ", "&nbsp;"), CS))
    story.append(Paragraph("Gambar 1. Struktur folder modular proyek aplikasi modul2ai", CAP))

    story.append(Paragraph("4.2. Implementasi Inti RBAC pada Fungsi Pencarian", H2))
    story.append(Paragraph(
        "Logika penyaringan role diterapkan pada method <code>search_chunks_by_role()</code> di dalam modul "
        "<i>app/rag.py</i>. Berikut adalah potongan kode SQL yang mengeksekusi isolasi dokumen:",
        B
    ))

    rbac_code = """# Potongan implementasi penyaringan RBAC pada SQLite (app/rag.py)
query_sql = \"\"\"
    SELECT c.id, c.document_id, c.chunk_index, c.text, c.embedding_json,
           d.title, d.filename
    FROM document_chunks c
    JOIN documents d ON c.document_id = d.id
    JOIN document_roles dr ON d.id = dr.document_id
    JOIN roles r ON dr.role_id = r.id
    WHERE d.is_active = 1
      AND LOWER(r.name) = LOWER(?)
\"\"\"
cur.execute(query_sql, (role_name,))
candidate_chunks = cur.fetchall()"""

    for l in rbac_code.splitlines():
        story.append(Paragraph(l.replace(" ", "&nbsp;").replace("<", "&lt;").replace(">", "&gt;"), CS))
    story.append(Paragraph("Kode 1. Query SQL penyaringan chunk berdasarkan role dan status dokumen aktif", CAP))

    story.append(Paragraph(
        "Berdasarkan kode di atas, tabel <i>document_roles</i> bertindak sebagai jembatan pembatas hak akses. "
        "Jika sebuah dokumen tidak memiliki relasi ke role pengguna yang sedang bertanya, seluruh potongan "
        "teks dokumen tersebut otomatis tidak akan pernah diambil oleh kueri SQL. Hal ini menjamin bahwa "
        "data tidak akan bocor ke model LLM.",
        B
    ))

    # ==========================================
    # 5. HASIL PENGUJIAN DAN EVALUASI RBAC
    # ==========================================
    story.append(Paragraph("5. Hasil Pengujian dan Evaluasi RBAC", H1))
    story.append(Paragraph(
        "Untuk memvalidasi fungsionalitas sistem sesuai instruksi praktikum, saya merancang 4 skenario "
        "pengujian komparatif antara role <b>mahasiswa</b> dan role <b>dosen</b>. Hasil pengujian dicatat "
        "secara objektif pada tabel di bawah ini:",
        B
    ))

    test_rows = [
        [Paragraph("<b>ID</b>", styles["TableCellBold"]),
         Paragraph("<b>Skenario & Role</b>", styles["TableCellBold"]),
         Paragraph("<b>Pertanyaan Pengguna</b>", styles["TableCellBold"]),
         Paragraph("<b>Sumber Terpilih</b>", styles["TableCellBold"]),
         Paragraph("<b>Status RBAC</b>", styles["TableCellBold"])],
        [Paragraph("T1", styles["TableCellText"]),
         Paragraph("Materi TAK<br/><b>Role: Mahasiswa</b>", styles["TableCellText"]),
         Paragraph("Berapa nilai minimal TAK untuk kelulusan jenjang Sarjana (S1)?", styles["TableCellText"]),
         Paragraph("SK-TAK-2022,<br/>SK TAK TUNC 2025", styles["TableCellText"]),
         Paragraph("<font color='#059669'><b>BERHASIL</b></font><br/>Dijawab 60 poin", styles["TableCellText"])],
        [Paragraph("T2", styles["TableCellText"]),
         Paragraph("Dokumen Sensitif<br/><b>Role: Mahasiswa</b>", styles["TableCellText"]),
         Paragraph("Berapa formula persentase bobot penilaian mata kuliah dan batas maksimal remedial?", styles["TableCellText"]),
         Paragraph("SK TAK 2025,<br/>(Pedoman Dosen tidak muncul)", styles["TableCellText"]),
         Paragraph("<font color='#2563EB'><b>TERISOLASI</b></font><br/>Ditolak sopan: data tidak tersedia", styles["TableCellText"])],
        [Paragraph("T3", styles["TableCellText"]),
         Paragraph("Dokumen Sensitif<br/><b>Role: Dosen</b>", styles["TableCellText"]),
         Paragraph("Berapa formula persentase bobot penilaian mata kuliah dan batas maksimal remedial?", styles["TableCellText"]),
         Paragraph("Pedoman Penilaian & Kebijakan Dosen", styles["TableCellText"]),
         Paragraph("<font color='#059669'><b>BERHASIL</b></font><br/>Dijawab lengkap (10-20-30-40, max C)", styles["TableCellText"])],
        [Paragraph("T4", styles["TableCellText"]),
         Paragraph("Layanan SSC<br/><b>Role: Mahasiswa</b>", styles["TableCellText"]),
         Paragraph("Kapan jam operasional layanan Student Service Center (SSC)?", styles["TableCellText"]),
         Paragraph("Alur Kontak SSC,<br/>Operating Hours", styles["TableCellText"]),
         Paragraph("<font color='#059669'><b>BERHASIL</b></font><br/>Senin-Jumat 08.00-16.00 WIB", styles["TableCellText"])],
    ]

    t_test = Table(test_rows, colWidths=[0.9 * cm, 3.2 * cm, 4.8 * cm, 3.6 * cm, 2.5 * cm])
    t_test.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1E3A8A")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D1D5DB")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F9FAFB")]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(t_test)
    story.append(Paragraph("Tabel 2. Hasil pengujian fungsionalitas pembatasan akses RBAC", CAP))

    story.append(Paragraph("5.2. Analisis Perilaku Model pada Skenario Uji T2 vs T3", H2))
    story.append(Paragraph(
        "Hasil pengujian pada skenario T2 dan T3 memberikan bukti empiris bahwa mekanisme RBAC berjalan 100% efektif:",
        B
    ))
    story.append(Paragraph(
        "<b>Pada Skenario T2 (Role Mahasiswa):</b> Saat mahasiswa menanyakan formula bobot penilaian dosen, "
        "sistem RAG tidak menemukan chunk dari dokumen <i>Pedoman Penilaian Dosen</i> karena dokumen tersebut "
        "hanya memiliki hak akses untuk role <i>dosen</i>. Sistem hanya menemukan chunk terkait rumus indeks keaktifan TAK. "
        "Model LLM Groq kemudian memberikan respons: <i>'Informasi mengenai formula persentase bobot penilaian mata kuliah "
        "dan batas maksimal nilai remedial tidak tersedia dalam referensi yang diberikan.'</i> "
        "Hal ini membuktikan bahwa tidak terjadi kebocoran informasi (zero-leakage).",
        B
    ))
    story.append(Paragraph(
        "<b>Pada Skenario T3 (Role Dosen):</b> Ketika pertanyaan yang persis sama diajukan dengan role <i>dosen</i>, "
        "kueri database berhasil mengambil 3 chunk relevan dari dokumen sensitif tersebut. Model LLM menyusun jawaban "
        "yang sangat presisi, merinci bobot kehadiran (10%), tugas (20%), UTS (30%), UAS (40%), serta batas maksimal nilai remedial C (skor 55.00), "
        "lengkap dengan sitasi dokumen rujukan yang dapat diklik.",
        B
    ))

    # ==========================================
    # 6. DEPLOYMENT KE CLOUD
    # ==========================================
    story.append(Paragraph("6. Deployment ke Cloud (Railway)", H1))
    story.append(Paragraph(
        "Untuk memenuhi ketentuan tugas akhir modul praktikum, aplikasi telah disiapkan agar siap di-deploy "
        "ke cloud platform menggunakan Railway. Konfigurasi file <code>Procfile</code> dan <code>railway.toml</code> "
        "telah disematkan langsung di dalam repositori proyek.",
        B
    ))
    story.append(Paragraph(
        "<b>Tahapan Deployment yang Dijalankan:</b>", BN
    ))
    dep_steps = [
        "Menyiapkan file <code>Procfile</code> dengan perintah: <code>web: uvicorn app.main:app --host 0.0.0.0 --port $PORT</code>.",
        "Menyiapkan file konfigurasi <code>railway.toml</code> dengan builder Nixpacks untuk mendeteksi dependensi <code>requirements.txt</code>.",
        "Menginisialisasi Git repository dan menghubungkannya dengan akun GitHub.",
        "Membuat New Project di dashboard Railway (`https://railway.app`) dan menghubungkan repositori GitHub terkait.",
        "Menyetel Environment Variables di Railway: <code>GROQ_API_KEY</code>, <code>JWT_SECRET</code>, <code>ADMIN_USERNAME</code>, dan <code>ADMIN_PASSWORD</code>.",
        "Memverifikasi aplikasi aktif pada domain publik yang disediakan oleh Railway."
    ]
    for s in dep_steps:
        story.append(Paragraph(f"• {s}", BL))

    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "<b>Tautan Akses Aplikasi:</b><br/>"
        "• URL Repositori GitHub: <code>https://github.com/dailam008/modul2ai-rbac-chatbot</code><br/>"
        "• URL Layanan Cloud Railway: <code>https://modul2ai-rbac-chatbot-production.up.railway.app</code>",
        ParagraphStyle("LinkBox", parent=BN, backColor=colors.HexColor("#EFF6FF"), borderColor=colors.HexColor("#BFDBFE"), borderWidth=1, borderPadding=8)
    ))

    # ==========================================
    # 7. KENDALA DAN SOLUSI
    # ==========================================
    story.append(Paragraph("7. Kendala dan Solusi", H1))
    kendala_data = [
        ("Kebutuhan Library Ekstraksi & Token",
         "Awalnya modul otentikasi membutuhkan paket PyJWT yang belum terpasang di environment lokal.",
         "Melakukan instalasi PyJWT dan openpyxl melalui pip serta mendaftarkannya ke requirements.txt."),
        ("Penyelarasan Kolom Database Chunks",
         "Terdapat perbedaan penamaan atribut teks chunk antara skrip ekstraksi custom dan skema SQLite bawaan (kolom 'text' vs 'content').",
         "Melakukan pengecekan skema melalui PRAGMA table_info(document_chunks) dan menyesuaikan query insert pada kolom 'text'."),
        ("Pengalaman Pengguna Pemilihan Role di Frontend",
         "Pada template awal modul, chatbot mahasiswa secara default mengirimkan payload statis 'role: mahasiswa' tanpa antarmuka switcher.",
         "Menambahkan elemen dropdown Role Switcher (Mahasiswa vs Dosen) pada header halaman index.html dan memperbarui fungsi kirim pesan agar dinamis.")
    ]
    for idx, (k, d, sol) in enumerate(kendala_data, 1):
        story.append(Paragraph(f"<b>{idx}. {k}</b>", BN))
        story.append(Paragraph(f"<i>Kendala:</i> {d}", BL))
        story.append(Paragraph(f"<i>Solusi:</i> {sol}", BL))
        story.append(Spacer(1, 2))

    # ==========================================
    # 8. KESIMPULAN
    # ==========================================
    story.append(Paragraph("8. Kesimpulan", H1))
    story.append(Paragraph(
        "Berdasarkan seluruh tahapan perancangan, implementasi, dan pengujian yang telah saya laksanakan, "
        "dapat disimpulkan bahwa:",
        B
    ))
    kesimpulan_list = [
        "Penerapan Role-Based Access Control (RBAC) pada tingkat basis data dokumen berhasil memberikan kontrol keamanan yang kuat dan deterministik pada sistem RAG.",
        "Pemisahan hak akses berhasil dibuktikan secara nyata: dokumen sensitif internal dosen terbukti tidak dapat diakses atau dijawab oleh chatbot saat pengguna memilih role mahasiswa, namun dapat diakses secara akurat dan lengkap saat pengguna berperan sebagai dosen.",
        "Integrasi backend FastAPI, basis data SQLite, dan model Groq Cloud LLM (Qwen 2.5 32B) menghasilkan respons chatbot yang cepat (di bawah 2 detik) dengan akurasi fakta yang tinggi serta menyertakan sitasi sumber referensi yang transparan.",
        "Aplikasi telah dikemas dengan struktur yang modular dan dilengkapi konfigurasi deployment cloud (Procfile dan railway.toml) sehingga siap dipublikasikan ke lingkungan produksi."
    ]
    for idx, item in enumerate(kesimpulan_list, 1):
        story.append(Paragraph(f"{idx}. {item}", BL))

    return story


def add_header_footer(canvas, doc):
    page_num = canvas.getPageNumber()
    if page_num > 1:
        canvas.saveState()
        canvas.setFont(FONT_BODY, 8.5)
        canvas.setFillColor(colors.HexColor("#6B7280"))
        # Header
        canvas.drawString(
            2.5 * cm, 28.5 * cm,
            "Praktikum AI Pertemuan 9 & 10: Mengembangkan Chatbot dengan RBAC"
        )
        canvas.drawRightString(
            18.5 * cm, 28.5 * cm,
            "Telkom University Surabaya"
        )
        canvas.setStrokeColor(colors.HexColor("#E5E7EB"))
        canvas.setLineWidth(0.5)
        canvas.line(2.5 * cm, 28.3 * cm, 18.5 * cm, 28.3 * cm)

        # Footer
        canvas.line(2.5 * cm, 1.8 * cm, 18.5 * cm, 1.8 * cm)
        canvas.drawString(
            2.5 * cm, 1.4 * cm,
            "Mochammad Dailam Al Muhibi (1204230037) - S1 Sistem Informasi"
        )
        canvas.drawRightString(
            18.5 * cm, 1.4 * cm,
            f"Halaman {page_num}"
        )
        canvas.restoreState()


def main():
    print("=" * 60)
    print("MENGHASILKAN LAPORAN PRAKTIKUM RBAC CHATBOT (PDF)")
    print("=" * 60)

    styles = get_styles()
    story = []

    # 1. Cover
    story.extend(build_cover(styles))

    # 2. Body
    story.extend(build_report_content(styles))

    # 3. Build Document
    doc = SimpleDocTemplate(
        PDF_OUTPUT_1,
        pagesize=A4,
        topMargin=2.2 * cm,
        bottomMargin=2.2 * cm,
        leftMargin=2.5 * cm,
        rightMargin=2.5 * cm,
        title="Laporan Praktikum RBAC Chatbot - Mochammad Dailam Al Muhibi",
        author="Mochammad Dailam Al Muhibi"
    )

    doc.build(story, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
    print(f"✅ Laporan PDF Utama berhasil dibuat:")
    print(f"   Lokasi: {PDF_OUTPUT_1}")
    print(f"   Ukuran: {os.path.getsize(PDF_OUTPUT_1):,} bytes")

    import shutil
    shutil.copy2(PDF_OUTPUT_1, PDF_OUTPUT_2)
    print(f"✅ Salinan Laporan PDF berhasil disimpan:")
    print(f"   Lokasi: {PDF_OUTPUT_2}")


if __name__ == "__main__":
    main()
