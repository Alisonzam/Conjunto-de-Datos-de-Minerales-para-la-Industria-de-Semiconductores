import os 
from skimage import io
import pandas as pd

carpeta= r"C:/Users/aliso/OneDrive/Escritorio/Aumento de Datos/imagenes minerales"
if os.path.exists(r"C:/Users/aliso/OneDrive/Escritorio/Aumento de Datos/imagenes minerales"):
    print("existe")

datos = []

# Recorre todas las carpetas y subcarpetas
for raiz, carpetas, archivos in os.walk(carpeta):
    for archivo in archivos:
        # Filtrar imágenes por extensión
        if archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
            ruta_imagen = os.path.join(raiz, archivo)
            try:
                imagen = io.imread(ruta_imagen)
                alto, ancho = imagen.shape[:2]
                canales = 1 if len(imagen.shape) == 2 else imagen.shape[2]
                tamaño_kb = os.path.getsize(ruta_imagen) / 1024

                datos.append({
                    "Nombre": archivo,
                    "Carpeta": os.path.basename(raiz),
                    "Ancho": ancho,
                    "Alto": alto,
                    "Tamaño (KB)": round(tamaño_kb, 2)
                })
            except Exception as e:
                print(f"⚠️ Error al leer {ruta_imagen}: {e}")

# Crear DataFrame con los resultados
tabla = pd.DataFrame(datos)

# Mostrar la tabla
print("\n📊 RESULTADOS DEL ANÁLISIS DE IMÁGENES 📊\n")
print(tabla)
