import oceansdb

# with oceansdb.WOA() as db:
#     db.keys()
#     t = db['sea_water_temperature'].extract(var='mean', doy=136.875, depth=0, lat=17.5, lon=-37.5)
#     t = db['sea_water_salinity'].extract(var='mean', doy=136.875, depth=[0, 10, 15, 18], lat=17.5, lon=-37.5)
#     t = db['sea_water_temperature'].extract(var='mean', doy=136.875, lat=17.48, lon=[-39, -37.5, -35.2])

with oceansdb.CARS() as db:
    t = db['sea_water_temperature'].extract(var='mean', doy=136.875, lat=44.69, lon=[-63.62, -63.637, -63.655], depth=[0,10,30,60])

# with oceansdb.ETOPO(resolution='1min') as db:
#     h = db['topography'].extract(lat=17.5, lon=0)
