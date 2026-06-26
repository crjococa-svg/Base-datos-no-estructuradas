import os
import json
from dotenv import load_dotenv
from pymongo import MongoClient, errors

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# CONEXIÓN E INICIALIZACIÓN DE DATOS 

def inicializar_base_de_datos():
    """Conecta a MongoDB usando variables de entorno, crea la BD prueba3 y pobla las colecciones."""
    try:
        # Obtener la URI desde el entorno de manera segura
        mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
        
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=2000)
        db = client["prueba3"]
        
        # Listas json entregadas para la evaluación
        eventos_data = [
          {
            "codigo": "EVT-2025-001", "nombre": "Evento 1 - Datos", "fecha": "2025-12-25T20:00:00Z",
            "lugar": "Auditorio B", "categoria": "charla",
            "invitados": [
              {"rut": "11.118.512-6", "estado": "confirmado", "checkin": False},
              {"rut": "11.098.760-0", "estado": "confirmado", "checkin": False},
              {"rut": "11.079.008-4", "estado": "confirmado", "checkin": False},
              {"rut": "11.009.876-3", "estado": "confirmado", "checkin": False},
              {"rut": "11.059.256-8", "estado": "confirmado", "checkin": False},
              {"rut": "11.029.628-9", "estado": "pendiente", "checkin": False},
              {"rut": "11.138.264-2", "estado": "confirmado", "checkin": False},
              {"rut": "11.148.140-5", "estado": "confirmado", "checkin": False},
              {"rut": "11.197.520-0", "estado": "confirmado", "checkin": False},
              {"rut": "11.187.644-7", "estado": "confirmado", "checkin": False},
              {"rut": "11.019.752-6", "estado": "confirmado", "checkin": False},
              {"rut": "11.246.900-5", "estado": "confirmado", "checkin": False},
              {"rut": "11.177.768-4", "estado": "pendiente", "checkin": False},
              {"rut": "11.207.396-3", "estado": "pendiente", "checkin": False},
              {"rut": "11.237.024-2", "estado": "rechazado", "checkin": False},
              {"rut": "11.217.272-6", "estado": "pendiente", "checkin": False},
              {"rut": "11.227.148-9", "estado": "pendiente", "checkin": False},
              {"rut": "11.128.388-9", "estado": "pendiente", "checkin": False}
            ]
          },
          {
            "codigo": "EVT-2025-002", "nombre": "Evento 2 - Seguridad", "fecha": "2025-12-27T20:00:00Z",
            "lugar": "Auditorio A", "categoria": "charla",
            "invitados": [
              {"rut": "11.158.016-8", "estado": "pendiente", "checkin": False},
              {"rut": "11.187.644-7", "estado": "pendiente", "checkin": False},
              {"rut": "11.059.256-8", "estado": "confirmado", "checkin": False},
              {"rut": "11.088.884-7", "estado": "rechazado", "checkin": False},
              {"rut": "11.098.760-0", "estado": "rechazado", "checkin": False},
              {"rut": "11.009.876-3", "estado": "pendiente", "checkin": False},
              {"rut": "11.049.380-5", "estado": "pendiente", "checkin": False},
              {"rut": "11.138.264-2", "estado": "confirmado", "checkin": False},
              {"rut": "11.118.512-6", "estado": "confirmado", "checkin": False},
              {"rut": "11.108.636-3", "estado": "confirmado", "checkin": False},
              {"rut": "11.029.628-9", "estado": "confirmado", "checkin": False},
              {"rut": "11.167.892-1", "estado": "confirmado", "checkin": False},
              {"rut": "11.217.272-6", "estado": "rechazado", "checkin": False},
              {"rut": "11.207.396-3", "estado": "confirmado", "checkin": False}
            ]
          },
          {
            "codigo": "EVT-2025-003", "nombre": "Evento 3 - MongoDB", "fecha": "2025-12-27T20:00:00Z",
            "lugar": "Auditorio B", "categoria": "workshop",
            "invitados": [
              {"rut": "11.039.504-2", "estado": "confirmado", "checkin": False},
              {"rut": "11.049.380-5", "estado": "confirmado", "checkin": False},
              {"rut": "11.237.024-2", "estado": "confirmado", "checkin": False},
              {"rut": "11.197.520-0", "estado": "confirmado", "checkin": False},
              {"rut": "11.128.388-9", "estado": "confirmado", "checkin": False},
              {"rut": "11.069.132-1", "estado": "confirmado", "checkin": False},
              {"rut": "11.177.768-4", "estado": "confirmado", "checkin": False},
              {"rut": "11.029.628-9", "estado": "confirmado", "checkin": False},
              {"rut": "11.019.752-6", "estado": "confirmado", "checkin": False},
              {"rut": "11.009.876-3", "estado": "confirmado", "checkin": False},
              {"rut": "11.207.396-3", "estado": "confirmado", "checkin": False},
              {"rut": "11.108.636-3", "estado": "confirmado", "checkin": False},
              {"rut": "11.187.644-7", "estado": "confirmado", "checkin": False},
              {"rut": "11.098.760-0", "estado": "confirmado", "checkin": False},
              {"rut": "11.158.016-8", "estado": "confirmado", "checkin": False},
              {"rut": "11.246.900-5", "estado": "confirmado", "checkin": False},
              {"rut": "11.138.264-2", "estado": "confirmado", "checkin": False},
              {"rut": "11.217.272-6", "estado": "pendiente", "checkin": False},
              {"rut": "11.227.148-9", "estado": "pendiente", "checkin": False},
              {"rut": "11.079.008-4", "estado": "pendiente", "checkin": False},
              {"rut": "11.059.256-8", "estado": "pendiente", "checkin": False},
              {"rut": "11.118.512-6", "estado": "pendiente", "checkin": False}
            ]
          },
          {
            "codigo": "EVT-2025-004", "nombre": "Evento 4 - DevOps", "fecha": "2025-12-25T19:00:00Z",
            "lugar": "Auditorio B", "categoria": "meetup",
            "invitados": [
              {"rut": "11.079.008-4", "estado": "confirmado", "checkin": False},
              {"rut": "11.128.388-9", "estado": "confirmado", "checkin": False},
              {"rut": "11.246.900-5", "estado": "pendiente", "checkin": False},
              {"rut": "11.069.132-1", "estado": "confirmado", "checkin": False},
              {"rut": "11.167.892-1", "estado": "pendiente", "checkin": False},
              {"rut": "11.158.016-8", "estado": "pendiente", "checkin": False},
              {"rut": "11.118.512-6", "estado": "confirmado", "checkin": False},
              {"rut": "11.009.876-3", "estado": "rechazado", "checkin": False},
              {"rut": "11.177.768-4", "estado": "confirmado", "checkin": False},
              {"rut": "11.088.884-7", "estado": "confirmado", "checkin": False}
            ]
          },
          {
            "codigo": "EVT-2025-005", "nombre": "Evento 5 - MongoDB", "fecha": "2025-12-30T18:00:00Z",
            "lugar": "Auditorio A", "categoria": "charla",
            "invitados": [
              {"rut": "11.197.520-0", "estado": "pendiente", "checkin": False},
              {"rut": "11.246.900-5", "estado": "rechazado", "checkin": False},
              {"rut": "11.009.876-3", "estado": "confirmado", "checkin": False},
              {"rut": "11.158.016-8", "estado": "confirmado", "checkin": False},
              {"rut": "11.207.396-3", "estado": "rechazado", "checkin": False},
              {"rut": "11.118.512-6", "estado": "pendiente", "checkin": False},
              {"rut": "11.029.628-9", "estado": "confirmado", "checkin": False},
              {"rut": "11.039.504-2", "estado": "confirmado", "checkin": False},
              {"rut": "11.128.388-9", "estado": "confirmado", "checkin": False},
              {"rut": "11.069.132-1", "estado": "rechazado", "checkin": False},
              {"rut": "11.079.008-4", "estado": "pendiente", "checkin": False},
              {"rut": "11.187.644-7", "estado": "confirmado", "checkin": False},
              {"rut": "11.217.272-6", "estado": "pendiente", "checkin": False},
              {"rut": "11.108.636-3", "estado": "rechazado", "checkin": False},
              {"rut": "11.059.256-8", "estado": "pendiente", "checkin": False},
              {"rut": "11.019.752-6", "estado": "confirmado", "checkin": False}
            ]
          },
          {
            "codigo": "EVT-2025-006", "nombre": "Evento 6 - MongoDB", "fecha": "2025-12-24T20:00:00Z",
            "lugar": "Auditorio B", "categoria": "charla",
            "invitados": [
              {"rut": "11.237.024-2", "estado": "confirmado", "checkin": False},
              {"rut": "11.207.396-3", "estado": "pendiente", "checkin": False},
              {"rut": "11.039.504-2", "estado": "confirmado", "checkin": False},
              {"rut": "11.167.892-1", "estado": "confirmado", "checkin": False},
              {"rut": "11.049.380-5", "estado": "pendiente", "checkin": False},
              {"rut": "11.138.264-2", "estado": "confirmado", "checkin": False},
              {"rut": "11.069.132-1", "estado": "pendiente", "checkin": False},
              {"rut": "11.187.644-7", "estado": "rechazado", "checkin": False},
              {"rut": "11.009.876-3", "estado": "pendiente", "checkin": False},
              {"rut": "11.088.884-7", "estado": "pendiente", "checkin": False},
              {"rut": "11.227.148-9", "estado": "confirmado", "checkin": False},
              {"rut": "11.246.900-5", "estado": "pendiente", "checkin": False}
            ]
          },
          {
            "codigo": "EVT-2025-007", "nombre": "Evento 7 - Datos", "fecha": "2025-12-29T18:00:00Z",
            "lugar": "Sala 204", "categoria": "charla",
            "invitados": [
              {"rut": "11.217.272-6", "estado": "confirmado", "checkin": False},
              {"rut": "11.009.876-3", "estado": "confirmado", "checkin": False},
              {"rut": "11.108.636-3", "estado": "confirmado", "checkin": False},
              {"rut": "11.019.752-6", "estado": "confirmado", "checkin": False},
              {"rut": "11.148.140-5", "estado": "confirmado", "checkin": False},
              {"rut": "11.079.008-4", "estado": "confirmado", "checkin": False},
              {"rut": "11.177.768-4", "estado": "confirmado", "checkin": False},
              {"rut": "11.158.016-8", "estado": "confirmado", "checkin": False},
              {"rut": "11.128.388-9", "estado": "confirmado", "checkin": False},
              {"rut": "11.118.512-6", "estado": "confirmado", "checkin": False},
              {"rut": "11.049.380-5", "estado": "confirmado", "checkin": False},
              {"rut": "11.227.148-9", "estado": "confirmado", "checkin": False},
              {"rut": "11.207.396-3", "estado": "confirmado", "checkin": False},
              {"rut": "11.197.520-0", "estado": "confirmado", "checkin": False},
              {"rut": "11.088.884-7", "estado": "confirmado", "checkin": False},
              {"rut": "11.138.264-2", "estado": "rechazado", "checkin": False},
              {"rut": "11.237.024-2", "estado": "pendiente", "checkin": False},
              {"rut": "11.059.256-8", "estado": "rechazado", "checkin": False},
              {"rut": "11.069.132-1", "estado": "pendiente", "checkin": False},
              {"rut": "11.039.504-2", "estado": "pendiente", "checkin": False}
            ]
          },
          {
            "codigo": "EVT-2025-008", "nombre": "Evento 8 - Seguridad", "fecha": "2025-12-28T19:00:00Z",
            "lugar": "Auditorio B", "categoria": "workshop",
            "invitados": [
              {"rut": "11.128.388-9", "estado": "pendiente", "checkin": False},
              {"rut": "11.148.140-5", "estado": "rechazado", "checkin": False},
              {"rut": "11.108.636-3", "estado": "confirmado", "checkin": False},
              {"rut": "11.029.628-9", "estado": "pendiente", "checkin": False},
              {"rut": "11.079.008-4", "estado": "pendiente", "checkin": False},
              {"rut": "11.138.264-2", "estado": "confirmado", "checkin": False},
              {"rut": "11.217.272-6", "estado": "rechazado", "checkin": False},
              {"rut": "11.069.132-1", "estado": "rechazado", "checkin": False},
              {"rut": "11.098.760-0", "estado": "confirmado", "checkin": False}
            ]
          }
        ]
        
        invitados_data = [
            {"rut": "11.009.876-3", "nombre": "Camila Herrera", "correo": "camila.herrera@empresa.cl", "empresa": "EmpresaX", "estado": "bloqueado"},
            {"rut": "11.019.752-6", "nombre": "Carla Rojas", "correo": "carla.rojas@empresa.cl", "empresa": "BlueCom", "estado": "activo"},
            {"rut": "11.029.628-9", "nombre": "Luis Fernández", "correo": "luis.fernandez@contratista.cl", "empresa": "DataShield", "estado": "activo"},
            {"rut": "11.039.504-2", "nombre": "Ana Martínez", "correo": "ana.martinez@empresa.cl", "empresa": "Inacap", "estado": "activo"},
            {"rut": "11.049.380-5", "nombre": "Diego López", "correo": "diego.lopez@empresa.cl", "empresa": "EmpresaX", "estado": "activo"},
            {"rut": "11.059.256-8", "nombre": "María González", "correo": "maria.gonzalez@inacap.cl", "empresa": "DataShield", "estado": "bloqueado"},
            {"rut": "11.069.132-1", "nombre": "José Pérez", "correo": "jose.perez@contratista.cl", "empresa": "EmpresaX", "estado": "activo"},
            {"rut": "11.079.008-4", "nombre": "Felipe Castro", "correo": "felipe.castro@contratista.cl", "empresa": "DataShield", "estado": "activo"},
            {"rut": "11.088.884-7", "nombre": "Valentina Soto", "correo": "valentina.soto@empresa.cl", "empresa": "AndesLog", "estado": "activo"},
            {"rut": "11.098.760-0", "nombre": "Ricardo Núñez", "correo": "ricardo.nunez@empresa.cl", "empresa": "AndesLog", "estado": "activo"},
            {"rut": "11.108.636-3", "nombre": "Tomás Vergara", "correo": "tomas.vergara@contratista.cl", "empresa": "Inacap", "estado": "activo"},
            {"rut": "11.118.512-6", "nombre": "Daniela Salinas", "correo": "daniela.salinas@contratista.cl", "empresa": "BlueCom", "estado": "activo"},
            {"rut": "11.128.388-9", "nombre": "Andrés Muñoz", "correo": "andres.munoz@empresa.cl", "empresa": "EmpresaX", "estado": "activo"},
            {"rut": "11.138.264-2", "nombre": "Fernanda Campos", "correo": "fernanda.campos@contratista.cl", "empresa": "CyberLab", "estado": "activo"},
            {"rut": "11.148.140-5", "nombre": "Javier Ortiz", "correo": "javier.ortiz@contratista.cl", "empresa": "NorteDigital", "estado": "activo"},
            {"rut": "11.158.016-8", "nombre": "Paula Rivera", "correo": "paula.rivera@empresa.cl", "empresa": "TechNova", "estado": "activo"},
            {"rut": "11.167.892-1", "nombre": "Cristóbal Sáez", "correo": "cristobal.saez@contratista.cl", "empresa": "AndesLog", "estado": "activo"},
            {"rut": "11.177.768-4", "nombre": "Ignacia Torres", "correo": "ignacia.torres@empresa.cl", "empresa": "NorteDigital", "estado": "activo"},
            {"rut": "11.187.644-7", "nombre": "Matías Castillo", "correo": "matias.castillo@empresa.cl", "empresa": "Inacap", "estado": "activo"},
            {"rut": "11.197.520-0", "nombre": "Rocío Paredes", "correo": "rocio.paredes@empresa.cl", "empresa": "BlueCom", "estado": "bloqueado"},
            {"rut": "11.207.396-3", "nombre": "Sebastián Fuentes", "correo": "sebastian.fuentes@empresa.cl", "empresa": "EmpresaX", "estado": "activo"},
            {"rut": "11.217.272-6", "nombre": "Gabriela Vega", "correo": "gabriela.vega@inacap.cl", "empresa": "BlueCom", "estado": "bloqueado"},
            {"rut": "11.227.148-9", "nombre": "Nicolás Araya", "correo": "nicolas.araya@empresa.cl", "empresa": "NorteDigital", "estado": "activo"},
            {"rut": "11.237.024-2", "nombre": "Catalina Contreras", "correo": "catalina.contreras@contratista.cl", "empresa": "Inacap", "estado": "activo"},
            {"rut": "11.246.900-5", "nombre": "Joaquín Reyes", "correo": "joaquin.reyes@inacap.cl", "empresa": "Inacap", "estado": "activo"}
        ]

        # Limpiar colecciones previas para asegurar datos limpios en cada ejecución
        db["eventos"].drop()
        db["invitados"].drop()
        
        db["eventos"].insert_many(eventos_data)
        db["invitados"].insert_many(invitados_data)
        return db
    except errors.ServerSelectionTimeoutError:
        print("[!] ERROR: No se pudo conectar a MongoDB. Revisa tu archivo .env o el estado del servicio.")
        return None

