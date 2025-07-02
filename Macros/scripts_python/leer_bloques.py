import ezdxf

# Ruta del archivo DWG a leer
archivo_dwg = "Project Automate/DIAGRAMA PID EJEMPLO (Documento creado por PROCESOS).dwg'"  # Cambiar luego por el nombre real

# Cargar el archivo DWG
doc = ezdxf.readfile(archivo_dwg)

# Acceder al modelspace
msp = doc.modelspace()

# Contador y listado de bloques encontrados
bloques_encontrados = []

# Buscar todos los INSERT (bloques insertados)
for entidad in msp.query("INSERT"):
    nombre_bloque = entidad.dxf.name
    bloques_encontrados.append(nombre_bloque)

# Eliminar duplicados (bloques con el mismo nombre)
bloques_unicos = list(set(bloques_encontrados))

# Mostrar el resultado
print("Bloques encontrados:")
for bloque in bloques_unicos:
    print("-", bloque)
