# ---------------------------------------------------------
# 1. Generator – log dosyasını satır satır okur
# ---------------------------------------------------------
def log_satir_okuyucu(dosya_adi):
    with open(dosya_adi, "r", encoding="utf-8") as f:
        for satir in f:
            yield satir.strip()


# ---------------------------------------------------------
# 2. Iterator Class – generator üzerinde gezinir
# ---------------------------------------------------------
class LogIsleyici:
    def __init__(self, satirlar):
        self.satirlar = satirlar

    def __iter__(self):
        return self

    def __next__(self):
        satir = next(self.satirlar)   # generator'dan sıradaki satırı alır
        return satir


# ---------------------------------------------------------
# 3. Decorator – analiz fonksiyonunu loglar
# ---------------------------------------------------------
def log_islem(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Çalışıyor: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


# ---------------------------------------------------------
# 4. Analiz fonksiyonu – hata satırlarını bulur
# ---------------------------------------------------------
@log_islem
def error_tara(iterator):
    hatalar = []
    for satir in iterator:
        if "ERROR" in satir:
            hatalar.append(satir)
    return hatalar


# ---------------------------------------------------------
# 5. Pipeline çalıştırma
# ---------------------------------------------------------
if __name__ == "__main__":
    # 1. Generator ile dosyayı oku
    satir_generator = log_satir_okuyucu("uygulama3.txt")

    # 2. Iterator sınıfına ver
    iterator = LogIsleyici(satir_generator)

    # 3. Decorator'lu analiz fonksiyonunu çağır
    sonuc = error_tara(iterator)

    # 4. Sonuçları yazdır
    print("\nBulunan Hatalar:")
    for h in sonuc:
        print(" -", h)
