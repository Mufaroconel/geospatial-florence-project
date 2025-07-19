# 🌪️ Hurricane Florence Geospatial Analysis Project

A comprehensive geospatial analysis project focused on Hurricane Florence (2018) using Python and geospatial libraries. This project downloads, processes, and visualizes hurricane track data to understand the storm's path and characteristics.

## 📋 Project Overview

This project analyzes Hurricane Florence's track data from 2018, including:
- **Data Collection**: Automated download of hurricane advisory data
- **Geospatial Processing**: Mapping and visualization of storm tracks
- **Data Analysis**: Examination of wind speeds, pressure, and movement patterns

## 🗂️ Project Structure

```
geospatial_florence_project/
├── data/
│   ├── florence_2018_data.py        # Data download script
│   ├── florence_2018.json           # Hurricane Florence track data (raw JSON)
│   ├── florence_2018.geojson        # Hurricane Florence track data (GeoJSON)
│   ├── data_utils.py                # Reusable data processing functions
│   ├── gz_2010_us_outline_5m.json   # US map outline (5m resolution)
│   └── gz_2010_us_outline_500k.json # US map outline (500k resolution)
├── notebooks/
│   ├── Starter.ipynb                # Starter notebook (uses reusable module)
│   └── load_Visualise_us_map.ipynb  # US map visualization
├── outputs/                         # Generated visualizations and results
├── config.py                        # Centralized configuration for paths
├── README.md                        # This file
└── LICENSE                          # Project license
```

## 🚀 Getting Started

### Prerequisites

Install the required Python packages:

```bash
pip install requests geopandas matplotlib pandas numpy
```

### Data Download

1. **Download Hurricane Florence Data:**
   ```bash
   cd data
   python florence_2018_data.py
   ```
   This script downloads the latest hurricane advisory data from [flhurricane.com](https://flhurricane.com) and saves it as `florence_2018.json`.

2. **Verify Data Download:**
   ```bash
   ls -l data/florence_2018.json
   ```

### Data Structure

The downloaded JSON contains hurricane advisory data with the following structure:
```json
{
  "AdvisoryNumber": "1",
  "Date": "08/30/2018 11:00",
  "Lat": "12.9",
  "Long": "18.4",
  "Wind": "30",
  "Pres": "1007",
  "Movement": "W at 12 MPH (280 deg)",
  "Type": "Potential Tropical Cyclone",
  "Name": "Six",
  "Received": "08/30/2018 10:45",
  "Forecaster": "Avila"
}
```

## 🛠️ Code Reusability

- The function to convert JSON to GeoJSON is now in `data/data_utils.py`.
- Use this function in your notebooks by importing it, rather than redefining it.

**Example usage in a notebook:**
```python
import sys
from pathlib import Path

# Add project root to path for imports
project_root = Path.cwd().parent
sys.path.append(str(project_root))

from data.data_utils import cyclone_json_to_geojson

data_path = "data/florence_2018.json"
output_path = "data/"
geojson_file = cyclone_json_to_geojson(input_path=data_path, output_path=output_path)
```

Or, if you want to use the centralized config:
```python
import sys
from pathlib import Path
project_root = Path.cwd().parent
sys.path.append(str(project_root))
import config
from data.data_utils import cyclone_json_to_geojson
geojson_file = cyclone_json_to_geojson(input_path=config.FLORENCE_JSON, output_path=config.DATA_DIR)
```

## 📊 Analysis Notebooks

### 1. US Map Visualization (`load_Visualise_us_map.ipynb`)
- **Purpose**: Load and visualize the base US States map from GeoJSON
- **Features**:
  - Creates a canvas for plotting Hurricane Florence tracks
  - Demonstrates geospatial data handling with GeoPandas

### 2. Starter Notebook (`Starter.ipynb`)
- Entry point for new analysis workflows
- Demonstrates code reusability by importing from `data_utils.py`

## 🛠️ Tools and Libraries

- **`requests`** - HTTP requests for data download
- **`geopandas`** - Geospatial data manipulation and analysis
- **`matplotlib`** - Data visualization and mapping
- **`pandas`** - Data manipulation and analysis
- **`json`** - JSON data processing

## 🔍 Data Sources

- **Primary Source**: [flhurricane.com](https://flhurricane.com/cyclone/stormhistory.php?j=1&year=2018&storm=6)
- **Data Type**: Hurricane advisory data in JSON format
- **Coverage**: Hurricane Florence (2018) complete track

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.

## 🙏 Acknowledgments

- Data provided by [flhurricane.com](https://flhurricane.com)
- Built with Python geospatial ecosystem (GeoPandas, Matplotlib)

---

**Note**: This project is for educational and research purposes. Always verify data accuracy and cite sources appropriately.
