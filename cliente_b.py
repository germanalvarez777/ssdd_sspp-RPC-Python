import Pyro5.api

def correr_cliente():
    # Se especifica la dirección IP del servidor
    server_ip = "192.168.1.44"

    # Se crea un proxy para el objeto remoto registrado en la IP y puerto especificados.
    calculadora_cliente = Pyro5.api.Proxy(f"PYRO:ejercicio2_rpc@{server_ip}:56410")
    
    # Se envian los numeros y la operacion al servidor
    operacion = int(input("Ingrese la operacion a efectuar (1:Suma,2:Resta,3:Division,4:Producto,Cualquier otro numero:Salir)\n"))
    while (operacion == 1 or operacion == 2 or operacion == 3 or operacion == 4):
        print("===================================================================================================")
        op1 = int(input("Ingrese el operando 1: "))
        op2 = int(input("Ingrese el operando 2: "))
        if operacion == 1:
            resultado = calculadora_cliente.suma(op1,op2)
        elif operacion == 2:
            resultado = calculadora_cliente.resta(op1,op2)
        elif operacion == 3:
            resultado = calculadora_cliente.divide(op1,op2)
        else:
            resultado = calculadora_cliente.multiplica(op1,op2)
        print(resultado)
        print("===================================================================================================")
        operacion = int(input("Ingrese la operacion a efectuar (1:Suma,2:Resta,3:Division,4:Producto,Cualquier otro numero:Salir)\n"))
    else:
        print("Adios Calculadora...")

if __name__ == "__main__":
    correr_cliente()