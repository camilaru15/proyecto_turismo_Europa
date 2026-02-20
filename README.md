# Pandas & Data Visualization Project  
## Análisis del Turismo en Europa

## 📌 Objetivo del proyecto
El objetivo de este proyecto es realizar un **Análisis Exploratorio de Datos (EDA) reproducible** utilizando Python, Pandas y herramientas de visualización, a partir de un dataset real sobre turismo en Europa.  
Se busca identificar patrones temporales, geográficos y diferencias entre turismo nacional e internacional.

---

## Dataset
- **Fuente**: Eurostat  
- **Formato**: CSV  
- **Archivo**: `turismo_europa.csv`  
- **Ubicación**: `data/raw/turismo_europa.csv`

El dataset contiene información sobre el número de estancias turísticas en países y regiones de Europa, desglosadas por año, tipo de residencia del turista (nacional o extranjero) y otras dimensiones relevantes.

---

## Preguntas de análisis
- ¿Cómo ha evolucionado el turismo en Europa a lo largo del tiempo?
- ¿Qué países concentran el mayor número de estancias turísticas?
- ¿Existe una diferencia significativa entre el turismo nacional y el internacional?
- ¿Cómo se distribuyen los valores de estancias y qué tipo de asimetría presentan?

---

## Pipeline del proyecto
El análisis sigue un pipeline reproducible implementado tanto en el notebook como en `main.py`:

1. **Carga del dataset** desde `data/raw/`
2. **Limpieza de datos**:
   - Eliminación de columnas irrelevantes
   - Tratamiento de valores nulos
   - Normalización de categorías
   - Conversión de tipos
3. **Creación de features**:
   - Década
   - Transformación logarítmica de estancias
   - Variable binaria de turismo nacional vs internacional
4. **Visualización de datos**
5. **Exportación del dataset limpio** a `data/processed/`

---

## Feature Engineering
Se crearon las siguientes variables adicionales:

- **decade**: década correspondiente al año de observación.
- **log_obs_value**: transformación logarítmica del número de estancias para reducir asimetría.
- **is_international**: variable binaria que identifica turismo internacional (`FOR`) frente a nacional (`DOM`).

---

## Visualizaciones realizadas
Se generaron visualizaciones con intención analítica y buena presentación:

- Evolución del turismo en Europa por año
- Top 10 países con mayor número de estancias
- Comparación entre turismo nacional e internacional
- Distribución del número de estancias (histograma)

Cada visualización incluye título, etiquetas de ejes e interpretación en el notebook.

---

## Principales hallazgos
- El turismo en Europa muestra una **tendencia creciente** a lo largo del periodo analizado.
- La actividad turística está **concentrada en un número reducido de países**.
- El **turismo internacional** representa una parte significativa del total de estancias.
- La distribución de estancias es **asimétrica**, lo que justifica el uso de transformaciones logarítmicas.

---

##  Cómo ejecutar el proyecto

### 1. Clonar el repositorio
```bash
git clone https://github.com/camilaru15/proyecto_turismo_Europa.git
cd proyecto_turismo_Europa