from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import sessionmaker

# Importar cadena de conexión desde un archivo de configuración
from configuracion import cadena_base_datos

# Crear el enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)

Base = declarative_base()

class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key= True)
    codigo_division = Column(Integer, nullable= False)
    nombre = Column(String(100))

    cantones = relationship("Canton", back_populates="provincia")

    def __repr__(self):
        return "Provincia: %s | Código División Política Administrativa Provincia: %d" % (
            self.nombre,
            self.codigo_division
        )

class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    codigo_division = Column(Integer, nullable=False)
    nombre = Column(String(100))
    provincia_id = Column(Integer, ForeignKey('provincia.id'))

    provincia = relationship("Provincia", back_populates="cantones")
    parroquias = relationship("Parroquia", back_populates="canton")

    def __repr__(self):
        return "Canton: %s | Código División Política Administrativa Cantón: %d" % (
            self.nombre,
            self.codigo_division
        )
    def numero_estudiantes(self):
        establecimientos = session.query(Establecimiento).join(Parroquia).filter(Parroquia.canton == self).all()
        suma = 0
        for establecimiento in establecimientos:
            suma += establecimiento.numero_estudiantes
        return suma
   

class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key= True)
    codigo_division = Column(Integer, nullable= False)
    nombre = Column(String(100))
    canton_id = Column(Integer, ForeignKey('canton.id'))

    canton = relationship("Canton", back_populates="parroquias")
    establecimientos = relationship("Establecimiento", back_populates="parroquia")

    def __repr__(self):
        return "Parroquia: %s | Código División Política Administrativa Parroquia: %d" % (
            self.nombre,
            self.codigo_division
        )

class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    
    id = Column(Integer, primary_key=True)
    codigo_amie = Column(String(100))
    nombre = Column(String(100))
    zona_administrativa = Column(String(100))
    denominacion_distrito = Column(String(100))
    codigo_distrito = Column(String(100))
    codigo_circuito = Column(String(100))
    sostenimiento = Column(String(100))
    regimen_escolar = Column(String(100))
    jurisdiccion = Column(String(100))
    tipo_educacion = Column(String(100))
    modalidad = Column(String(100))
    jornada = Column(String(100))
    nivel = Column(String(100))
    etnia = Column(String(100))
    acceso = Column(String(100))
    numero_estudiantes = Column(Integer)
    numero_docentes = Column(Integer)
    estado = Column(String(100))
    parroquia_id = Column(Integer, ForeignKey('parroquia.id'))
    
    parroquia = relationship("Parroquia", back_populates="establecimientos")

    def __repr__(self):
        return "Establecimiento: %s | Código AMIE: %s | Zona Administrativa: %s | Denominación Distrito: %s | Código Distrito: %s | Código Circuito: %s | Sostenimiento: %s | Régimen Escolar: %s | Jurisdicción: %s | Tipo de Educación: %s | Modalidad: %s | Jornada: %s | Nivel: %s | Etnia: %s | Acceso: %s | Número de Estudiantes: %d | Número de Docentes: %d | Estado: %s" % (
            self.nombre,
            self.codigo_amie,
            self.zona_administrativa,
            self.denominacion_distrito,
            self.codigo_distrito,
            self.codigo_circuito,
            self.sostenimiento,
            self.regimen_escolar,
            self.jurisdiccion,
            self.tipo_educacion,
            self.modalidad,
            self.jornada,
            self.nivel,
            self.etnia,
            self.acceso,
            self.numero_estudiantes,
            self.numero_docentes,
            self.estado
        )

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)
