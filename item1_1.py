vlan = input("Ingrese el número de VLAN: ") 
vlan_num = int(vlan)

if vlan_num >= 1 and vlan_num <= 1005:
    print("La VLAN es del rango normal.")
elif vlan_num >= 1006 and vlan_num <= 4094:
    print("La VLAN es del rango extendido.")
else:
    print("Número de VLAN fuera del rango válido.")
