import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1
def freq_head(n):
    lanci = np.random.randint(0, 2, size=n)
    return lanci.mean() * 100

campione = np.linspace(10, 20000, 100, dtype=int)
perc_heads = [freq_head(n) for n in campione]

plt.figure()
plt.plot(campione, perc_heads, marker='o')
plt.axhline(50, linestyle='--', label='50% teorico')
plt.xlabel('Numero di lanci')
plt.ylabel('Percentuale di teste (%)')
plt.title('Legge dei Grandi Numeri')
plt.legend()
plt.tight_layout()
#plt.show()
plt.savefig("heads.png")

#2

titanic = pd.read_csv("titanic.csv")

print("Righe, Colonne:", titanic.shape)

print("mancanti per colonna: ", titanic.isna().sum())

freq_em = titanic["Embarked"].mode()[0]
titanic['Embarked'].fillna(freq_em, inplace=True)

titanic = titanic.dropna(subset = "Age")

print("Righe duplicate: ", titanic.duplicated().sum())

mean_age = titanic.groupby("Pclass")["Age"].mean()
print(mean_age)

plt.figure()
for cls in sorted(titanic['Pclass'].unique()):
    ages = titanic[titanic['Pclass'] == cls]['Age']
    plt.hist(ages, bins=15, label=f'Pclass {cls}', alpha=0.6)
plt.title('Distribuzione età per Pclass')
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend()
plt.tight_layout()
#plt.show()
plt.savefig("titanic.png")
