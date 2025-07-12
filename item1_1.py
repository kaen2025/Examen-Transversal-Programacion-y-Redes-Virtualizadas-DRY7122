vlan = input("Ingrese el número de VLAN: ") # pide el numero de vlan easy
vlan_num = int(vlan) # esto es porque la vlan siempre sera texto string y se requiere que sea numero entero

if vlan_num >= 1 and vlan_num <= 1005:
    print("La VLAN es del rango normal.")
elif vlan_num >= 1006 and vlan_num <= 4094:
    print("La VLAN es del rango extendido.")
else:
    print("Número de VLAN fuera del rango válido.")