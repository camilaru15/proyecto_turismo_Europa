from src.io import load_data
from src.cleaning import basic_cleaning

def main():
    # Cargar
    df = load_data("data/raw/turismo_europa.csv")
    
    #Limpiar
    df_clean = basic_cleaning(df)
    
    #Guardar procesado (opcional)
    df_clean.to_csv("data/processed/turismo_europa_clean.csv", index=False)
    
    print("Pipeline completo. Dataset limpio guardado en data/processed/")

if __name__ == "__main__":
    main()
