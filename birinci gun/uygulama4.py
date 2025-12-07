def log_step(func):
    def wrapper(*args,**kw):
        print(f"[LOG] {func.__name__} çalışıyor")
        return func(*args,**kw)
    return wrapper

def aktivite_okuyucu(file_path):
    with open(file_path,"r",encoding="utf-8") as f:
        for line in f:
            yield line.strip()

class Aktivite:
    def __init__(self, user):
        self.user = user
    def message(self):
        return "Genel aktivite"
    
class LoginAktivite(Aktivite):
    def __init__(self, user):
        super().__init__(user)
        print( f"{self.user} sisteme giriş yapti ")

class LogoutAktivite(Aktivite):
    def __init__(self,user):
        super().__init__(user)
        print( f"{self.user} sistemden çıktı  ")
    
class ErrorAktivite(Aktivite):
    def __init__(self,user):
        super().__init__(user)
        print( f"{self.user} için HATA oluştu" )  
    

class AktiviteAnalizi:
    def __init__(self,generator):
        self.gen = generator
    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self.gen)
    
path = "uygulama4.txt"


@log_step
def analiz(file):
    results = []
    for line in AktiviteAnalizi(aktivite_okuyucu(path)):
        parts = line.split(",")
    
        try:
            a_tipi , user = parts[0] , parts[1]
        except:
            print(f"hatalı satır: {line}")
        
        if a_tipi == "LOGIN":
            act = LoginAktivite(user)
        elif a_tipi == "LOGOUT":
            act = LogoutAktivite(user)
        elif a_tipi =="ERROR":
            act = ErrorAktivite(user)

        else:
            print(f"hatali bir sastır var : {line}")

        results.append(act.message())

    return results


analiz(path)


    