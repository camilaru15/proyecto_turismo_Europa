def build_features(df):
    # Feature 1: Década
    df["decade"] = (df["TIME_PERIOD"] // 10) * 10

    # Feature 2: Log del turismo (reduce skew)
    df["log_obs_value"] = df["OBS_VALUE"].apply(lambda x: 0 if x <= 0 else __import__("math").log(x))

    # Feature 3: Turismo internacional vs nacional
    # Limpieza de categoría
    df["c_resid"] = df["c_resid"].astype(str).str.strip().str.upper()

    # crea Variable categorica
    df["tourism_type"] = df["c_resid"].replace({
    "FOREIGN COUNTRY": "Internacional",
    "TOTAL": "total"
    })

    return df
