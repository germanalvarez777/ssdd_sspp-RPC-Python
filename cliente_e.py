import Pyro5.api
import unicodedata

def correr_cliente():
    server_ip = "192.168.1.44"
    # Se crea un proxy para el objeto remoto registrado en la IP y puerto especificados.
    Materias = Pyro5.api.Proxy(f"PYRO:ejercicio4_rpc@{server_ip}:57175")
    dia = input("Ingrese un dia para averiguar sus materias: ").lower()
    
    # Descompone el texto quitando los caracteres con acentos
    texto_normalizado = unicodedata.normalize('NFKD', dia)
    # Filtra solo los caracteres base (sin acentos)
    dia = ''.join([c for c in texto_normalizado if not unicodedata.combining(c)])

    resultado = Materias.get_materias(dia)
    print(resultado)
if __name__ == "__main__":
    correr_cliente()