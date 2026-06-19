import os
from dotenv import load_dotenv

from pymongo import MongoClient

import datetime
import subprocess 

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client: MongoClient = MongoClient(MONGO_URI)

try:
    print("Estableciendo conexión...⏳")
    client.admin.command("ping")
    print("Conexión establecida 😊")
except:
    print("❌ ERROR EN LA CONEXIÓN")
    exit(code=1)

TI3032_U3_EF = client["TI3032_U3_EF"]  # Elijo la base de datos

coleccion_clientes = TI3032_U3_EF["clientes"]  # Seleccion coleccion Clientes
coleccion_pedidos = TI3032_U3_EF["pedidos"]  # Seleccion coleccion Pedidos

def insercion_inicial_coleccion_clientes() -> None:
    respuesta = coleccion_clientes.insert_many(
        [
            {
                "_id": 1,
                "nombre": "Laura Martínez",
                "email": "laura.martinez@gmail.com",
                "fecha_registro": "2026-01-15T10:30:00Z",
                "direccion": "Av. Providencia 1234, Santiago",
                "telefono": "+56 9 8123 4567",
            },
            {
                "_id": 2,
                "nombre": "Carlos Rojas",
                "email": "carlos.rojas@hotmail.com",
                "fecha_registro": "2025-09-22T14:10:00Z",
                "direccion": "Calle Los Aromos 456, Valparaíso",
                "telefono": "+56 9 7234 5678",
            },
            {
                "_id": 3,
                "nombre": "Fernanda Silva",
                "email": "fernanda.silva@gmail.com",
                "fecha_registro": "2024-03-05T09:45:00Z",
                "direccion": "Pasaje Las Rosas 789, Concepción",
                "telefono": "+56 9 6345 6789",
            },
            {
                "_id": 4,
                "nombre": "Javier Torres",
                "email": "javier.torres@outlook.com",
                "fecha_registro": "2026-04-18T16:20:00Z",
                "direccion": "Av. Alemania 321, Temuco",
                "telefono": "+56 9 5456 7890",
            },
            {
                "_id": 5,
                "nombre": "Camila Soto",
                "email": "camila.soto@gmail.com",
                "fecha_registro": "2025-12-02T11:00:00Z",
                "direccion": "Calle San Martín 654, La Serena",
                "telefono": "+56 9 4567 8901",
            },
            {
                "_id": 6,
                "nombre": "Matías Herrera",
                "email": "matias.herrera@yahoo.com",
                "fecha_registro": "2023-07-11T13:25:00Z",
                "direccion": "Av. Brasil 987, Antofagasta",
                "telefono": "+56 9 3678 9012",
            },
            {
                "_id": 7,
                "nombre": "Valentina Fuentes",
                "email": "valentina.fuentes@gmail.com",
                "fecha_registro": "2026-02-28T08:15:00Z",
                "direccion": "Camino El Alba 147, Rancagua",
                "telefono": "+56 9 2789 0123",
            },
            {
                "_id": 8,
                "nombre": "Diego Morales",
                "email": "diego.morales@empresa.cl",
                "fecha_registro": "2022-10-09T17:40:00Z",
                "direccion": "Calle Maipú 258, Talca",
                "telefono": "+56 9 1890 1234",
            },
            {
                "_id": 9,
                "nombre": "Paula Contreras",
                "email": "paula.contreras@gmail.com",
                "fecha_registro": "2025-06-20T12:05:00Z",
                "direccion": "Av. Costanera 369, Puerto Montt",
                "telefono": "+56 9 9001 2345",
            },
            {
                "_id": 10,
                "nombre": "Andrés Vega",
                "email": "andres.vega@icloud.com",
                "fecha_registro": "2024-11-30T15:55:00Z",
                "direccion": "Pasaje Los Pinos 741, Chillán",
                "telefono": "+56 9 8111 2222",
            },
        ]
    )

    print(respuesta)


