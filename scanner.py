import argparse;import os;import hashlib;import subprocess;import Puertos;import logging;from datetime import datetime

parser = argparse.ArgumentParser(prog="python scanner.py", description="Scanner de procesos, puertos y archivos descargados", epilog="El programa puede tardar algunos minutos dependiento del rendimiento de tu computadora")
parser.add_argument("--mode", dest="mode", help="Modo de escaneo. Ej: p = analizar puertos, t = analizar procesos")
parser.add_argument('--sendemail', dest="email", help="Ingresa el correo al que se enviara reporte sobre el escaneo")
parser.add_argument("--downloads", help="Analizar descargas", action='store_true')
parser.add_argument("--ports", help="Puerto o rango de puertos. Ej: 22,80 | 20-80 | 22")
parser.add_argument("--scantype", help="Seleccionar el tipo de escaneo TCP/UDP/Rapido")

params = parser.parse_args()

def main():
    if params.downloads == True:
        hash_downloads()
    if params.mode != None and "t" in params.mode:
        process_analysis()
    if params.mode != None and "p" in params.mode:
        ports_analysis()
    if params.email != None:
        send_email()

def hash_downloads():
    try:
        downloads_folder = os.path.expanduser("~/Downloads")  # Ruta de la carpeta de descargas
        for filename in os.listdir(downloads_folder):
            filepath = os.path.join(downloads_folder, filename)
            if os.path.isfile(filepath):
                with open(filepath, "rb") as f:
                    print(f'Analizando: {filename}')
                    bytes = f.read()  # Lee el archivo en modo binario
                    hash = hashlib.sha256(bytes).hexdigest()  # Calcula el hash SHA-256
                    print(f"{filename}: {hash}")
    except Exception as Argument:
        f = open("logs.txt", "a")
        f.write(str(datetime.now().strftime("%Y/%m/%d %H:%M:%S")) + " Error: " + str(Argument) + "\n")
        f.close()

def process_analysis():
    # Obetener la lista de ID de los procesos corriendo
    id_processes = subprocess.run(["powershell", "Get-Process | Select-Object Id, name"], capture_output=True, text=True)
    processes_list = []
        
    for j in range((len(id_processes.stdout.split()))//2):
        processes_list.append([])
        processes_list[j].append(id_processes.stdout.split()[j*2]) #
        processes_list[j].append(id_processes.stdout.split()[j*2+1]) # id_processes.stdout.split()[4]
    print(processes_list)
    
    for i in range(2, (len(id_processes.stdout.split()))//2):
        print(f"La ruta del proceso {processes_list[i][1]} con id: {processes_list[i][0]} es: {subprocess.run(['powershell', f'(Get-Process -Id {processes_list[i][0]}).path'], capture_output=True, text=True).stdout}" if subprocess.run(['powershell', f'(Get-Process -Id {processes_list[i][0]}).path'], capture_output=True, text=True).stdout != "" else f"La ruta del proceso {processes_list[i][1]} con id: {processes_list[i][0]} no fue encontrada")
        if processes_list[i][1] == "svchost" and "system32" in subprocess.run(['powershell', f'(Get-Process -Id {processes_list[i][0]}).path'], capture_output=True, text=True).stdout:
            print(f"Archivo localizado")

def ports_analysis():
    print(params.ports)
    if params.scantype == "tcp":
        if params.ports == None:
            params.ports = "22,25,80,443,143,110,3389,8080"
        print(f"Ejecutando escaneo TCP sobre los puertos: {params.ports}")
        Puertos.TCP(params.ports)
    elif params.scantype == "utp":
        if params.ports == None:
            params.ports = "59,67,68,123,161,389,443,514"
        print(f"Ejecutando escaneo UDP sobre los puertos: {params.ports}")
        Puertos.UDP(params.ports)
    else:
        Puertos.Fast()
        
def send_email():
    pass

if __name__ == '__main__':
    main()
    