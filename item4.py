conexion netconf.py   #conectarse por netconf                                                                                                                                                             from ncclient import manager

try:
    with manager.connect(
        host="192.168.56.109",
        port=830,
        username="cisco",
        password="cisco123!",
        hostkey_verify=False
    ) as m:
        print("Conexión NETCONF exitosa con el router.")
except Exception as e:
    print("Error al conectar:", e)
    
    
    
    