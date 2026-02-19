def build_features(df):
    # Feature 1: Década
    df["decade"] = (df["TIME_PERIOD"] // 10) * 10

    # Feature 2: Log del turismo (reduce skew)
    df["log_obs_value"] = df["OBS_VALUE"].apply(lambda x: 0 if x <= 0 else __import__("math").log(x))

    # Feature 3: Turismo internacional (binaria)
    df["is_international"] = df["c_resid"].apply(
        lambda x: 1 if x != "domestic" else 0
    )

    return df
