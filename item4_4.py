rom ncclient import manager #cargar config por ncclient

# Datos de conexión al CSR1000v
router = {
    "host": "192.168.56.109",
    "port": 830,
    "username": "cisco",
    "password": "cisco123!",
    "hostkey_verify": False
}

# Configuración YANG para crear interfaz Loopback11
config = """
<config>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>Loopback11</name>
      <description>Loopback creada con NETCONF</description>
      <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
      <enabled>true</enabled>
      <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        <address>
          <ip>11.11.11.11</ip>
          <netmask>255.255.255.255</netmask>
        </address>
      </ipv4>
    </interface>
  </interfaces>
</config>
"""

# Conexión y envío de configuración
with manager.connect(**router) as m:
    m.edit_config(target="running", config=config)
    print("Loopback11 creada con 11.11.11.11/32")

