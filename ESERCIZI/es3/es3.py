import numpy as np
import pandas as pd
import matplotlib as plt
from datasets import load_dataset


#1

df = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv")

top10 = df.sort_values("total_litres_of_pure_alcohol", ascending=False).head(10)
print("Top 10 paesi per consumo totale di alcol:")
print(top10[["country","total_litres_of_pure_alcohol"]], "\n")

print("Media beer_servings:   ", df["beer_servings"].mean())
print("Media wine_servings:   ", df["wine_servings"].mean())
print("Media spirit_servings: ", df["spirit_servings"].mean(), "\n")

df["alcohol_index"] = (df["beer_servings"] + df["wine_servings"] + df["spirit_servings"]) /3

max_idx = df["alcohol_index"].idxmax()
print("Paese con alcohol_index più alto:", df.loc[max_idx, "country"], "\n")

birra100 = df[df["beer_servings"] > 100]
print(f"Paesi con beer_servings > 100 ({len(birra100)} paesi):")
print(birra100[["country","beer_servings"]], "\n")

plt.figure()
plt.bar(top10["country"], top10["total_litres_of_pure_alcohol"])
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 paesi per total_litres_of_pure_alcohol")
plt.tight_layout()
#plt.show()
#plt.savefig("bar_top10.png")

wine_sorted = df.sort_values("wine_servings").set_index("country")["wine_servings"]
plt.figure()
plt.plot(wine_sorted.index, wine_sorted.values, marker="o")
plt.xticks(rotation=90, ha="right")
plt.title("wine_servings per paese (ordinato)")
plt.tight_layout()
#plt.show()
#plt.savefig("line_wine.png")


#2

dataset = load_dataset("lukebarousse/data_jobs")
jobs = dataset["train"].to_pandas()

jobs["job_posted_date"] = pd.to_datetime(jobs["job_posted_date"])

country_stats = jobs.groupby("country")["salary_year_avg"].agg(
    avg_salary="mean",
    total_jobs="count",
    min_salary="min",
    max_salary="max"
).reset_index()

print("Statistiche offerte per paese:")
print(country_stats.head(), "\n")

avg_salary_by_title = jobs.groupby("job_title_short")["salary_year_avg"] \
                          .mean() \
                          .sort_values(ascending=False)


plt.figure(figsize=(8, 6))
plt.barh(avg_salary_by_title.index, avg_salary_by_title.values)
plt.xlabel("Stipendio medio annuale")
plt.ylabel("Titolo di lavoro")
plt.title("Stipendio medio per job_title_short")
plt.tight_layout()
plt.show()
#plt.savefig(bsrh.png)