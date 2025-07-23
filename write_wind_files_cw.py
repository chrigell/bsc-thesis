import xarray as xr
import numpy as np
 
months = ['05','06','07','08','09']
 
for m in months:
    print('Processing month: ',m, flush=True)
    sample = xr.open_dataset(f"/scratch2/fzukanovic/fcstveri/ICON-CH1_monthly/ICON-CH1_{m}_2024.nc")
    sample['wind_speed'] = np.sqrt(sample.U_10M**2 + sample.V_10M**2)
    sample.to_netcdf(f'/scratch2/cwenger/ICON-CH1_monthly/ICON-CH1_{m}_2024_copy.nc', mode='w')
    print('Saved file for month ',m,flush=True)