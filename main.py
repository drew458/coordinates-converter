def coordinatesToDecimal(degreeslat, degreeslong, minuteslat, minuteslong):
    # Equation for the conversion
    minutesconvlat = minuteslat / 60
    lat = degreeslat + minutesconvlat

    print(lat)

    minutesconvlong = minuteslong / 60
    long = degreeslong + minutesconvlong

    print(long)


print('Inserire i gradi della Latitudine: ')
latitudeDegrees = input()
print('Inserire i minuti della Latitudine: ')
latitudeMinutes = input()
print('Inserire i gradi della Longitudine: ')
longitudeDegrees = input()
print('Inserire i minuti della Longitudine: ')
longitudeMinutes = input()

coordinatesToDecimal(latitudeDegrees, longitudeDegrees, latitudeMinutes, longitudeMinutes)
