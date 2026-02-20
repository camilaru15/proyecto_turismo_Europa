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

def plot_top_countries(df, top_n=10):
    data = (
        df.groupby("geo")["OBS_VALUE"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
    )

    plt.figure(figsize=(10,6))
    sns.barplot(x=data.values, y=data.index)
    plt.title(f"Top {top_n} países con mayor número de estancias")
    plt.xlabel("Número de estancias")
    plt.ylabel("País")
    plt.tight_layout()
    plt.show()

def plot_domestic_vs_international(df):
    data = (
        df.groupby("tourism_type")["OBS_VALUE"]
        .sum()
        .reset_index()
    )
    plt.figure(figsize=(8, 5))

    ax = sns.barplot(
        data=data,
        x="tourism_type",
        y="OBS_VALUE"
    )

    # Agregar etiquetas numéricas
    for i, value in enumerate(data["OBS_VALUE"]):
        ax.text(
            i,
            value,
            f"{value:,.0f}",
            ha="center",
            va="bottom"
        )
        
    plt.title("Turismo nacional vs internacional", fontsize=14)
    plt.xlabel("Tipo de turismo")
    plt.ylabel("Número total de estancias")
    plt.tight_layout()
    plt.show()

def plot_distribution_obs_value(df):
    plt.figure(figsize=(8,5))
    sns.histplot(df["OBS_VALUE"], bins=50, kde=True)
    plt.title("Distribución del número de estancias")
    plt.xlabel("Número de estancias")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()