def assert_columns(df, required_cols):
    missing = set(required_cols) - set(df.columns)
    assert not missing, f"Faltan columnas: {missing}"

