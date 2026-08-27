import pandas as pd
import numpy as np

df = pd.read_excel('03_MATRICULAS_ED_SUPERIOR_ANTOFAGASTA_2021.xlsx')

intervalos=round(1+3.3*np.log10(31596))

# Tabla de frecuencia del valor arancel en pesos por carrera.

df['VALOR ARANCEL (PESOS)'] = pd.cut(df['VALOR ARANCEL (PESOS)'], bins=intervalos, include_lowest=True)

f1 = df['VALOR ARANCEL (PESOS)'].value_counts(sort=False)
h1 = df['VALOR ARANCEL (PESOS)'].value_counts(sort=False, normalize=True)

ft = pd.DataFrame({

    'fi': f1,
    'Fi': f1.cumsum(),
    'hi (%)': (h1*100).round(2),
    'Hi (%)': (h1.cumsum() * 100).round(2)

    })

print(ft.to_string())
