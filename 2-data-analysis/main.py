import pandas as pd

df_stats = pd.read_csv("/home/myri/Documents/Coding projects/ao3trendingpage/data-extraction/ATEEZ/ATEEZ_2024-01-05 14:44:28.514477.csv", encoding="unicode_escape")
print(df_stats.info())

