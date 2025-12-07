def log_satir_okuyucu(dosya_adi):
    with open(dosya_adi,"r",encoding="utf-8") as f:
        for satir in f:
            yield satir.strip()

class LogIsleyici:
    def __init__(self,satirlar):
        self.satirlar =satirlar

    def __iter__(self):
        return self
    
    def __next__(self):
        satir = next(self.satirlar)
        return satir
    

def log_islem(func):
    def wrapper(*args,**kwargs):
        print(f"[LOG] çalışıyor : {func.__name__}")

        return func(*args , **kwargs)
    return wrapper

@log_islem
def eror_tara(iterator):
    hatalar = []

    for satir  in iterator:
        if "ERROR" in satir:
            hatalar.append(satir)
    
    return hatalar


satir_generator = log_satir_okuyucu("uygulama3.txt")

iterator = LogIsleyici(satir_generator)

sonuc = eror_tara(iterator)

print("bulunana hatalar ")
for h in sonuc:
    print ("-",h)