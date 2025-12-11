import time
from machine import ADC, Pin
def conductividad():
   
    

    # --- Configuración ---
    TdsSensorPin = 33      # Pin analógico (puedes cambiarlo)
    VREF = 3.3               # Voltaje de referencia del ADC
    SCOUNT = 30              # Número de muestras
    temperature = 27          # Temperatura (para compensación)

    # --- Inicializar ADC ---
    tds_sensor = ADC(Pin(TdsSensorPin))
    tds_sensor.atten(ADC.ATTN_11DB)   # Permite leer hasta ~3.3V
    tds_sensor.width(ADC.WIDTH_12BIT) # Resolución de 12 bits (0–4095)

    # --- Buffer para muestras ---
    analogBuffer = [0] * SCOUNT

    # --- Función para obtener la mediana ---
    def getMedianNum(data):
        sorted_data = sorted(data)
        length = len(sorted_data)
        if length % 2 == 1:
            return sorted_data[length // 2]
        else:
            return (sorted_data[length // 2 - 1] + sorted_data[length // 2]) / 2

    # --- Bucle principal ---
        # Leer muestras
    for i in range(SCOUNT):
        analogBuffer[i] = tds_sensor.read()
         # cada 40 ms

        # Calcular valor medio (filtrado por mediana)
    median_value = getMedianNum(analogBuffer)
    averageVoltage = median_value * (VREF / 4095.0)

        # Compensación por temperatura
    compensationCoefficient = 1.0 + 0.02 * (temperature - 25.0)
    compensationVoltage = averageVoltage / compensationCoefficient

        # Convertir a valor TDS (ppm)
    tdsValue = (133.42 * compensationVoltage**3
                - 255.86 * compensationVoltage**2
                + 857.39 * compensationVoltage) * 0.5

    return tdsValue
    

