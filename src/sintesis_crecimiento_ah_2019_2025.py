"""Síntesis multitemporal 2019-2025 del crecimiento de asentamientos humanos
en los distritos de Conchagua y La Unión (La Unión Sur, El Salvador).
Consolida los cortes anuales en una capa vectorial única con atribución distrital
y calcula métricas anuales en hectáreas en proyección UTM Zona 16N (EPSG:32616).
"""
from pathlib import Path
import geopandas as gpd
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
CAPAS = ROOT / "geovisor" / "capas"

def sintetizar_crecimiento() -> pd.DataFrame:
    gdf = gpd.read_file(CAPAS / "crecimiento_ah_consolidado_2019_2025.geojson")
    resumen = (
        gdf.groupby(["anio", "distrito"], as_index=False)
        .agg(poligonos_n=("area_ha", "count"), superficie_ha=("area_ha", "sum"))
    )
    resumen["superficie_ha"] = resumen["superficie_ha"].round(2)
    return resumen

if __name__ == "__main__":
    print(sintetizar_crecimiento().to_string(index=False))
