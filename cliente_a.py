import Pyro5.api

def main():
    # Se especifica la dirección IP del servidor al correr primero el servidor
    server_ip = "192.168.1.44"

    # Se crea un proxy para el objeto remoto registrado como "ejercicio1_rpc" en la IP y puerto especificados.
    paridad = Pyro5.api.Proxy(f"PYRO:ejercicio1_rpc@{server_ip}:50353")
    
    # Envía un número al servidor
    numero = int(input("Introduce un número: "))
    resultado = paridad.es_par(numero)
    print(resultado)

if __name__ == "__main__":
    main()
