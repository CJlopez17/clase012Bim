from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_tablas import Establecimiento, Parroquia

# Los establecimientos ordenados por nombre de parroquia que tengan más 
# de 40 profesores y la cadena "Educación regular" en tipo de educación.

# Crear el enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def establecimientos_por_profesores():
    establecimientos = session.query(Establecimiento).join(Parroquia).filter(
        Establecimiento.numero_docentes > 40,
        Establecimiento.tipo_educacion.like("%Educación regular%")
    ).order_by(Parroquia.nombre).all()
    return establecimientos

establecimientos = establecimientos_por_profesores()
for establecimiento in establecimientos:
    print(f"Parroquia: {establecimiento.parroquia.nombre} | Establecimiento: {establecimiento.nombre} | Profesores: {establecimiento.numero_docentes}")

session.close()
