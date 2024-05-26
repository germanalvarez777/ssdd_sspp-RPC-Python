import Pyro5.api
import socket

@Pyro5.api.expose               # Decorador que expone la clase para que puedan ser llamados remotamente.
class Paridad(object):          # Clase conformada por un metodo que define el servicio remoto
    def es_par(self, numero):
        if numero % 2 == 0:
            return f"El número {numero} es par."
        else:
            return f"El número {numero} es impar."

def correr_servicio():
    # Obtener la dirección IP de la máquina del servidor
    hostname = socket.gethostname()
    direccion_ip = socket.gethostbyname(hostname)
    
    # Daemon Pyro es el componente del servidor Pyro que escucha las solicitudes RPC.
    # En este caso, escucha en todas las interfaces de red ("0.0.0.0")
    daemon = Pyro5.api.Daemon(host="0.0.0.0")  

    # Registrar la clase Paridad como un objeto Pyro
    # daemon.register expone la clase Paridad en el servidor bajo el nombre "ejercicio1_rpc".
    uri = daemon.register(Paridad, "ejercicio1_rpc")
    print(f"Servidor listo. URI del objeto: {uri}")
    print(f"Dirección IP del servidor: {direccion_ip}")

    # Mantener el servidor corriendo para escuchar las llamadas RPC
    daemon.requestLoop()

if __name__ == "__main__":
    correr_servicio()
