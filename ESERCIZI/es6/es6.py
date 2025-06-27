import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
from sklearn.linear_model import LinearRegression

#1
np.random.seed(42)
shape_true = 1.0 
sample = stats.gamma(a=shape_true).rvs(size=1000)

x = np.linspace(0, sample.max(), 200)
pdf = stats.gamma(a=shape_true).pdf(x)

plt.figure()
plt.hist(sample, bins=30, density=True, alpha=0.6, label="Campione")
plt.plot(x, pdf, label="PDF teorica")
plt.title("Gamma(α=1): istogramma + PDF")
plt.xlabel("x")
plt.ylabel("Densità")
plt.legend()
plt.tight_layout()
#plt.show()
plt.savefig("hist_gamma.png")

shape_est, loc_est, scale_est = stats.gamma.fit(sample, floc=0)  
print(f"Stima parametro di forma α: {shape_est:.3f}")

cdf = stats.gamma(a=shape_est, scale=scale_est).cdf(x)
plt.figure()
plt.plot(x, cdf, label="CDF stimata")
plt.title("Funzione di ripartizione (CDF)")
plt.xlabel("x")
plt.ylabel("F(x)")
plt.tight_layout()
#plt.show()
plt.savefig("CDF.png")

print(f"Varianza campionaria: {sample.var(ddof=1):.3f}")
print(f"Varianza teorica (fit): {stats.gamma(a=shape_est, scale=scale_est).var():.3f}")


#2
temp_max = np.array([17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18])
temp_min = np.array([-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58])
months = np.arange(12)

plt.plot(months, temp_max, "ro")
plt.plot(months, temp_min, "bo")
plt.xlabel("Month")
plt.ylabel("Min and max temperature")

#3
df = pd.read_csv('https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv')

X = df[["disp"]].values   
y = df["mpg"].values      

model = LinearRegression().fit(X, y)

intercept = model.intercept_
slope     = model.coef_[0]
r2        = model.score(X, y)

print(f"Modello: mpg = {intercept:.2f} + {slope:.4f}·disp")
print(f"R² del fit: {r2:.3f}")

plt.figure()
plt.scatter(df["disp"], df["mpg"], color="blue", label="Dati osservati")
plt.plot(df["disp"], model.predict(X), color="red", linewidth=2, label="Retta di fit")
plt.xlabel("Displacement (disp) [cubic inches]")
plt.ylabel("Miles per Gallon (mpg)")
plt.title("Regressione lineare: mpg ~ disp")
plt.legend()
plt.tight_layout()
#plt.show()
plt.savefig("regressione.png")
