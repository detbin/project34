import sqlite3

def main():
    nombredelalumno= input("Introduzca el nombre de la persona a buscar :")
    datos=()
    datos=busqueda(nombredelalumno)
    print(datos)

def busqueda(nombre):
    conn = sqlite3.connect('project34.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM alumnos WHERE nombre='{nombre}'"
    print("Query a ejecutar ",query)
    rows = cursor.execute(query)
    data=rows.fetchone()
    print("data es",type(data))
    cursor.close()
    conn.close()
    return data

def verifica_credenciales(username, password):
    conn = sqlite3.connect('prueba.db')
    cursor = conn.cursor()
    query = f"SELECT id FROM usuarios WHERE username='{username}' AND password='{password}'"
    print("Query a ejecutar ",query)
    rows = cursor.execute(query)
    data=rows.fetchone
    print("data es",type(data))
    cursor.close()
    conn.close()
    if data == None:
        return False
    else:
        return True
def crearusuario(id,usuario,clave):
    conn = sqlite3.connect('prueba.db')
    cursor = conn.cursor()
    query = '''INSERT INTO usuarios (id,username,password) VALUES (?,?,?)'''
    rows = cursor.execute(query,(id,usuario,clave))
    data=rows.fetchone
    print("data es",type(data))
    #envia los cambios a la base de datos
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
