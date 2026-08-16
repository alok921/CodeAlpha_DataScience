

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Unemployment_Rate.csv")


print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())


df.columns = df.columns.str.strip()


print("\nStatistical Summary:")
print(df.describe())


if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")


rate_column = None

for column in df.columns:
    if "Unemployment Rate" in column:
        rate_column = column
        break

if rate_column:

    print("\nAverage Unemployment Rate:")
    print(df[rate_column].mean())

    print("\nMaximum Unemployment Rate:")
    print(df[rate_column].max())

    print("\nMinimum Unemployment Rate:")
    print(df[rate_column].min())

   
    if "Date" in df.columns:

        plt.figure(figsize=(10, 5))

        plt.plot(
            df["Date"],
            df[rate_column],
            marker="o"
        )

        plt.title("Unemployment Rate Trend")
        plt.xlabel("Date")
        plt.ylabel("Unemployment Rate (%)")
        plt.xticks(rotation=45)
        plt.grid(True)

        plt.tight_layout()
        plt.show()

else:
    print("\nUnemployment Rate column not found.")


print("\nCorrelation Matrix:")
print(df.select_dtypes(include="number").corr())
