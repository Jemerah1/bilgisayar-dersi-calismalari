#AKILLI ARAÇ KİRALAMA PROGRAMI 

import math

ad = input("Ad giriniz: ")
soyad = input("Soyad giriniz: ")
kiralama_gün_süresi = int(input("Kaç gün kiralayacaksınız: "))
günlük_kiralama_ücret = int(input("Günlük kiralama ücreti: "))
günlük_sürüş_mesafesi = int(input("Günlük kaç km yol gidiceksiniz: "))
yüz_km_tüketim = float(input("100km'deki yakıt tüketimi: "))
yakıt_ücret = float(input("Yakıtın lite fiyatı: "))
teslimat_mesafesi = int(input("Teslimat mesafesi: "))
araç_model = str(input("Araç modeli: "))

#--- Kiralama Maliyeti ---

kiralama_ücreti = kiralama_gün_süresi*günlük_kiralama_ücret
hizmet_bedeli = kiralama_ücreti*0.08
toplam_kiralama_ücreti = kiralama_ücreti+hizmet_bedeli

#--- Yakıt Masrafı ---

toplam_sürüş_mesafe = günlük_sürüş_mesafesi * kiralama_gün_süresi
toplam_yakıt_tüketimi = (toplam_sürüş_mesafe * yüz_km_tüketim) / 100
toplam_yakıt_maliyeti = toplam_yakıt_tüketimi * yakıt_ücret

#--- Teslimat Ücreti --- 

teslimat_ücret = max(teslimat_mesafesi-20 , 0) * 12 

# --- Genel Maliyet --- 

genel_maliyet = toplam_kiralama_ücreti + toplam_yakıt_maliyeti + teslimat_ücret
günlük_ortalama_maliyet = genel_maliyet / kiralama_gün_süresi

#--- Toparlama --- 

genel_maliyet_karekok = math.sqrt(genel_maliyet)
genel_maliyet_log = math.log(genel_maliyet)
günlük_ortalama_maliyet_yukarı_yuv = math.ceil(günlük_ortalama_maliyet)
genel_maliyet_tam_ksm = math.trunc(genel_maliyet)
toplam_sürüş_mesafe_mutlak = math.fabs(toplam_sürüş_mesafe)

#--- Metinsel İfadeler --- 

ad_soyad = ad + " " + soyad
ad_soyad_karakter = len(ad_soyad)
ad_soyad_ilküç = ad_soyad[0:3]
araç_model_büyük = araç_model.upper()
araç_model_küçük = araç_model.lower()

#--- Yazdırma --- 
print("")
print("Ad Soyad: ", ad_soyad)
print("Ad Soyad karakter uzunluğu: ", ad_soyad_karakter)
print("Ad Soyad ilk üç karakteri: ", ad_soyad_ilküç)
print(f"Toplam kiralama ücreti:  {toplam_kiralama_ücreti: .2f}")
print(f"Toplam yakıt maliyeti: {toplam_yakıt_maliyeti: .2f}")
print(f"Teslimat ücreti: {teslimat_ücret: .2f}")
print(f"Toplam maliyet: {genel_maliyet: .2f}")
print(f"Günlük ortalama maliyet: {günlük_ortalama_maliyet: .2f}")
print(f"Genel maliyetin karekökü: {genel_maliyet_karekok: .2f}")
print(f"Genel maliyetin logaritması: {genel_maliyet_log: .2f}")
print(f"Günlük ortalama maliyetin yukarı yuvarlanması: {günlük_ortalama_maliyet_yukarı_yuv: .2f}")
print(f"Genel maliyetin tam kısmı: {genel_maliyet_tam_ksm: .2f}")
print(f"Toplam sürüş mesalfesini mutlak değeri: {toplam_sürüş_mesafe_mutlak: .2f}")
print("Araç modeliniz: ", araç_model_büyük)