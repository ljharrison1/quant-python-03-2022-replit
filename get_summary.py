import pandas as pd
surveys_df = pd.read_csv("surveys.csv")
print(surveys_df.describe())
print(surveys_df["weight"].describe())
