import pandas as pd
df = pd.read_csv("stats.csv",sep=",")
df.loc[(df["Opperator"] == "Ash") & (df["Site"] == "1st"),["Wins"]] += 1
df.to_csv("stats.csv",index=False)
