import Pyro5.api
from concurrent.futures import ThreadPoolExecutor, TimeoutError

def call_remote_method(server_ip, numero):
    try:
        paridad = Pyro5.api.Proxy(f"PYRO:ejercicio1_rpc@{server_ip}:56563")
        return paridad.es_par(numero)
    except Exception as e:
        return e

def correr_cliente():
    # Se especifica la dirección IP del servidor
    server_ip = "192.168.1.44"

    # Se crea un proxy para el objeto remoto registrado como "ejercicio1_rpc" en la IP y puerto especificados.

    numero = int(input("Introduce un número: "))
    with ThreadPoolExecutor() as executor:
        future = executor.submit(call_remote_method, server_ip, numero)
        
        try:
            resultado = future.result(timeout=5)  # Espera hasta 5 segundos
            if isinstance(resultado, Exception):
                print(f"Error Inesperado: {resultado}")
            else:
                print(resultado)
        except TimeoutError:
            print("La llamada al servidor ha superado el tiempo de espera,retransmita el procedimiento.")

if __name__ == "__main__":
    correr_cliente()