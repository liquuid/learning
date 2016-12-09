metro_areas = [
    ('2qweasd', 'jk2', 23, (1234,1234)),
    ('qhweasd', 'jk3', 23, (1234,-1234)),
    ('gqweasd', 'jk4', 23, (1234,-1234)),
    ('bqweasd', 'jk5', 23, (1234,1234)),
    ('aqweasd', 'jk6', 23, (1234,-1234)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat', 'long'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))