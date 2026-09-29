#!/usr/bin/python
import socket,sys

# Hegner Brandao | Ethical Hacker

print(f"[1] Scanear as portas mais comuns")
print(f"[2] Scanear todas as portas (65535)")
typeScript = int(input())

if typeScript == 1:
    portList = [21,22,23,25,53,67,68,80,110,
                123,137,138,139,143,161,443,
                445,587,993,995,1433,3000,3306,
                3389,5432,8000,8080,27017]

    for port in portList:
                mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if mysocket.connect_ex((sys.argv[1],port)) == 0:
                    print(f"Porta",port," [ABERTA]")
                    mysocket.close()
else:
    for port in range(1,65535):
            mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if mysocket.connect_ex((sys.argv[1],port)) == 0:
                print(f"Porta",port," [ABERTA]")
                mysocket.close()