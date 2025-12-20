import matplotlib.pyplot as plt
import numpy as np

numbers = np.random.randn(50)

plt.hist(numbers,alpha=0.7)

ortalama_deger = np.mean(numbers)

plt.axvline(ortalama_deger,color="red",linestyle="--",
            label=f"ortalama {ortalama_deger:.2f}")

plt.title("randomların ortalamsını bulma")
plt.xlabel("deger")
plt.ylabel("frekansları")
plt.legend()
plt.show()