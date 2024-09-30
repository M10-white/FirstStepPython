speed_kmh = float(input('Veuillez entrer une vitesse en Km/h :'))

kmh_to_mph = 1.609
speed_mph = speed_kmh / kmh_to_mph

print('En Km/h')
print('-> ' ,speed_kmh)
print('En M/h')
print('-> ' ,round(speed_mph, 2))