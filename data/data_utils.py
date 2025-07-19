"""
Data utility functions for Hurricane Florence geospatial analysis.
"""

import json
from pathlib import Path
from typing import Union


def cyclone_json_to_geojson(
    input_path: Union[str, Path],
    output_path: Union[str, Path],
    lat_key: str = "Lat",
    lon_key: str = "Long"
) -> Path:
    """
    Convert a cyclone advisory JSON (list of dicts) to a
    GeoJSON FeatureCollection of Point geometries.

    Parameters
    ----------
    input_path : str | Path
        Path to the raw advisory JSON file.
    output_path : str | Path
        Where to write the GeoJSON file.
    lat_key, lon_key : str, default "Lat", "Long"
        Keys in each advisory dict that hold latitude and longitude.

    Returns
    -------
    Path
        The path to the written GeoJSON file.
    """
    input_path = Path(input_path)
    output_path = Path(output_path) / "florence_2018.geojson"

    # Load the raw advisory list
    with input_path.open() as f:
        advisories = json.load(f)

    # Wrap each advisory in a GeoJSON Feature
    features = []
    for item in advisories:
        try:
            # Extract coords and convert to float
            lat = float(item[lat_key])
            lon = float(item[lon_key])

            # Build GeoJSON Feature
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon, lat]   # GeoJSON = [x, y] = [lon, lat]
                },
                # Everything *except* Lat/Long becomes properties
                "properties": {k: v for k, v in item.items() if k not in {lat_key, lon_key}}
            }
            features.append(feature)
        except (KeyError, ValueError):
            # Skip rows with missing or malformed coordinates
            continue

    # Assemble FeatureCollection
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    # Write to file
    with output_path.open("w") as f:
        json.dump(geojson, f)

    return output_path 