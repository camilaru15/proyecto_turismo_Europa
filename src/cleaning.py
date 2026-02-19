def basic_cleaning(df):
    # Eliminar columnas irrelevantes
    cols_to_drop = [
        "DATAFLOW", "LAST UPDATE", "OBS_FLAG", "CONF_STATUS"
    ]
    df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])

    # Eliminar nulos
    df = df.dropna()

    # Tipos correctos
    df["TIME_PERIOD"] = df["TIME_PERIOD"].astype(int)
    df["OBS_VALUE"] = df["OBS_VALUE"].astype(float)

    # Normalizar categorías
    df["c_resid"] = df["c_resid"].str.lower()
    df["geo"] = df["geo"].str.upper()

    # Eliminar duplicados
    df = df.drop_duplicates()

    return df

