from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_tablas import Canton

# Todos los establecimientos del cantón de Guayaquil.

# Crear el enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

cantones = session.query(Canton).all()

for s in cantones:
   print("%s: %d estudiantes" % (s.nombre, s.numero_estudiantes(session)))

#for canton in cantones:
#    print(f"Cantón: {canton.canton}, Número de estudiantes: {canton.numero_estudiantes(session)}")

session.close()
