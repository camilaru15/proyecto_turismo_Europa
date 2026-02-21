from src.io import load_data
from src.cleaning import basic_cleaning
from src.features import build_features

RAW_PATH = "data/raw/turismo_europa.csv"
OUT_PATH = "data/processed/turismo_europa_clean.csv"

def main():
    print("Cargando datos...")
    df = load_data(RAW_PATH)
    
    print("Limpiando datos...")
    df_clean = basic_cleaning(df)

    print("Creando features...")
    df_final = build_features(df_clean)
    
    print("Guardando dataset procesado...")
    df_final.to_csv(OUT_PATH, index=False)
    
    print("Pipeline completo ejecutado correctamente.")
    print(f"Archivo generado en: {OUT_PATH}")

if __name__ == "__main__":
    main()