# RUTINAS DE BÚSQUEDA AVANZADA

def listar_eventos(db):
    """Actividad 1:	Listado de eventos con código, nombre, fecha, lugar y categoría"""
    print("\n========================================================")
    print("      LISTADO DE EVENTOS DISPONIBLES EN SISTEMA")
    print("========================================================")
    
    # Proyección explícita eliminando el _id para cumplir con formatos limpios
    proyeccion = {"codigo": 1, "nombre": 1, "fecha": 1, "lugar": 1, "categoria": 1, "_id": 0}
    eventos = db["eventos"].find({}, proyeccion)
    
    for ev in eventos:
        print(f"Código: {ev['codigo']} | Nombre: {ev['nombre']}")
        print(f"Fecha:  {ev['fecha']} | Lugar: {ev['lugar']}")
        print(f"Categoría: {ev['categoria']}")
        print("-" * 52)

def buscar_invitados_regex(db):
    """Actividad 2: Listado de invitados, aplicando filtros con regex."""
    print("\n========================================================")
    print("       BÚSQUEDA AVANZADA DE INVITADOS (REGEX)")
    print("========================================================")
    print("1. Buscar por concordancia de nombre parcial")
    print("2. Buscar por dominio corporativo de correo (Ej: inacap.cl)")
    opcion = input("Seleccione una opción de búsqueda (1-2): ")
    
    query = {}
    if opcion == "1":
        patron = input("Ingrese el texto o nombre a buscar: ")
        # Opción 'i' para búsqueda no sensible a mayúsculas
        query = {"nombre": {"$regex": patron, "$options": "i"}}
    elif opcion == "2":
        dominio = input("Ingrese el dominio de correo (ej: empresa.cl): ")
        # Asegura la búsqueda al final de la cadena de texto ($)
        query = {"correo": {"$regex": f"@{dominio}$", "$options": "i"}}
    else:
        print("[!] Opción inválida.")
        return

    invitados = db["invitados"].find(query, {"_id": 0})
    cantidad = db["invitados"].count_documents(query)
    
    print(f"\nResultados encontrados: {cantidad}\n")
    for inv in invitados:
        print(f"RUT: {inv['rut']} | Nombre: {inv['nombre']} | Estado: {inv['estado']}")
        print(f"Email: {inv['correo']} | Empresa: {inv['empresa']}")
        print("-" * 56)

