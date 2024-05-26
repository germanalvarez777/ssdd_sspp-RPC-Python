import Pyro5.api
import socket

@Pyro5.api.expose               # Decorador que expone la clase remota
class Calculadora(object):         
    def suma(self, op1, op2):
        try: 
            if type(op1) == int and type(op2) == int:
                return f'Resultado de la suma: {op1 + op2}'
        except TypeError:
            return 'No se puede realizar la suma por tipado de datos invalido.'
    def resta(self, op1, op2):
        try: 
            if type(op1) == int and type(op2) == int:
                return f'Resultado de la resta: {op1 - op2}'
        except TypeError:
            return 'No se puede realizar la resta por tipado de datos invalido.'
    def divide(self, op1, op2):
        try: 
            if type(op1) == int and type(op2) == int:
                return f'Resultado de la division: {op1 / op2}'
        except TypeError:
            return 'No se puede realizar la division por tipado de datos invalido.'
        except ZeroDivisionError:
            return 'No se puede realizar la division por cero'
    def multiplica(self, op1, op2):
        try: 
            if type(op1) == int and type(op2) == int:
                return f'Resultado del producto: {op1 * op2}'
        except TypeError:
            return 'No se puede realizar la multiplicacion por tipado de datos invalido.'

def correr_servicio():
    # Obtener la dirección IP de la máquina del servidor
    hostname = socket.gethostname()
    direccion_ip = socket.gethostbyname(hostname)
    
    # Daemon Pyro es el componente del servidor Pyro que escucha las solicitudes RPC.
    daemon = Pyro5.api.Daemon(host="0.0.0.0")  

    # Registrar la clase Calculadora como un objeto Pyro
    uri = daemon.register(Calculadora, "ejercicio2_rpc")
    print(f"Servidor listo. URI del objeto: {uri}")
    print(f"Dirección IP del servidor: {direccion_ip}")

    # Mantener el servidor corriendo para escuchar las llamadas RPC
    daemon.requestLoop()

if __name__ == "__main__":
    correr_servicio()