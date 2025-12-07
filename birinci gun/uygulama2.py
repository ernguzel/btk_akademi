class Kullanici:
    def __init__(self,isim,email):
        self.isim = isim
        self.email = email
    def bilgi(self):
        return f"bu kullanıcı: {self.isim} --- {self.email}"
    
class Ogrenci(Kullanici):
    def __init__(self,isim,email,ogrenci_no):
        super().__init__(isim,email)
        self.ogrenci_no = ogrenci_no
    def bilgi(self):
        return f" bu kullanici: {self.isim} --- {self.email} sahiptir --- \n ogrenci nosu: {self.ogrenci_no}"
    
class Ogretmen(Kullanici):
    def __init__(self, isim, email,brans):
        super().__init__(isim, email)
        self.brans = brans

    def bilgi(self):
        return f"egitmen {self.isim} - branş {self.brans}"
    
class Ders:
    def __init__(self,ad ,ogretmen):
        self.ad=ad
        self.ogrtmen = ogretmen
        self.__notlar = {}

    def not_ekle(self,ogrenci,not_deger):
        if 0<=not_deger<=100:
            self.__notlar[ogrenci.isim] = not_deger
        else:
            print("yanlis nor araliği")

    def notlari_goster(self):
        return dict(self.__notlar)
    
    def ortalama(self):
        if  not self.__notlar:
            return 0
        else:
            return sum(self.__notlar.values())/len(self.__notlar)
        
class Platform:
    def __init__(self):
        self.kullanicilar = []
        self.dersler = []

    def kullanici_ekle(self,k):
        self.kullanicilar.append(k)
    def ders_ekle(self,d):
        self.dersler.append(d)
    def listele(self):
        print("platformdaki kullanicilar")
        for k in self.kullanicilar:
            print(k.bilgi())
        for d in self.dersler:
            print(d.ad)

if __name__ == "__main__":

    t1 = Ogretmen("beytullah","beytullah@btk.com","ucus egitmeni")
    s1 = Ogrenci("ahmet","ahmet@firat.com",2255518)
    s2 = Ogrenci("mehmet","mehmet@firat.com",1299928)

    plt = Platform()
    plt.kullanici_ekle(t1)
    plt.kullanici_ekle(s1)
    plt.kullanici_ekle(s2)

    python_dersi = Ders("python101",t1)
    python_dersi.not_ekle(s1,55)
    python_dersi.not_ekle(s2,96)

    plt.ders_ekle(python_dersi)

    plt.listele()

    print("ders notlari: ", python_dersi.notlari_goster())
    print("ders ortlamaasi: ", python_dersi.ortalama())