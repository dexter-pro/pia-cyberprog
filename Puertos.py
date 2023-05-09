import nmap
import socket

hostname = socket.gethostname();ip_address = socket.gethostbyname(hostname)

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('192.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
 
ip_address = get_local_ip()

def UTP (ports):
    escaner = nmap.PortScanner()
    escaner.scan(ip_address, arguments="-sU -p " + ports)
    for host in escaner.all_hosts():
        print(f"Escaneando host: ", ip_address)
        for port in escaner[host]['udp']:
            print("Puerto : %s\tEstado : %s" % (port, escaner[host]['udp'][port]["state"]))
            
def TCP(ports):
    escaner = nmap.PortScanner()
    escaner.scan(ip_address, arguments="-sS -p " + ports)
    for host in escaner.all_hosts():
        print("Escaneando host: ", ip_address )
        for port in escaner[host]['tcp']:
            print("Puerto : %s\tEstado : %s" % (port, escaner[host]['tcp'][port]["state"]))

def Fast():
    escaner = nmap.PortScanner()
    escaner.scan(ip_address, arguments="-F")
    for host in escaner.all_hosts():
        print("Escaneando host: ", ip_address)
        for Proto in escaner[host].all_protocols():
            print("Escaneando protocolo: %s" % Proto)
            LP = list(escaner[host][Proto].keys())
            LP.sort()
            for port in LP:
                print("Puerto : %s\tEstado : %s" % (port, escaner[host][Proto][port]["state"]))