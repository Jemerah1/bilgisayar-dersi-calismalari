#Akıllı Üretim ve Fabrika Maliyet Analizi

import math

operatör = input("Operatör adı giriniz: ")
fabrika = input("Fabrika adı giriniz: ")
üretilecek_parça = int(input("Kaç parça üretilecek: "))
parça_birim_maliyet = float(input("Birim parça maliyeti (TL): "))
parça_birim_satış = float(input("Birim parça satış fiyatı(TL): "))
üretim_hat_günlük_çalışma_saat = float(input("Üretim hattı günde kaç saat çalışıyor: "))
saatte_üretilen_parça = int(input("Bir saatte kaç parça üretiliyor: "))
hatalı_üretim_oranı = int(input("Hatalı üretim oranı (%): "))
saatlik_elektrik_tüketimi = float(input("Bir saatte tüketilen elektrik (kWh): "))
elektrik_brm_fyt = float(input("Elektriğin birim fiyat: "))

#--- Üretim ve Fire Hesabı ---

üretim_hedef_süre = üretilecek_parça / saatte_üretilen_parça

hatalı_üretim_miktar = üretilecek_parça * (hatalı_üretim_oranı / 100)

sağlam_parça = üretilecek_parça - hatalı_üretim_miktar

üretim_hedef_süre_aşağı_yuv = math.floor(üretim_hedef_süre)

#--- Üretim Maliyetleri --- 

toplam_üretim_maliyet = (üretilecek_parça * parça_birim_maliyet) 
harcanan_elektrik = (üretim_hedef_süre * saatlik_elektrik_tüketimi)
harcanan_elektrik_maliyet = (harcanan_elektrik * elektrik_brm_fyt)

toplam_maliyet = toplam_üretim_maliyet + harcanan_elektrik_maliyet

#--- Satış ve Kârlılık Oranı --- 

satış_geliri = (sağlam_parça * parça_birim_satış)

net_kar = satış_geliri - (harcanan_elektrik_maliyet + toplam_üretim_maliyet)

kar_yüzde = (net_kar / satış_geliri) * 100

sağlam_prç_bşn_dşn_tplm_maliyet = (toplam_maliyet / sağlam_parça) 

#--- Matematiksel İşlemler --- 

üretim_hdf_ve_saatlik_ürtm_ebob = math.gcd(üretilecek_parça , saatte_üretilen_parça)

üretim_hdf_süre_yuv = round(üretim_hedef_süre)

ürtm_süresi_üstel = math.exp(üretim_hedef_süre)

ürtm_süresi_radyan = math.radians(üretim_hedef_süre)
ürtm_süresi_sin = math.sin(ürtm_süresi_radyan)
ürtm_süresi_cos = math.cos(ürtm_süresi_radyan)
ürtm_süresi_tan = math.tan(ürtm_süresi_radyan)

ürtm_süresi_sin_dgr = math.asin(ürtm_süresi_sin)
ürtm_süresi_cos_dgr = math.acos(ürtm_süresi_cos)
ürtm_süresi_tan_dgr = math.atan(ürtm_süresi_tan)

ürtm_süresi_tam_kesir_ayrm = math.modf(üretim_hedef_süre)

#--- Metinsel İfadeler --- 

fabrika_tmz = fabrika.strip()
fabrika_ilk_byk = fabrika.title()
#Fabrika adı STRden mi oluşuyor fabrika.isalpha()
#Fabrika adından Sanayi kelime kaçıncı sırada bul -> fabrika.find("sanayi")
operatör_tre = operatör.replace(" ", "-")
fabrika_klm = fabrika.split("-")
rapor_başlık = operatör + " " + "(" + fabrika_ilk_byk + ")"
rapor_başlık_uzunlk = len(rapor_başlık)

#--- Yazdırma --- 

print(" ")
print("Rapor Başlığı:  ", rapor_başlık )
print("Rapor başlığı uzunluğu: ", rapor_başlık_uzunlk )
print(" ")
print("Hedef Üretim ", üretim_hdf_süre_yuv, "saatte yapılacak."  )
print(f"{hatalı_üretim_miktar: .2f} Tane Hatalı parça üretildi ")
print(sağlam_parça, "Tane sağlam parça üretildi. ")
print(" ")
print(f"Toplam {harcanan_elektrik:.2f} ", f"kWh elektirk harcandı. {harcanan_elektrik_maliyet:.2f}" , "TL elektrik faturası geldi")
print("Toplam " , satış_geliri, "TL'lik parça satıldı. ", net_kar , "TL Net kâr elde edildi. ", f"Kâr yüzdesi % {kar_yüzde: .2f}")
print(f"Sağlam parça başına düşen toplam maliyet: {sağlam_prç_bşn_dşn_tplm_maliyet: .2f} TL ")
print(" ")
print("Üretim hedefi ve saatlik üretimin en büyük ortak böleni: ", üretim_hdf_ve_saatlik_ürtm_ebob)
print(f"Üretim süresinin üstel değeri: {ürtm_süresi_üstel: .2f}")
print(f"Üretim süresinin sinüsü açısı:  {ürtm_süresi_sin_dgr: .2f}", f"\tÜretim süresinin cosinüs açısı: {ürtm_süresi_cos_dgr: .2f}",f"\tÜretim süresini tanjant açısı: {ürtm_süresi_tan_dgr: .2f}")
print("Üretim süresinin kesir ve tam kısımları: ", ürtm_süresi_tam_kesir_ayrm)
print(" ")
print("Fabrika Adı:", fabrika_tmz)
print(" ")
print(fabrika_ilk_byk)
print(" ")
print("Fabrika adında \"Sanayi\"", fabrika.lower().find("sanayi"), ".sırada bulunuyor")
print("Öperatör adının arasına \"-\" konması: ", operatör_tre )
print("Fabrika adının arasına \"-\" konması: ", fabrika.split())