def validar_acceso_cruzado(db):
    """Actividad 3	Validación de acceso a eventos con búsqueda cruzada(usar lookup))."""

def top_eventos_confirmados(db):
    """Actividad 4: Top 3 eventos con mayor número de invitados confirmados."""
    print("\n========================================================")
    print("        TOP 3 EVENTOS CON MÁS INVITADOS CONFIRMADOS")
    print("========================================================")
    
    pipeline = [
        {"$unwind": "$invitados"},
        {"$match": {"invitados.estado": "confirmado"}},
        {
            "$group": {
                "_id": {
                    "codigo": "$codigo",
                    "nombre": "$nombre",
                    "lugar": "$lugar"
                },
                "total_confirmados": {"$sum": 1}
            }
        },
        {"$sort": {"total_confirmados": -1}},
        {"$limit": 3}
    ]
    
    resultados = db["eventos"].aggregate(pipeline)
    
    for i, res in enumerate(resultados, 1):
        info = res["_id"]
        print(f"{i}°. {info['nombre']} ({info['codigo']})")
        print(f"    Ubicación: {info['lugar']} | Invitados Confirmados: {res['total_confirmados']}")
        print("-" * 56)

# ----------------------------
# MENÚ INTERACTIVO PRINCIPAL
# ----------------------------
def menu_principal():
    db = inicializar_base_de_datos()
    if db is None:
        return

    while True:
        print("\n========================================================")
        print("          SISTEMA DE GESTIÓN DE EVENTOS E INVITADOS")
        print("========================================================")
        print("1. Mostrar todos los eventos")
        print("2. Buscar invitados mediante expresiones regulares")
        print("3. Validar acceso a evento")
        print("4. Ver Top 3 eventos con más confirmados")
        print("5. Salir")
        print("========================================================")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            listar_eventos(db)
        elif opcion == "2":
            buscar_invitados_regex(db)
        elif opcion == "3":
            validar_acceso_cruzado(db)
        elif opcion == "4":
            top_eventos_confirmados(db)
        elif opcion == "5":
            print("\nCerrando aplicación. Evaluación completada de manera exitosa.")
            break
        else:
            print("[!] Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu_principal() 