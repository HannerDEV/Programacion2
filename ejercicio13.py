import random
import datetime
import pandas as pd


def calculate_time(original_function):
    def wrapper_function(*args, **kwargs):
        pre = datetime.datetime.now()
        result = original_function(*args, **kwargs)
        pos = datetime.datetime.now()
        sorted()

        print(f"Execution time: {pos - pre} segundos")
        return result
    return wrapper_function

def verify_data(original_function):
    def wrapper_function(datos, *args, **kwargs):

        if not datos:
            raise ValueError("There are not values in the sensors")
        
        result = original_function(datos, *args, **kwargs)

        return result
    return wrapper_function

def parametrize_thresshold(threshold):
    def decorator(original_function):
        def wrapper_function(*args, **kwargs):
            kwargs["superior_thresshold"] = threshold
            return original_function(*args, **kwargs)
        return wrapper_function
    return decorator

@calculate_time
def generar_datos():
    datos = {}
    lecturas_diarias = 2*60*24
    for sensor in range(1, 101):
        lecturas = []
        sensor_name = f"Sensor_{sensor}"
        for day in range(1, 8):
            for i in range(lecturas_diarias):
                temp = random.randint(0, 90)
                hora = i // 2 // 60
                lecturas.append((hora, temp))
        datos[sensor_name] = lecturas

    return datos

@verify_data
@calculate_time
def calcular_estadisticas(datos):
    all_temps = [temp for lecturas in datos.values() for _, temp in lecturas]
    values = pd.Series(all_temps)

    media = values.mean()
    mediana = values.median()
    moda = values.mode()[0]

    return {"media": media, "mediana": mediana, "moda": moda}

@parametrize_thresshold(threshold=70)
@verify_data
@calculate_time
def analyze_rises(datos, superior_thresshold = 70, mid_thresshold = 50):
    conteo_horas_criticas = {n: 0 for n in range(24)}
    sensores_criticos = {sensor: 0 for sensor in datos}

    clasificacion = {"bajo": 0, "medio": 0, "alto": 0}

    for sensor, lecturas in datos.items():
        for hora, tem in lecturas:
            if tem >= superior_thresshold:
                conteo_horas_criticas[hora] += 1
                sensores_criticos[sensor] += 1
                clasificacion["alto"] += 1
                continue
            if tem>= mid_thresshold:
                clasificacion["medio"] += 1
                continue
            else:
                clasificacion["bajo"] += 1

    max_conteo = 0
    max_hora = 0

    for hora, conteo  in conteo_horas_criticas.items():
        if conteo > max_conteo:
            max_conteo = conteo
            max_hora = hora

    sensores_ordenados = sorted(sensores_criticos.items(), key=lambda x: x[1], reverse=True)
    top_sensores_criticos = sensores_ordenados[:5]

    return clasificacion, max_hora, top_sensores_criticos, conteo_horas_criticas

def main():
    print("==================================================")
    print(" SISTEMA DE CONTROL DE TEMPERATURA")
    print("==================================================\n")
    datos = generar_datos()
    statics = calcular_estadisticas(datos)

    print("Datos de los sensores")
    print(f"Media: {statics['media']}")
    print(f"Mediana: {statics['mediana']}")
    print(f"Moda: {statics['moda']}")

    clasificacion, hora_critica, top_sensores, conteo_horas = analyze_rises(datos)


    print("\n--- CLASIFICACIÓN DEL CONSUMO / RIESGO ---")
    print(f"Riesgo Bajo     (< 40°C) : {clasificacion['bajo']} lecturas")
    print(f"Riesgo Moderado (40-70°C): {clasificacion['medio']} lecturas")
    print(f"Riesgo Alto     (> 70°C) : {clasificacion['alto']} lecturas")

    print(f"\n--- HORA DE MAYOR RIESGO EN EL DÍA ---")
    print(f"La hora pico de sobrecalentamiento es entre las {hora_critica}:00 y las {hora_critica}:59 hs "
          f"con {conteo_horas[hora_critica]} eventos críticos.")

    print("\n--- TOP 5 SENSORES MÁS CRÍTICOS ---")
    for sensor, num_alertas in top_sensores:
        print(f"{sensor}: {num_alertas} alertas críticas registradas")





if __name__ == "__main__":
    main()
