import archivo
import socket

addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print("Servidor listo en puerto 80")

led.on()

while True:
    cl, addr = s.accept()
    print("Cliente:", addr)

    peticion = cl.recv(1024).decode()
    print("Petición:\n", peticion)

   
    if "GET /archivo.json" in peticion:
        with open("archivo.json") as f:
            contenido = f.read()

        cl.send("HTTP/1.1 200 OK\r\n")
        cl.send("Content-Type: application/json\r\n")
        cl.send("Connection: close\r\n\r\n")   
        cl.send(contenido)

    else:
        cl.send("HTTP/1.1 404 Not Found\r\n")
        cl.send("Content-Type: text/plain\r\n")
        cl.send("Connection: close\r\n\r\n")
        cl.send("Archivo no encontrado")

    cl.close()
    led.off()
