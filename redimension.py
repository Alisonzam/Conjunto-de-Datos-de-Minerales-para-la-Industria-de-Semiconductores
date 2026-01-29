import os
from PIL import Image

#Carpeta principal donde están tus imágenes y subcarpetas
carpeta_principal = r"C:/Users/aliso/OneDrive/Escritorio/Aumento de Datos/imagenes minerales"

#Tamaño deseado
tamaño = (128, 128)

#Recorrer todas las subcarpetas e imágenes
for archivo in os.listdir(carpeta_principal):
    if archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
        ruta_imagen = os.path.join(carpeta_principal, archivo)
        carpeta_destino = os.path.join(carpeta_principal, archivo)
            # Redimensionar y guardar
            
        img = Image.open(ruta_imagen)
        img = img.resize(tamaño, Image.LANCZOS)
        
        img.save(carpeta_destino)


    
