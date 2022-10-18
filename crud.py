from sqlalchemy.orm import sessionmaker
from model import engine, Tevas, Vaikas


session = sessionmaker(bind=engine)()

# CRUD
def create_tevas(vardas, pavarde):
    tevas = Tevas(vardas=vardas, pavarde=pavarde)
    session.add(tevas)
    session.commit()
    return tevas

def read_tevai():
    tevai = session.query(Tevas).all()
    return tevai


def delete_object(object_class, object_id):
    obj = session.query(object_class).get(object_id)
    if obj:
        session.delete(obj)
        session.commit()
        return True
    else:
        print(f"Klaida: {object_class.__name__} su ID:{object_id} neegzistuoja")

def create_vaikas(vardas, pavarde, tevas, mokymo_istaiga=None):
    vaikas = Vaikas(
        vardas=vardas, 
        pavarde=pavarde, 
        tevas=tevas, 
        mokymo_istaiga=mokymo_istaiga
    )
    session.add(vaikas)
    session.commit()
    return vaikas


def update_object(object_class, object_id, **kwargs):
    obj = session.query(object_class).get(object_id)
    if obj and kwargs:
        for column_name, value in kwargs.items():
            if hasattr(obj, column_name):
                setattr(obj, column_name, value)
            else:
                print(f"Klaida: {obj} neturi {column_name} atributo")
        else:
            session.commit()
            return obj
    else:
        print(f"Klaida: {object_class.__name__} su ID:{object_id} neegzistuoja")


def read_vaikai():
    return session.query(Vaikas).all()

# Testuojam
if __name__ == "__main__":
    # ivaikinimo scenarijus
    # vaikas = session.query(Vaikas).filter(Vaikas.vardas.ilike("%Ivaikintas")).first()
    # tevas = session.query(Tevas).filter(Tevas.vardas.ilike("%Niekam")).first()
    # ivaikintas = update_object(Vaikas, vaikas.id, tevas=tevas, vardas="Ivaikintas dar kart")
    # print("Python objektas 'ivaikintas':\n", ivaikintas)
    # print("perkraunam is DB:\n", read_vaikai())

    # - Naujas Vaikas
    # tevas = session.query(Tevas).get(1)
    # naujas_vaikas = create_vaikas(
    #     "Emilija", "Januskeviciute", 
    #     tevas, "Scuola di Staggia Sienese"
    # )
    # delete_object(Vaikas, 2)
    # print(read_tevai())
    print(read_vaikai())
    # - Naujas Tevas
    # naujas_tevas = create_tevas("Niekam", "Tikes")
    # naujas_vaikas = create_vaikas("mazasis", "pavardeeee",mokymo_istaiga="gimnazija", tevas=tevas)
    # print(naujas_tevas.id, naujas_tevas.vardas, naujas_tevas.pavarde)
    # - Atnaujintas Tevas
    # update_tevas(1, vardas="Geras", pavarde="Programuotojas")
    # update_tevas(1, vardas="Neblogas")
    # - Trinamas Tevas
    # print(delete_tevas(1))