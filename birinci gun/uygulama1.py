import string

def kelime_analizi(file_name):
    try:
        with open(file_name,"r",encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print("boyle bir dosya bulunamadi!!!")
        return
    
    for p in string.punctuation:
        text = text.replace(p," ")

    words = text.lower().split()

    if not words:
        print("dosyamiz bos")
        return
    
    counts = {}
    for w in words:
        counts[w] = counts.get(w,0) + 1

    toplam_kelime = len(words)
    toplam_benzersiz_kelime = len(counts)

    top3 = sorted(counts.items(), key= lambda x: (-x[1],x[0]))[:3]

    long_words = {w: c for w,c in counts.items() if len(w) > 5}
    top_long_words = max(long_words.items(),key=lambda x: (x[1],x[0]))

    harflerden_kelimeler = {w: c for w,c in counts.items() if w.isalpha()}
    top_harflerden = max(harflerden_kelimeler.items(), key= lambda x: (x[1],x[0]),default=(("yok",0)))


    print("toplam kelime sayisi: ", toplam_kelime)
    print("benzersiz kelime sayisi: ", toplam_benzersiz_kelime)

    print("en çok tekraar eden kelime: ")
    for w,c in top3:
        print(f"{w},{c}")
    
    print("uzunluğu 5 ten büyük en çok geçen kelime : ", top_long_words)
    print("sadece harfler oluşan en çok geçen kelime : ", top_harflerden)


file_path ="uygulama1.txt"
kelime_analizi(file_path)