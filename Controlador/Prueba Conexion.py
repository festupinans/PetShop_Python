import mysql.connector
from mysql.connector import Error

try:
    conexion= mysql.connector.connect(
        host='localhost',
        port='3306',
        user='Pacho',
        password='032620',
        db='world',
        auth_plugin='mysql_native_password'
    )

    if conexion.is_connected():
        print("Conexion exitosa.")

        cursor=conexion.cursor() # Inicializa la conexion en la variable cursor

        cursor.execute("SELECT database();")                # Nombre de la base de datos
        registro=cursor.fetchone()                          # Almacena los resultados en la variable
        print("Conectado a la base de datos: ", registro)


        # Como leer datos de una base mysql
        cursor.execute("SELECT * FROM country") #trae todos los elementos
        resultados=cursor.fetchall()            #almacena los resultados en la variable
        for fila in resultados:                 #Usamos un for por recorrer la consulta
            print(fila[0], fila[1], fila[2])
        # Como leer datos de una base mysql

        # Cuenta los elementos en la tabla
        print("Todal de registros: ", cursor.rowcount)
        

except Error as ex:
    print("Error durante la conexion:", ex)

finally:
    if conexion.is_connected():
        conexion.close()
        print("La conexion ha finalizado")
