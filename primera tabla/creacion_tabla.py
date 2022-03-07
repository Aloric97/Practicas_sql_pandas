import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime, create_engine


engine= create_engine('postgresql://postgres:123456@localhost/proyecto_alkemy')
Base= declarative_base()

class Proyecto(Base):
    __tablename__ = 'proyecto_alkemy'


    id=Column(Integer(), primary_key=True)
    Cod_localidad=Column(Integer(), nullable=False)
    IdProvincia=Column(Integer(), nullable=False)
    IdDepartamento=Column(Integer(), nullable=False)
    Categoria=Column(String(255), nullable=False)
    Provincia=Column(String(255), nullable=False)
    Localidad=Column(String(255), nullable=False)
    Nombre=Column(String(255), nullable=False)
    Domicilio=Column(String(255))
    Codigo_postal=Column(String(255))
    Telefono=Column(String(255))
    Mail=Column(String(255))
    Web=Column(String(255))
    Creado_el=Column(DateTime(), default=datetime.datetime.now())
    
    def __str__(self):
        return self.Direccion

Session=sessionmaker(engine)

session=Session()

if __name__ == "__main__":

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print('creacion exitosa')