import tkinter as tk
import os


def soru_sor():

    soru = giris.get().lower()

    cevap = "Bu bilgi kaynaklarda bulunamadı."

    for dosya in os.listdir("data"):

        if dosya.endswith(".txt"):

            with open(
                os.path.join("data", dosya),
                "r",
                encoding="utf-8"
            ) as f:

                icerik = f.read()

                if "rag" in soru and "rag" in icerik.lower():

                    cevap = f"Kaynak: {dosya}\n\n{icerik}"

                elif "shap" in soru and "shap" in icerik.lower():

                    cevap = f"Kaynak: {dosya}\n\n{icerik}"

    sonuc.config(text=cevap)


pencere = tk.Tk()

pencere.title("Akademik Yapay Zeka Asistanı")

pencere.geometry("700x500")


baslik = tk.Label(
    pencere,
    text="Akademik Yapay Zeka Asistanı",
    font=("Arial", 16)
)

baslik.pack(pady=15)


giris = tk.Entry(
    pencere,
    width=60
)

giris.pack(pady=10)


buton = tk.Button(
    pencere,
    text="Sor",
    command=soru_sor
)

buton.pack(pady=10)


sonuc = tk.Label(
    pencere,
    text="",
    wraplength=600,
    justify="left"
)

sonuc.pack(pady=20)

pencere.mainloop()