from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_tablas import Establecimiento, Parroquia, Canton

# Los cantones que tiene establecimientos como número de estudiantes tales como: 1, 74, 100

# Crear el enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def cantones_estudiantes(num_estudiantes):
    cantones = session.query(Canton).join(Parroquia).join(Establecimiento).filter(
        Establecimiento.numero_estudiantes.in_(num_estudiantes)
    ).all()
    return cantones

# Ejemplo de uso
num_estudiantes = [1, 74, 100]
cantones = cantones_estudiantes(num_estudiantes)
for canton in cantones:
    print(canton)

session.close()
