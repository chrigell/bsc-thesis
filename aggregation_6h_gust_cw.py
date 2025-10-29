import xarray as xr
from pathlib import Path

aggregation_time = 6
inits = [
    "2024-07-11T21",
    "2024-07-12T00",
    "2024-08-12T12",
    "2024-08-18T00",
    "2024-09-01T03",
    "2024-09-01T06",
    "2024-09-01T15",
]

indir = Path("/scratch2/cwenger/ICON-CH1_monthly/ICON-CH1_gust_data")
outdir = indir  # change if you want different output directory

for init in inits:
    inp = indir / f"ICON-CH1-EPS_{init}.nc"
    out = outdir / f"ICON-CH1-EPS_{init}._agg.nc"
    print(f"Processing {inp}", flush=True)

    # Open the dataset for the specific initialization time
    ds = xr.open_dataset(inp)

    # delete first two time steps and last time step
    ds = ds.isel(lead_time=slice(2, 32))

    # aggregation to 6h maximum
    ds = ds.coarsen(lead_time=aggregation_time, boundary='exact').max()
    
    # rename the time coordinate
    new_time_values = [0, 6, 12, 18, 24]
    ds = ds.assign_coords(lead_time=new_time_values)
    
    ds.to_netcdf(out)
    print(f"  wrote {out}", flush=True)