def insercion_inicial_coleccion_pedidos() -> None:
    respuesta = coleccion_pedidos.insert_many(
        [
            {
                "cliente_id": 1,
                "fecha_pedido": "2026-02-10T10:00:00Z",
                "monto_total": 245.90,
                "productos": [
                    {"producto_id": 101, "cantidad": 1, "precio": 120.00},
                    {"producto_id": 205, "cantidad": 2, "precio": 62.95},
                ],
            },
            {
                "cliente_id": 2,
                "fecha_pedido": "2025-10-01T13:30:00Z",
                "monto_total": 89.50,
                "productos": [{"producto_id": 302, "cantidad": 1, "precio": 89.50}],
            },
            {
                "cliente_id": 3,
                "fecha_pedido": "2023-04-15T09:20:00Z",
                "monto_total": 560.00,
                "productos": [
                    {"producto_id": 101, "cantidad": 2, "precio": 180.00},
                    {"producto_id": 410, "cantidad": 1, "precio": 200.00},
                ],
            },
            {
                "cliente_id": 4,
                "fecha_pedido": "2026-05-03T18:45:00Z",
                "monto_total": 720.35,
                "productos": [
                    {"producto_id": 508, "cantidad": 1, "precio": 450.35},
                    {"producto_id": 207, "cantidad": 3, "precio": 90.00},
                ],
            },
            {
                "cliente_id": 5,
                "fecha_pedido": "2026-01-20T11:10:00Z",
                "monto_total": 135.75,
                "productos": [{"producto_id": 101, "cantidad": 1, "precio": 135.75}],
            },
            {
                "cliente_id": 6,
                "fecha_pedido": "2023-11-22T16:05:00Z",
                "monto_total": 42.99,
                "productos": [{"producto_id": 601, "cantidad": 1, "precio": 42.99}],
            },
            {
                "cliente_id": 7,
                "fecha_pedido": "2026-03-14T12:35:00Z",
                "monto_total": 980.00,
                "productos": [
                    {"producto_id": 305, "cantidad": 2, "precio": 250.00},
                    {"producto_id": 412, "cantidad": 4, "precio": 120.00},
                ],
            },
            {
                "cliente_id": 8,
                "fecha_pedido": "2024-08-19T19:00:00Z",
                "monto_total": 310.40,
                "productos": [{"producto_id": 208, "cantidad": 1, "precio": 310.40}],
            },
            {
                "cliente_id": 9,
                "fecha_pedido": "2025-07-08T15:25:00Z",
                "monto_total": 515.20,
                "productos": [
                    {"producto_id": 101, "cantidad": 1, "precio": 215.20},
                    {"producto_id": 509, "cantidad": 2, "precio": 150.00},
                ],
            },
            {
                "cliente_id": 10,
                "fecha_pedido": "2023-01-30T08:50:00Z",
                "monto_total": 155.00,
                "productos": [{"producto_id": 706, "cantidad": 5, "precio": 31.00}],
            },
            {
                "cliente_id": 1,
                "fecha_pedido": "2023-09-12T14:15:00Z",
                "monto_total": 75.60,
                "productos": [{"producto_id": 333, "cantidad": 2, "precio": 37.80}],
            },
            {
                "cliente_id": 2,
                "fecha_pedido": "2026-04-09T10:40:00Z",
                "monto_total": 640.90,
                "productos": [
                    {"producto_id": 101, "cantidad": 3, "precio": 120.00},
                    {"producto_id": 804, "cantidad": 1, "precio": 280.90},
                ],
            },
            {
                "cliente_id": 5,
                "fecha_pedido": "2025-12-18T17:30:00Z",
                "monto_total": 98.00,
                "productos": [{"producto_id": 212, "cantidad": 2, "precio": 49.00}],
            },
            {
                "cliente_id": 7,
                "fecha_pedido": "2023-06-25T20:10:00Z",
                "monto_total": 430.00,
                "productos": [{"producto_id": 610, "cantidad": 1, "precio": 430.00}],
            },
            {
                "cliente_id": 9,
                "fecha_pedido": "2026-05-28T09:05:00Z",
                "monto_total": 110.30,
                "productos": [{"producto_id": 715, "cantidad": 1, "precio": 110.30}],
            },
        ]
    )
    
    print(respuesta)

def clientes_ultimo_año() -> None:
    # Calcular la fecha de hoy en el año pasado
    fecha_de_hoy = datetime.datetime.now()
    año_pasado = fecha_de_hoy.year - 1
    fecha_a_consultar = datetime.date(
        year=año_pasado,
        month=fecha_de_hoy.month,
        day=fecha_de_hoy.day
    )
    # Consulta desde el año pasado hasta hoy
    query = {"fecha_registro" : { "$gte": f"{fecha_a_consultar}T00:00:00Z" } }
    resultado = coleccion_clientes.aggregate([
        { "$match": query  },
        { "$sort": { "fecha_registro": -1 } }
    ])
    # Mostrar resultado
    for doc in resultado:
        print(doc)

