class estacion():

    def __init__(self, lat, long):
        self.longitud = long
        self.latitud = lat

    def dondeEstoy(self):
        print(f"latitud: {self.latitud}\nlongitud: {self.longitud}")


leon = estacion(42.57682, -5.59698)
santiago = estacion(42.90510, -8.50701)
madrid = estacion(40.51642, -3.89502)
barcelona = estacion(41.40124, 2.19122)
sevilla = estacion(37.39523, -6.01029)

# pista1 = 3L-4M+2Se
latitud_objetivo = round(3 * leon.latitud - 4 * madrid.latitud + 2 * sevilla.latitud, 5)
# pista2 = 6L-4Sa-2B
longitud_objetivo = round(6 * leon.longitud - 4 * santiago.longitud - 2 * barcelona.longitud, 5)

objetivo = estacion(latitud_objetivo, longitud_objetivo)
objetivo.dondeEstoy()
