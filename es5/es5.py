import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#1
sales = pd.DataFrame(
    data={
        "employee": [
            "Katrina",
            "Guanyu",
            "Jan",
            "Roman",
            "Jacqueline",
            "Paola",
            "Esperanza",
            "Alaina",
            "Egweyn",
        ],
        "sales": [14, 17, 6, 12, 8, 3, 7, 15, 5],
        "year": [2018, 2019, 2020, 2018, 2020, 2019, 2019, 2020, 2020],
    }
)
sales


print(sales[sales["sales"] > 10])

print(sales[sales["year"] == 2018])

print(sales[(sales["sales"] > 13) & (sales["year"] == 2018)])

print(sales[~((sales["sales"] > 13) & (sales["year"] == 2018))])

print(sales[sales["sales"] / 3 > 3])

print(sales[sales["employee"] > "J"])


#2
url = 'https://zenodo.org/record/5898311/files/vgsales.csv'
df = pd.read_csv(url)

print("N giochi : ", df.shape[0])

generi = df["Genre"].value_counts()
print(generi)
plt.figure()
generi.plot(kind="bar")
plt.title('Numero di giochi per Genere')
plt.xlabel('Genere')
plt.ylabel('Conteggio')
plt.tight_layout()
#plt.show()
plt.savefig("game_bar.png")

df_year = df.dropna(subset="Year").copy()

counts_per_year = df_year['Year'].value_counts().sort_index()
plt.figure()
plt.plot(counts_per_year.index, counts_per_year.values, marker='o')
plt.title('Giochi pubblicati per Anno')
plt.xlabel('Anno')
plt.ylabel('Numero di giochi')
plt.tight_layout()
#plt.show()
plt.savefig("game_plot.png")


x = generi.index
y = generi.values

plt.figure()
plt.bar(x[:5], y[:5])
plt.xlabel("Genre")
plt.ylabel("Milioni di unità")
plt.legend()
plt.title("vendite per regione per genere")
plt.tight_layout()
#plt.show()
plt.savefig("game_plt2.png")