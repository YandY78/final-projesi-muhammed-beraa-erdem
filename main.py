import os

kaynaklar = ""

for dosya in os.listdir("data"):

    if dosya.endswith(".txt"):

        with open(
            os.path.join("data", dosya),
            "r",
            encoding="utf-8"
        ) as f:

            kaynaklar += f.read()
            kaynaklar += "\n"


while True:

    soru = input("\nSorunuz: ").lower()

    if "rag" in soru:

        print("""
RAG, Retrieval Augmented Generation anlamına gelir.
RAG sistemleri önce kaynaklarda arama yapar.
Sonra yapay zeka cevabı oluşturur.
""")

    elif "shap" in soru:

        print("""
SHAP açıklanabilir yapay zeka yöntemidir.
Makine öğrenmesi modellerinin kararlarını yorumlar.
""")

    else:

        print("Bu bilgi kaynaklarda bulunamadı.")