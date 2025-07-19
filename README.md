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
│   ├── florence_2018_data.py    # Data download script
│   └── florence_2018.json       # Hurricane Florence track data
├── notebooks/
│   ├── load_Visualise_us_map.ipynb  # US map visualization
│   └── Starteripynb                 # Starter notebook
├── outputs/                     # Generated visualizations and results
├── README.md                    # This file
└── LICENSE                      # Project license
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

## 📊 Analysis Notebooks

### 1. US Map Visualization (`load_Visualise_us_map.ipynb`)
- **Purpose**: Load and visualize the base US States map from GeoJSON
- **Features**:
  - Creates a canvas for plotting Hurricane Florence tracks
  - Demonstrates geospatial data handling with GeoPandas
  - Shows how to clean geospatial data (removing Alaska/Hawaii)

### 2. Starter Notebook (`Starteripynb`)
- Entry point for new analysis workflows
- Template for additional hurricane analysis

## 🛠️ Tools and Libraries

- **`requests`** - HTTP requests for data download
- **`geopandas`** - Geospatial data manipulation and analysis
- **`matplotlib`** - Data visualization and mapping
- **`pandas`** - Data manipulation and analysis
- **`json`** - JSON data processing

## 📈 Key Features

- **Automated Data Collection**: Script-based download of hurricane data
- **Geospatial Analysis**: Professional mapping and spatial analysis
- **Reproducible Workflows**: Jupyter notebooks for analysis
- **Data Validation**: Error handling and status checking

## 🔍 Data Sources

- **Primary Source**: [flhurricane.com](https://flhurricane.com/cyclone/stormhistory.php?j=1&year=2018&storm=6)
- **Data Type**: Hurricane advisory data in JSON format
- **Coverage**: Hurricane Florence (2018) complete track

## 📝 Usage Examples

### Load and Inspect Data
```python
import json

with open('data/florence_2018.json', 'r') as f:
    data = json.load(f)

print(f"Total advisories: {len(data)}")
print("First advisory:", data[0])
```

### Basic Geospatial Analysis
```python
import geopandas as gpd
import matplotlib.pyplot as plt

# Load US states map
states = gpd.read_file('path_to_us_states.geojson')
states.plot()
plt.title('US States Map')
plt.show()
```

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

## 📞 Support

For questions or issues:
1. Check the existing notebooks for examples
2. Review the data structure documentation above
3. Open an issue in the repository

---

**Note**: This project is for educational and research purposes. Always verify data accuracy and cite sources appropriately.
