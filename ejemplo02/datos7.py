from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_tablas import Establecimiento, Parroquia, Canton

# Los cantones que tiene establecimientos con 0 número de profesores y 210 estudiantes

# Crear el enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def cantones_nEstudiants_nProfesores(num_estudiantes, num_profesores):
    cantones = session.query(Canton).join(Parroquia).join(Establecimiento).filter(
        Establecimiento.numero_estudiantes == num_estudiantes,
        Establecimiento.numero_docentes == num_profesores
    ).all()
    return cantones


num_estudiantes = 210
num_profesores = 0
cantones = cantones_nEstudiants_nProfesores(num_estudiantes, num_profesores)
for canton in cantones:
    print(canton)

session.close()