# 2. Encuentra todos los pedidos cuyo monto total sea superior a $100.
def pedidos_monto_mayor_100() -> None:
    query = {"monto_total": {"$gt": 100.00}}
    resultado = coleccion_pedidos.find(query)
    for doc in resultado:
        print(doc)

# 3. Encuentra todos los clientes cuyo email pertenezca al dominio "gmail.com".
def clientes_email_gmail() -> None:
    query = {"email": {"$regex": "@gmail\\.com$", "$options": "i"}}
    resultado = coleccion_clientes.find(query)
    for doc in resultado:
        print(doc)

# 4. Encuentra todos los pedidos realizados en el año 2023.
def pedidos_año_2023() -> None:
    query = {
        "fecha_pedido": {
            "$gte": "2023-01-01T00:00:00Z",
            "$lte": "2023-12-31T23:59:59Z"
        }
    }
    resultado = coleccion_pedidos.find(query)
    for doc in resultado:
        print(doc)

# 5. Encuentra todos los pedidos que contengan un producto con producto_id igual a 101.
def pedidos_producto_101() -> None:
    query = {"productos.producto_id": 101}
    resultado = coleccion_pedidos.find(query)
    for doc in resultado:
        print(doc)

# 6. Clientes con al menos un pedido superior a $500 en el último año.
def clientes_pedidos_complejos_500() -> None:
    fecha_de_hoy = datetime.datetime.now()
    año_pasado = fecha_de_hoy.year - 1
    fecha_a_consultar = f"{año_pasado}-{fecha_de_hoy.month:02d}-{fecha_de_hoy.day:02d}T00:00:00Z"
    
    pipeline = [
        {
            "$lookup": {
                "from": "pedidos",
                "localField": "_id",
                "foreignField": "cliente_id",
                "as": "pedidos_asociados"
            }
        },
        {
            "$match": {
                "pedidos_asociados": {
                    "$elemMatch": {
                        "monto_total": {"$gt": 500.00},
                        "fecha_pedido": {"$gte": fecha_a_consultar}
                    }
                }
            }
        }
    ]
    resultado = coleccion_clientes.aggregate(pipeline)
    for doc in resultado:
        print(doc)

def main():
    # Reiniciar colecciones para pruebas limpias
    coleccion_clientes.drop()
    coleccion_pedidos.drop()

    insercion_inicial_coleccion_clientes()
    insercion_inicial_coleccion_pedidos()

    while True:
        subprocess.run(["cls || clear"], shell=True, check=True)
        print(
            """
            ===================================================================
            |                       PYMONGO ECOMMERCE                         |
            ===================================================================
            1. Clientes registrados en el último año.
            2. Pedidos con monto total superior a $100.
            3. Clientes con email del dominio 'gmail.com'.
            4. Pedidos realizados en el año 2023.
            5. Pedidos con el producto_id igual a 101.
            6. Clientes con pedidos > $500 en el último año (Consulta Compleja).
            0. Salir.
            ===================================================================
            """
        )
        opcion = input("Ingresa tu opción [0-6]: ")

        subprocess.run(["cls || clear"], shell=True, check=True)
        if opcion == "1":
            print("=== CLIENTES REGISTRADOS EL ÚLTIMO AÑO ===")
            clientes_ultimo_año()
        elif opcion == "2":
            print("=== PEDIDOS CON MONTO MAYORES A $100 ===")
            pedidos_monto_mayor_100()
        elif opcion == "3":
            print("=== CLIENTES CON EMAIL GMAIL.COM ===")
            clientes_email_gmail()
        elif opcion == "4":
            print("=== PEDIDOS REALIZADOS EN EL AÑO 2023 ===")
            pedidos_año_2023()
        elif opcion == "5":
            print("=== PEDIDOS CON PRODUCTO ID 101 ===")
            pedidos_producto_101()
        elif opcion == "6":
            print("=== CLIENTES CON PEDIDOS > $500 EN EL ÚLTIMO AÑO ===")
            clientes_pedidos_complejos_500()
        elif opcion == "0":
            input("Adiós. Presiona ENTER para salir...")
            break
        else:
            print("Opción incorrecta.")
        
        input("\nPresiona ENTER para continuar...")
    
    exit()

if __name__ == "__main__":
    main()