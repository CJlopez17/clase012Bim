import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Provincia, Canton

# Importar cadena de conexión desde un archivo de configuración
from configuracion import cadena_base_datos

# Crear el enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Ruta del archivo CSV
archivo_csv = 'data/Listado-Instituciones-Educativas-02.csv'

# Lista para almacenar los datos del CSV
datos_csv = []

# Leer datos del archivo CSV y almacenar en la lista
with open(archivo_csv, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        provincia_nombre = row['Provincia']
        canton_nombre = row['Cantón']
        codigo_division = int(row['Código División Política Administrativa  Cantón'])
        datos_csv.append((provincia_nombre, canton_nombre, codigo_division))  # Agregar a la lista

# Convertir la lista a un conjunto para eliminar duplicados
miscantones = set(datos_csv)

# Insertar datos únicos en la base de datos y asociar con la provincia correspondiente
for provincia_nombre, canton_nombre, codigo_division in miscantones:
    provincia = session.query(Provincia).filter_by(nombre=provincia_nombre).first()
    micanton = Canton(codigo_division=codigo_division, nombre=canton_nombre, provincia=provincia)
    session.add(micanton)

# Guardar los cambios en la base de datos
session.commit()
