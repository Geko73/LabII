import pandas as pd
import numpy as np
import plotly.express as px
from math import sqrt

#1
df = pd.read_csv("data.csv")

df['date'] = pd.to_datetime(df['date'], format='%Y-%m')
df['month_numeric'] = (df['date'].dt.year - 1949) * 12 + (df['date'].dt.month - 1)

degree = 3
coefs = np.polyfit(df['month_numeric'], df['passengers'], deg=degree)
df['predicted'] = np.polyval(coefs, df['month_numeric'])

errors = df['passengers'] - df['predicted']
rmse = sqrt((errors**2).mean())
print(f"RMSE del fit polinomiale di grado {degree}: {rmse:.2f} passeggeri")

fig = px.scatter(
    df,
    x='date',
    y='passengers',
    labels={'passengers':'Passeggeri', 'date':'Data'},
    title=f'Passeggeri mensili e fit polinomiale (grado {degree})'
)
fig.add_scatter(
    x=df['date'],
    y=df['predicted'],
    mode='lines',
    name='Fit polinomiale',
    line=dict(width=3)
)
fig.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01))
#fig.show()
#fig.write_image("passengers_fit.png", width=800, height=500)



#2
