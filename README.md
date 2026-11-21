# 🎓 Custom AI Chatbot RAG Berbasis Role (RBAC) dengan FastAPI & Groq LLM

Proyek implementasi tugas praktikum mata kuliah **Kecerdasan Artifisial dan Penerapannya** (Pertemuan 9 & 10) di Telkom University Surabaya.

---

## 👨‍💻 Identitas Mahasiswa
- **Nama**: Mochammad Dailam Al Muhibi
- **NIM**: 1204230037
- **Kelas**: SS1SI-06-REG-01
- **Program Studi**: S1 Sistem Informasi (Fakultas Rekayasa Industri)
- **Dosen Pengampu**: M. Nizar P. Ma'ady, S.Kom., M.IM., M.Kom.
- **Asisten Praktikum**: Muhammad Baihaqi / Mohamad Fikri Isfahani

---

## 🌟 Fitur Utama
1. **Role-Based Access Control (RBAC)**: Pembatasan dokumen di tingkat database SQLite (`document_roles`). Dokumen sensitif khusus role `dosen` tidak akan bocor saat pengguna bertanya dengan role `mahasiswa`.
2. **Hybrid Retrieval**: Perpaduan Cosine Similarity pada vektor 384-dimensi dan Lexical Bonus (exact keyword matching).
3. **Groq Cloud LLM Integration**: Generasi jawaban faktual berbasis sitasi dengan model `qwen/qwen3.8-27b`.
4. **Multi-Format Document Parsing**: Mendukung ekstraksi teks dari PDF, DOCX, TXT, dan CSV.
5. **Modern Web Interface**: Antarmuka Chatbot Publik dengan Role Switcher (`/`) dan Dashboard Admin (`/admin`) dengan otentikasi JWT.

---

## 🚀 Panduan Menjalankan Lokal

```bash
# 1. Masuk folder proyek
cd modul2ai

# 2. Pasang pustaka
pip install -r requirements.txt

# 3. Jalankan server
uvicorn app.main:app --reload --port 8000
```
Akses di browser: `http://localhost:8000`

---

## ☁️ Deployment ke Railway
File konfigurasi `Procfile` dan `railway.toml` sudah tersedia.
Set environment variables berikut di dashboard Railway:
- `GROQ_API_KEY`: API key dari Groq Console
- `JWT_SECRET`: Kunci rahasia JWT
- `ADMIN_USERNAME`: admin
- `ADMIN_PASSWORD`: kata sandi admin
