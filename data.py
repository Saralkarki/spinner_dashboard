import pandas as pd

df = pd.read_csv('spinners.csv')

player_names = df.Name.unique()
# print(player_names)
df_econ = df[['Name','Econ']]

df_adil_econ = x = pd.DataFrame(df_econ.iloc[0]).T
df_sandy_econ = x = pd.DataFrame(df_econ.iloc[1]).T
df_warne_econ = df_econ.iloc[2][1] 
df_kumble_econ = df_econ.iloc[3][1] 
df_rashid_econ = df_econ.iloc[4][1] 
df_chahal_econ = df_econ.iloc[5][1] 
df_mishra_econ = df_econ.iloc[6][1] 
df_zampa_econ = df_econ.iloc[7][1] 
df_tahir_econ = df_econ.iloc[8][1] 
econ_df = [df_adil_econ, df_sandy_econ, df_warne_econ, df_kumble_econ, df_rashid_econ, df_chahal_econ,df_mishra_econ,
df_zampa_econ, df_tahir_econ]

