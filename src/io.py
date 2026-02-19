import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """
    Carga el dataset desde un CSV.
    """
    df = pd.read_csv(path)
    return df
