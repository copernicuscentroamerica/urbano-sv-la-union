## Metodología de consolidación multitemporal 2019–2025

1. **Estandarización geométrica y métrica anual:** Reproyección al sistema métrico **UTM Zona 16N (EPSG:32616)** de las siete capas anuales (`Crecimiento_AH_LU_CH_2019` a `2025`) para cuantificar el área exacta en hectáreas de cada polígono y publicar geometrías limpias en **EPSG:4326**.
2. **Asignación espacial distrital:** Cruce por centroide e intersección con los límites de **Distrito de Conchagua** y **Distrito de La Unión** (`src/sintesis_crecimiento_ah_2019_2025.py`).
3. **Integración en capa síntesis única:** Construcción de `crecimiento_ah_consolidado_2019_2025.geojson` con simbología secuencial por cohorte anual y tabla de indicadores verificables.
