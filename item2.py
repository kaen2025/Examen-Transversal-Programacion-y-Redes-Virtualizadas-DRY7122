import openrouteservice

client = openrouteservice.Client(key='eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6ImRjNTMzMmEzYWM0MjQzYWNhNThkNDhlMzRmYTdjMDFiIiwiaCI6Im11cm11cjY0In0=')  # Reemplaza con tu API key

vel = {"auto": 80, "bus": 60, "avión": 700}
print("Viajes Chile-Argentina (s para salir)\n")

while True:
    o = input("Origen: ").title()
    if o == 'S': break
    d = input("Destino: ").title()
    if d == 'S': break
    m = input("Transporte (auto, bus, avión): ").lower()
    if m == 's' or m not in vel: break

    try:
        coor = [
            client.pelias_search(text=o)['features'][0]['geometry']['coordinates'],
            client.pelias_search(text=d)['features'][0]['geometry']['coordinates']
        ]
        ruta = client.directions(coordinates=coor, profile='driving-car')
        km = round(ruta['routes'][0]['summary']['distance'] / 1000, 2)
        millas = round(km * 0.621371, 2)
        tiempo = round(km / vel[m], 2)

        print(f"\n Desde {o} hasta {d} en {m}:")
        print(f" Distancia: {km} km | {millas} millas")
        print(f" Tiempo estimado: {tiempo} horas\n")
    except:
        print(" Error, intenta con otra ciudad.\n")