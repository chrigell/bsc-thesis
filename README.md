# BSc Thesis Code Repository

This repository contains the code developed and used for the Bachelor’s thesis  
**“Towards a Definition of Wind
Thresholds for Thunderstorm
Events: A Qualitative Case Study
for Swiss Campgrounds”**, submitted at the **Climate Impact Research Group, Institute of Geography, University of Bern**.

The scripts were used to process ensemble forecast data, compute wind and precipitation exceedances, and generate the figures and tables presented in the thesis. The repository serves as a supplementary material to ensure transparency and reproducibility.

## Data Availability

The analyses are based on ensemble forecast data from MeteoSwiss (ICON-CH1-EPS).  
The input data are not included in this repository, but can be requested on demand.

## Usage

The code is provided as research code accompanying the thesis and is not intended as a standalone or operational software package. The scripts were executed in the context described in the thesis manuscript.

## Citation

If you use this code, please cite the thesis accordingly:

> [Christian Wenger] (2025): *Towards a Definition of Wind Thresholds for Thunderstorm Events: A Qualitative Case Study for Swiss Campgrounds*. Bachelor’s thesis, [University of Bern].
>
## Code Overview

This repository contains scripts, notebooks, and configuration files used for the analyses presented in the thesis. The main components are:

### Python scripts

- **write_sustained_wind_precip_files.py**  
  Prepares and writes sustained wind and precipitation data used in subsequent analyses.

- **aggregation_6h_sustained_wind_precip.py**  
  Aggregates sustained wind and precipitation to 6-hour frames.
  
- **aggregation_6h_gust.py**  
  Aggregates wind gust data to 6-hour frames.

### Jupyter notebooks

- **warn_times_2024.ipynb**  
  Analysis of the warning times for the 2024 case studies.

- **analysis_gust_precip.ipynb**  
  Analysis of wind gust and precipitation exceedances for the 2024 case studies.

### Configuration and case definition files

- **warnlevels.json**  
  Definition of wind and precipitation warning thresholds used throughout the analysis.

- **cases.json**  
  Case study definitions, including timing and domain information.

