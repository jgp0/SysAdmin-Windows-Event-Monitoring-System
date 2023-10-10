import time
import csv
import win32evtlog

# Función para obtener eventos del sistema de Windows
def obtener_eventos_sistema():
    eventos = []
    servername = None
    logtype = "System"
    hand = win32evtlog.OpenEventLog(servername, logtype)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    total = win32evtlog.GetNumberOfEventLogRecords(hand)

    events = win32evtlog.ReadEventLog(hand, flags, 0)
    for event in events:
        eventos.append(event.StringInserts)
    
    win32evtlog.CloseEventLog(hand)
    return eventos

# Función para mostrar eventos en tiempo real
def mostrar_eventos_en_tiempo_real(ruta_csv):
    while True:
        eventos = obtener_eventos_sistema()
        if eventos:
            for evento in eventos:
                print(evento)
                # Guardar evento en el archivo CSV especificado
                guardar_evento_en_csv(ruta_csv, evento)
        time.sleep(5)  # Espera 5 segundos antes de volver a verificar

# Función para guardar eventos en un archivo CSV
def guardar_evento_en_csv(ruta_csv, evento):
    with open(ruta_csv, mode="a", newline="", encoding="utf-8") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), evento])

if __name__ == "__main__":
    print("Sistema de Monitorización de Eventos del Sistema (Windows)")
    ruta_csv = "data/syslogs.csv"  # Reemplaza con la ruta deseada
    # Crea el archivo CSV si no existe y escribe un encabezado
    with open(ruta_csv, mode="w", newline="", encoding="utf-8") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(["Timestamp", "Evento"])
    mostrar_eventos_en_tiempo_real(ruta_csv)