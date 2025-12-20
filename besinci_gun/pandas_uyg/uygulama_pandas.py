import pandas as pd 

df = pd.read_csv("people.csv")
# print(df.head())

filtered = df[df["yas"]>30]
# print(f"30 dan buyuk olanlar {filtered}")

sorted_df = df.sort_values(by = "maas",ascending=False)
# print(f"siralanmis hali {sorted_df}")

ortalama_maas = df.groupby("departman")["maas"].mean()
# print(f"ortalama maas degeri {ortalama_maas}")

df["maas"] = df["maas"].fillna(0)
print(f"sıfırla dolum {df}")

