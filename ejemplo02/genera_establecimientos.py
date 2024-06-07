import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Establecimiento, Parroquia, Base

# Importar cadena de conexión desde un archivo de configuración
from configuracion import cadena_base_datos

# Crear el enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Ruta del archivo CSV
archivo_csv = 'data/Listado-Instituciones-Educativas-02.csv'

# Leer datos del archivo CSV y almacenar en la base de datos
with open(archivo_csv, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        codigo_amie = row['Código AMIE']
        nombre = row['Nombre de la Institución Educativa']
        zona_administrativa = row['Zona Administrativa']
        denominacion_distrito = row['Denominación del Distrito']
        codigo_distrito = row['Código de Distrito']
        codigo_circuito = row['Código de Circuito Educativo']
        sostenimiento = row['Sostenimiento']
        regimen_escolar = row['Régimen Escolar']
        jurisdiccion = row['Jurisdicción']
        tipo_educacion = row['Tipo de Educación']
        modalidad = row['Modalidad']
        jornada = row['Jornada']
        nivel = row['Nivel']
        etnia = row['Etnia']
        acceso = row['Acceso (terrestre/ aéreo/fluvial)']
        numero_estudiantes = int(row['Número de estudiantes'])
        numero_docentes = int(row['Número de docentes'])
        estado = row['Estado']
        parroquia_nombre = row['Parroquia']

        parroquia = session.query(Parroquia).filter_by(nombre=parroquia_nombre).first()

        establecimiento = Establecimiento(
            codigo_amie=codigo_amie, 
            nombre=nombre, 
            zona_administrativa=zona_administrativa,
            denominacion_distrito=denominacion_distrito,
            codigo_distrito=codigo_distrito,
            codigo_circuito=codigo_circuito,
            sostenimiento=sostenimiento,
            regimen_escolar=regimen_escolar, 
            jurisdiccion=jurisdiccion,
            tipo_educacion=tipo_educacion, 
            modalidad=modalidad, 
            jornada=jornada,
            nivel=nivel, 
            etnia=etnia, 
            acceso=acceso,
            numero_estudiantes=numero_estudiantes, 
            numero_docentes=numero_docentes,
            estado=estado, 
            parroquia=parroquia
        )
        session.add(establecimiento)

# Guardar los cambios en la base de datos
session.commit()
