import xarray as xr

aggregation_time = 6
months = ['05','06','07','08','09']

for month in months:
    print(f'Processing month: {month}',flush=True)
    # Open the dataset for the specific month
    ds = xr.open_dataset(f'/scratch2/cwenger/ICON-CH1_monthly/ICON-CH1_{month}_2024_copy.nc')
    # delete first two time steps and last time step
    ds = ds.isel(time=slice(2, 32))
    # aggregation to 6h maximum
    ds = ds.coarsen(time=aggregation_time, boundary='exact').max()
    
    # rename the time coordinate
    new_time_values = [0, 6, 12, 18, 24]
    ds = ds.assign_coords(time=new_time_values)

    print(f"calculations done for month {month} done", flush=True)

    ds.to_netcdf(f'/scratch2/cwenger/ICON-CH1_monthly/ICON-CH1_{month}_2024_agg.nc')