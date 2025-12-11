from funcionC import conductividad
import time
from machine import ADC, Pin
import json

# Listas para almacenar acumulados
datos = [0, 0, 0]  # [cond, ph, turb]

# Configurar ADC una sola vez
sensor_turb = ADC(Pin(34))
sensor_turb.atten(ADC.ATTN_11DB)

sensor_ph = ADC(Pin(32))
sensor_ph.atten(ADC.ATTN_11DB)

# --- Proceso ---
for i in range(50):
    for _ in range(3):

        # conductividad (función externa)
        cond = conductividad()

        # turbidez
        turb = sensor_turb.read()

        # ph
        ph = sensor_ph.read()

        # Acumular cada sensor
        datos[0] += cond
        datos[1] += ph
        datos[2] += turb
        print("cond= ",cond," ph= ",ph," tubr= ",turb)
        time.sleep(0.2)

# Promedio de cada sensor
for i in range(3):
    datos[i] /= 50
 

arch={
    "cond":datos[0],
    "ph":datos[1],
    "turb":datos[2]}
print("Promedios:", arch)

#json
archivo="archivo.json"
with open(archivo,"w") as file:
    json.dump(arch, file)

    
    