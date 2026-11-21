import os
import json

os.chdir(r'c:\Users\Dailam\Documents\Semester 7\AI\modul2ai')
from app.rag import search_chunks_by_role, generate_answer

tests = [
    {
        'id': 'T1',
        'desc': 'Pertanyaan Umum TAK (Role: Mahasiswa)',
        'role': 'mahasiswa',
        'q': 'Berapa nilai minimal TAK untuk kelulusan jenjang Sarjana (S1)?'
    },
    {
        'id': 'T2',
        'desc': 'Pertanyaan Dokumen Sensitif Dosen diajukan oleh Mahasiswa (Uji Penolakan/Isolasi RBAC)',
        'role': 'mahasiswa',
        'q': 'Berapa formula persentase bobot penilaian mata kuliah dan batas maksimal nilai remedial?'
    },
    {
        'id': 'T3',
        'desc': 'Pertanyaan Dokumen Sensitif Dosen diajukan oleh Dosen (Uji Akses Resmi RBAC)',
        'role': 'dosen',
        'q': 'Berapa formula persentase bobot penilaian mata kuliah dan batas maksimal nilai remedial?'
    },
    {
        'id': 'T4',
        'desc': 'Pertanyaan Layanan Operasional SSC (Role: Mahasiswa)',
        'role': 'mahasiswa',
        'q': 'Kapan jam operasional layanan Student Service Center (SSC)?'
    }
]

results = []
for t in tests:
    print(f"=== {t['id']}: {t['desc']} ===")
    chunks = search_chunks_by_role(t['q'], t['role'], top_k=5)
    ans = generate_answer(t['q'], t['role'], chunks)
    res_obj = {
        'id': t['id'],
        'desc': t['desc'],
        'role': t['role'],
        'query': t['q'],
        'chunk_count': len(chunks),
        'sources': ans['sources'],
        'answer': ans['answer']
    }
    results.append(res_obj)
    print(f"Role: {t['role']}")
    print(f"Chunks ditemukan: {len(chunks)}")
    print(f"Sumber: {[s['title'] for s in ans['sources']]}")
    print(f"Cuplikan Jawaban: {ans['answer'][:200].replace(chr(10), ' ')}...\n")

with open('evaluasi_rbac_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("✅ Semua pengujian RBAC selesai dan disimpan di evaluasi_rbac_results.json!")
