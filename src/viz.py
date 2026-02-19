import matplotlib.pyplot as plt
import seaborn as sns

def plot_tourism_by_year(df):
    data = df.groupby("TIME_PERIOD")["OBS_VALUE"].sum()

    plt.figure(figsize=(10,5))
    plt.plot(data.index, data.values)
    plt.title("Evolución del turismo en Europa")
    plt.xlabel("Año")
    plt.ylabel("Número de estancias")
    plt.tight_layout()
    plt.show()

def plot_top_countries(df):
    latest_year = df["TIME_PERIOD"].max()

    data = (
        df[df["TIME_PERIOD"] == latest_year]
        .groupby("GEO")["OBS_VALUE"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )

    plt.figure(figsize=(10,5))
    sns.barplot(data=data, x="GEO", y="OBS_VALUE")
    plt.title(f"Top 5 países con más turismo ({latest_year})")
    plt.xlabel("País")
    plt.ylabel("Número de estancias")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return data