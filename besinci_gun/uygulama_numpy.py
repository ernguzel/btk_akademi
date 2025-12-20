import numpy as np 

numbers = np.random.randint(0,50,size=20)
print(numbers)

bolunmus_numbers = numbers / 2
print(bolunmus_numbers)

ortalama_numbers = np.mean(numbers)
ortalama_bolunmus = np.mean(bolunmus_numbers)


print(f"ortalama normal {ortalama_numbers}")
print(f"ortalama bolunmus {ortalama_bolunmus}")

filtered_numbers = numbers[numbers>30]

print(f"30 dan buyukler {filtered_numbers}")