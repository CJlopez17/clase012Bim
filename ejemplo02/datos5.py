from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_tablas import Establecimiento, Parroquia

# Las parroquias que tienen establecimientos únicamente en la jornada "Matutina, Vesperina y Nocturna"

# Crear el enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def parroquia_jornadas(jornadas):
    parroquias = session.query(Parroquia).join(Establecimiento).filter(
        Establecimiento.jornada.in_(jornadas)
    ).all()
    return parroquias

# Ejemplo de uso
jornadas = ["Matutina", "Vespertina", "Nocturna"]
parroquias = parroquia_jornadas(jornadas)
for parroquia in parroquias:
    print(parroquia)

session.close()
