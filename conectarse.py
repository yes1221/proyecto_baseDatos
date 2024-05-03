
import sqlite3

# Conecta a la base de datos SQLite (si no existe, se creará automáticamente)
conn = sqlite3.connect('nombre_de_tu_base_de_datos.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Ahora puedes ejecutar comandos SQL
# Por ejemplo, crear una tabla
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)''')

# Insertar datos en la tabla
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ('Juan', 30))
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ('María', 25))

# Guardar los cambios
conn.commit()

# Seleccionar datos de la tabla
cursor.execute("SELECT * FROM usuarios")
filas = cursor.fetchall()
for fila in filas:
    print(fila)

# Cerrar la conexión
conn.close()