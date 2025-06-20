import pandas as pd
from matplotlib import pyplot as plt
from matplotlib_venn import venn3

# Dados de exemplo
data = {
    'date': ['2025-06-01', '2025-06-02', '2025-06-03', '2025-06-04', '2025-06-05', '2025-06-06', '2025-06-07', '2025-06-08', '2025-06-09', '2025-06-10'],
    'sessions': [5, 6, 8, 10, 15, 18, 20, 15, 10, 15],  # Sessões(t)
    'time_played': [30, 40, 50, 70, 110, 130, 150, 80, 20, 60],  # T(t) em minutos
    'amount_bet': [100, 150, 200, 300, 450, 550, 650, 80, 100, 20]  # A(t) em R$
}
df = pd.DataFrame(data)

# Calcula diferenças e intervalos de tempo
df['time_diff'] = (pd.to_datetime(df['date']) - pd.to_datetime(df['date'].shift(1))).dt.days
df['sessions_diff'] = df['sessions'] - df['sessions'].shift(1)
df['time_played_diff'] = df['time_played'] - df['time_played'].shift(1)
df['amount_bet_diff'] = df['amount_bet'] - df['amount_bet'].shift(1)

# Calcula índices (evita divisão por zero)
df['IFA'] = df['sessions_diff'] / df['time_diff'].replace(0, 1)  # Índice de Frequência Aumentada ΔS/Δt
df['IAT'] = df['time_played_diff'] / df['time_diff'].replace(0, 1)  # Índice de Aceleração do Tempo ΔT/Δt  
df['IAG'] = df['amount_bet_diff'] / df['time_diff'].replace(0, 1)  # Índice de Aceleração de Gastos ΔA/Δt  

# Calcula ICRV com pesos típicos (w1 = 0.4, w2 = 0.3, w3 = 0.3)
w1, w2, w3 = 0.4, 0.3, 0.3
df['ICRV'] = w1 * df['IAG'] + w2 * df['IAT'] + w3 * df['IFA']

# Preenche valores NaN da primeira linha (sem dados anteriores)
df['IFA'] = df['IFA'].fillna(0)
df['IAT'] = df['IAT'].fillna(0)
df['IAG'] = df['IAG'].fillna(0)
df['ICRV'] = df['ICRV'].fillna(0)

# Avaliação de risco
for index, row in df.iterrows():
    risk_level = "Baixo"
    if row['IAG'] > 50:  # Alerta IAG por 3 dias consecutivos
        risk_level = "Possível comportamento compulsivo"
    if row['IAT'] > 30:  # Alerta IAT
        risk_level = "Alto risco"
    if row['IFA'] > 100:  # Alerta IFA
        risk_level = "Comportamento viciante emergente"
    if row['ICRV'] > 100:  # Alerta ICRV
        risk_level = "Necessidade de intervenção"
    print(f"Data: {row['date']}, IAG: {row['IAG']:.2f}, IAT: {row['IAT']:.2f}, IFA: {row['IFA']:.2f}, "
          f"ICRV: {row['ICRV']:.2f}, Nível de Risco: {risk_level}")

# Verifica se houve 3 dias consecutivos com IAG > 50
iag_threshold = 50
consecutive_days = (df['IAG'] > iag_threshold).rolling(window=3).sum()
if consecutive_days.max() >= 3:
    print("Alerta: Possível comportamento compulsivo detectado por 3 dias consecutivos.")
    
# seleciona as datas em que esse total >= 3
dias_risco = set(df.loc[consecutive_days >= 3, 'date'])

# 2) Define limiares para IAT, IAG e ICRV
thresholds = {
    'IAT': 30,
    'IAG': 50,
    'IFA': 100,
    'ICRV': 100,
}

# 3) Conjuntos de dias em que cada índice excede seu limiar
dias_IAT = set(df.loc[df['IAT'] > thresholds['IAT'], 'date'])
dias_IAG = set(df.loc[df['IAG'] > thresholds['IAG'], 'date'])
dias_IFA = set(df.loc[df['IFA'] > thresholds['IFA'], 'date'])
dias_ICRV = set(df.loc[df['ICRV'] > thresholds['ICRV'], 'date'])

# 4) Plot do Diagrama de Venn usando “dias de risco” como terceiro conjunto
plt.figure(figsize=(8, 8))
venn3(
    [dias_IAT, dias_risco, dias_IAG],
    set_labels=(
        f'IAT > {thresholds["IAT"]}',
        'Comportamento abusivo constante detectado\n',
        f'IAG > {thresholds["IAG"]}'
    )
)
plt.title('Venn: IAT, IAG e Dias de Comportamento Compulsivo')
plt.savefig('venn3_risco.png', bbox_inches='tight')
plt.show()