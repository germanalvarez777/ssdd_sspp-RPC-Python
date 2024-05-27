import Pyro5.api
import os

def correr_cliente():
    server_ip = "192.168.1.44"

    # Se crea un proxy para el objeto remoto registrado en la IP y puerto especificados.
    calculadora_cliente = Pyro5.api.Proxy(f"PYRO:ejercicio2_rpc@{server_ip}:50291")
    
    # Identificador único del cliente
    id_cliente = input("Ingrese su id unico como cliente: ")
    print(f"Bienvenido cliente {id_cliente}!")

    # Intentar obtener cualquier resultado pendiente primero
    resultado_pendiente = calculadora_cliente.get_resultado_pendiente(id_cliente)
    if resultado_pendiente:
        print(f"Resultado pendiente para {id_cliente}: {resultado_pendiente}")

    # Se envian los numeros y la operacion al servidor
    operacion = int(input("Ingrese la operacion a efectuar (1:Suma,2:Resta,3:Division,4:Producto,Cualquier otro numero:Salir)\n"))
    while (operacion == 1 or operacion == 2 or operacion == 3 or operacion == 4):
        print("===================================================================================================")
        op1 = int(input("Ingrese el operando 1: "))
        op2 = int(input("Ingrese el operando 2: "))
        if operacion == 1:
            resultado = calculadora_cliente.suma(id_cliente,op1,op2)
        elif operacion == 2:
            resultado = calculadora_cliente.resta(id_cliente,op1,op2)
        elif operacion == 3:
            resultado = calculadora_cliente.divide(id_cliente,op1,op2)
        else:
            resultado = calculadora_cliente.multiplica(id_cliente,op1,op2)

        # Simula la desconexión del cliente antes de recibir la respuesta
        opcion = input("Desea simular la desconexion con el servidor?(s/n): ")
        if opcion.lower() == 's' or opcion.lower() == 'si':
            print(f"Se produce la caida del cliente {id_cliente} de manera abrupta!")
            os._exit(1)
        
        # En este punto, no hay resultado pendiente a resguardar, por ende se descarta el guardado pendiente
        resultado_no_pendiente = calculadora_cliente.get_resultado_pendiente(id_cliente)
        print(resultado)
        print("===================================================================================================")
        operacion = int(input("Ingrese la operacion a efectuar (1:Suma,2:Resta,3:Division,4:Producto,Cualquier otro numero:Salir)\n"))
    else:
        print("Adios Calculadora...")

if __name__ == "__main__":
    correr_cliente()