import psutil

#   Captura Sensor da Bateria
battery = psutil.sensors_battery()

#   Captura Percentual da Bateria
percent = str(battery.percent)

#   Mostra o resultado
print(f'No momento vc tem {percent}%,de bateria')
