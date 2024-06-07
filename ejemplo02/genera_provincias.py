import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Provincia, Base

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
        codigo_division = int(row['Código División Política Administrativa Provincia'])
        provincia = row['Provincia']
        datos_csv.append((codigo_division, provincia))  # Agregar a la lista

# Convertir la lista a un conjunto para eliminar duplicados
misprovincias = set(datos_csv)

# Insertar datos únicos en la base de datos
for codigo, provincia in misprovincias:
    laprovincia = Provincia(codigo_division=codigo, nombre=provincia)
    session.add(laprovincia)

# Guardar los cambios en la base de datos
session.commit()
