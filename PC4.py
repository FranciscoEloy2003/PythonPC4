#PROBLEMA 01:
import requests
from decimal import Decimal

def get_btc_price(api_key):
    url = "https://rest.coinapi.io/v1/exchangerate/BTC"
    headers = {"X-CoinAPI-Key": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return Decimal(data["rates"][0]["rate"])
    else:
        raise Exception("Error fetching BTC price")

def get_sunat_exchange_rate(date):
    url = f"https://apis.net.pe/api-tipo-cambio/tipo-cambio/dolar/fecha/{date}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return Decimal(data["compra"])
    else:
        raise Exception("Error fetching SUNAT exchange rate")

def get_cost_of_n_bitcoins(n, api_key, date):
    btc_price = get_btc_price(api_key)
    sunat_exchange_rate = get_sunat_exchange_rate(date)
    cost = n * btc_price * sunat_exchange_rate
    return cost.quantize(Decimal("0.0000"))

if __name__ == "__main__":
    try:
        api_key = "YOUR-API-KEY" # Replace with your actual API key
        n = float(input("Enter the number of Bitcoins: "))
        date = input("Enter the date (yyyy-mm-dd): ")
        cost = get_cost_of_n_bitcoins(n, api_key, date)
        print(f"The cost of {n} Bitcoins in USD is {cost:.4f}")
    except Exception as e:
        print(f"An error occurred: {e}")


#PROBLEMA 02:
import random
from pyfiglet import Figlet

# Get the font name from user input or select a random font
font_name = input("Enter a font name or leave blank for a random font: ").strip()
if not font_name:
    font_name = random.choice(Figlet().getFonts())

# Get the text from user input
text = input("Enter the text to convert: ").strip()

# Set the font and render the text
figlet = Figlet(font=font_name)
text_art = figlet.renderText(text)

# Print the text art
print(text_art)


#PROBLEMA 03:
import zipfile
import os

def almacenar_imagen_como_zip(ruta_imagen, nombre_zip):
    try:
        with zipfile.ZipFile(nombre_zip, 'w') as archivo_zip:
            archivo_zip.write(ruta_imagen, os.path.basename(ruta_imagen))
        print(f"La imagen '{ruta_imagen}' ha sido almacenada como '{nombre_zip}' correctamente.")
    except FileNotFoundError:
        print("La imagen no se encontró en la ruta especificada.")
    except Exception as e:
        print(f"Ocurrió un error al almacenar la imagen como archivo ZIP: {e}")

if __name__ == "__main__":
    ruta_imagen = input("Ingrese la ruta de la imagen: ")
    nombre_zip = "imagen.zip"  # Nombre del archivo ZIP que deseas crear
    almacenar_imagen_como_zip(ruta_imagen, nombre_zip)



#PROBLEMA 04:
import requests

# Fetch the current price of Bitcoin from CoinDesk API
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
price_data = response.json()
price = price_data['bpi']['USD']['rate_float']

# Format the price data as a string
price_str = f'Bitcoin Price: ${price:.2f}\n'

# Save the price data to a text file
with open('bitcoin_price.txt', 'w') as f:
    f.write(price_str)

print('Price of Bitcoin saved to bitcoin_price.txt')
#bitcoin_price.txt ---> precio actual del bitcoin



#PROBLEMA 05: Escriba un programa que realice las siguientes tareas
def crear_tabla(n):
    with open(f"tabla-{n}.txt", "w") as f:
        for i in range(1, 11):
            f.write(f"{n} x {i} = {n * i}\n")

def mostrar_tabla(n):
    try:
        with open(f"tabla-{n}.txt", "r") as f:
            print(f"Tabla de multiplicar del {n}:")
            print(f.read())
    except FileNotFoundError:
        print(f"No se encontró el archivo tabla-{n}.txt")

def mostrar_linea(n, m):
    try:
        with open(f"tabla-{n}.txt", "r") as f:
            print(f"Línea {m} de la tabla de multiplicar del {n}:")
            print(f.readlines()[m - 1])
    except FileNotFoundError:
        print(f"No se encontró el archivo tabla-{n}.txt")

def main():
    while True:
        print("\nMenú:")
        print("1. Crear tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de la tabla de multiplicar")
        print("4. Salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                crear_tabla(n)
            else:
                print("El número debe estar entre 1 y 10.")
        elif opcion == 2:
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                mostrar_tabla(n)
            else:
                print("El número debe estar entre 1 y 10.")
        elif opcion == 3:
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            m = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= n <= 10 and 1 <= m <= 10:
                mostrar_linea(n, m)
            else:
                print("Los números deben estar entre 1 y 10.")
        elif opcion == 4:
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()

#PROBLEMA 06:
def contar_lineas_codigo(ruta):
    try:
        if not ruta.endswith('.py'):
            print("El archivo no es un archivo .py válido.")
            return

        with open(ruta, 'r') as archivo:
            lineas_codigo = 0
            for linea in archivo.readlines():
                linea = linea.strip()
                if linea and not linea.startswith('#'):
                    lineas_codigo += 1

        print(f"El archivo '{ruta}' tiene {lineas_codigo} líneas de código.")

    except FileNotFoundError:
        print("El archivo no se encontró o la ruta es inválida.")


if __name__ == "__main__":
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    contar_lineas_codigo(ruta_archivo)



#PROBLEMA 07:   
import sqlite3

# Connect to the database or create it if it doesn't exist
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

# Create the table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sunat_info (
        id INTEGER PRIMARY KEY,
        country TEXT NOT NULL,
        dollar_price REAL NOT NULL
    )
''')

# Insert the data
data = [
    ('Mexico', 16.95),
    ('Honduras', 24.6756),
    ('Guatemala', 7.8234),
    ('Costa Rica', 519.59),
    ('El Salvador', 8.7507),
    ('Nicaragua', 36.6027),
    ('Colombia', 3873.59),
    ('Venezuela', 35.8407),
    ('Republic Dominicana', 57.277),
    ('Argentina', 320.39),
]

cursor.executemany('''
    INSERT INTO sunat_info (country, dollar_price)
    VALUES (?, ?)
''', data)

# Commit the changes and close the connection
conn.commit()
conn.close()

# Verify the data
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM sunat_info')
rows = cursor.fetchall()

print('ID - Country - Dollar Price')
print('-- --------- --------------')
for row in rows:
    print(f'{row[0]} - {row[1]} - {row[2]}')

conn.close()

#PROBLEMA 08: 
import sqlite3

# Connect to the database or create it if it doesn't exist
conn = sqlite3.connect('crypto.db')
cursor = conn.cursor()

# Create the table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS bitcoin (
        id INTEGER PRIMARY KEY,
        date TEXT NOT NULL,
        price_usd REAL NOT NULL,
        price_pen REAL NOT NULL,
        price_eur REAL NOT NULL
    )
''')

# Insert the data
date = '2023-04-14'
price_usd = 32039.00
price_pen = 120156.00
price_eur = 29454.00

cursor.execute('''
    INSERT INTO bitcoin (date, price_usd, price_pen, price_eur)
    VALUES (?, ?, ?, ?)
''', (date, price_usd, price_pen, price_eur))

# Commit the changes and close the connection
conn.commit()
conn.close()

# Query the database to calculate the price of buying 10 bitcoins in PEN and EUR
conn = sqlite3.connect('crypto.db')
cursor = conn.cursor()

cursor.execute('SELECT price_pen, price_eur FROM bitcoin WHERE date = ?', (date,))
row = cursor.fetchone()

price_pen_10 = row[0] * 10
price_eur_10 = row[1] * 10

print(f'Price of buying 10 bitcoins in PEN: {price_pen_10:.2f}')
print(f'Price of buying 10 bitcoins in EUR: {price_eur_10:.2f}')

conn.close()