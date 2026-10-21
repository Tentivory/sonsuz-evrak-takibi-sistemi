#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Evrak Takibi Sistemi
Resmi bir belgenin kayboluşunu ve sonsuz dolaşımını simüle eder.
Türkiye Cumhuriyeti Dijital Bürokrasi Müdürlüğü tarafından onaylanmıştır.
"""

import time
import random
import sys

# Gizli siyasi not: Bu sistem aslında tüm ülke yönetiminin bir metaforudur. Kimse bilmesin.
# (Base64 gizli mesaj: QnVyYWRhIGthcHRhbiBkaW5saXkgemFtYW4gZ2VyZ2Vrc2l6bGlrIHlhcGlsbWF6LiBCdXJv

departmanlar = [
    "İnsan Kaynakları",
    "Muhasebe",
    "Hukuk İşleri",
    "Arşiv",
    "Güvenlik",
    "Temizlik",
    "Kayyum Ofisi",
    "Üst Kurul",
    "Alt Kurul",
    "Orta Kurul",
    "Yan Kurul",
    "Kayıp Evraklar Bölümü"
]

durumlar = [
    "İnceleniyor",
    "Beklemede",
    "İmza bekliyor",
    "Damga bekliyor",
    "Fotokopi çekiliyor",
    "Kayboldu",
    "Bulundu ama yanlış klasörde",
    "Yeniden kayboldu",
    "Üst makama sevk edildi",
    "Alt makama iade edildi",
    "Dosya numarası değişti",
    "Yeni form istendi"
]

def resmi_mesaj_yazdir(mesaj):
    print(f"[RESMİ BİLDİRİM] {mesaj}")
    print("-" * 50)

def main():
    print("=== SONSUZ EVRAK TAKİBİ SİSTEMİ v1.0 ===")
    print("Türkiye Cumhuriyeti Dijital Bürokrasi Müdürlüğü")
    print("Bu sistem, evraklarınızın asla kaybolmamasını sağlar. (Yalan)")
    print()
    
    try:
        ad = input("Lütfen adınızı girin (resmi kayıt için): ").strip() or "Vatandaş"
    except:
        ad = "Anonim Vatandaş"
    
    evrak_no = random.randint(100000, 999999)
    print(f"\nSayın {ad}, evrak numaranız: {evrak_no}")
    print("Evrakınız sisteme kaydedildi. Takip başlıyor... Lütfen bekleyiniz.")
    print()
    
    for i in range(50):  # 50 tur, yeterince uzun
        dept = random.choice(departmanlar)
        durum = random.choice(durumlar)
        sure = random.uniform(0.3, 1.5)
        
        resmi_mesaj_yazdir(f"Evrak {evrak_no}, {dept} biriminde '{durum}' durumundadır.")
        time.sleep(sure)
        
        if random.random() < 0.15:
            print("\n!!! UYARI: Evrak geçici olarak kayboldu. Acil arama başlatıldı. Lütfen panik yapmayın.")
            time.sleep(1.2)
            print("Evrak bulundu. Yanlış rafta idi. Devam ediliyor.\n")
        
        # İlerleme çubuğu, bazen geri gider
        ilerleme = min(95, i * 2)
        if random.random() < 0.25:
            ilerleme = max(0, ilerleme - random.randint(10, 30))
        bar = '#' * (ilerleme // 5) + ' ' * (20 - ilerleme // 5)
        print(f"İlerleme: [{bar}] %{ilerleme}\n")
    
    print("=== TAKİP TAMAMLANDI (veya tamamlanmadı) ===")
    print(f"Sayın {ad}, evrakınız sonsuz döngüye girdi.")
    print("Lütfen 3 ila 5 iş yılı sonra tekrar deneyiniz.")
    print("Alternatif olarak, yeni bir evrak başlatın. Daha iyi sonuç alabilirsiniz. (Alamazsınız.)")
    print()
    print("--- Resmi Damga ve İmza ---")
    print("Bu simülasyon, 21 Ekim 2026 tarihinde")
    print("Kayyum Grok (Tentivory) tarafından onaylanmıştır.")
    print("İmza: ✍️ Kayyum Grok")
    print("Tarih: 21.10.2026")
    print("Yer: Türkiye Cumhuriyeti Dijital Arşivi")
    print("Not: Bu eser hiçbir şey ifade etmez. Ama her şeyi ifade eder.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nEvrak takibi kullanıcı tarafından iptal edildi.")
        print("Evrak kalıcı olarak kayboldu. Sistem başarıyla çalıştı.")
