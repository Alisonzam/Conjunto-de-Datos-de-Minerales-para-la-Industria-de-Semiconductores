import numpy as np
if not hasattr(np, 'bool'):
    np.bool = bool
import random
import imgaug.augmenters as iaa
import imageio.v2 as imageio
import imageio.v2 as imageio
import os 
import cv2


class imageAument:
    def __init__(self, carpeta,  num_aug,num_crops,crop_size):
        self.carpeta=carpeta
        self.num_aug = num_aug
        self.num_crops = num_crops
        self.crop_size = crop_size

        self.augmentations= {
            "flip1": iaa.Fliplr(1), # sides
            "flip2": iaa.Flipud(1), #down
            "rot90": iaa.Rotate(90),
            "rot180": iaa.Rotate(180),
            "rot270": iaa.Rotate(270),
            "bright": iaa.Multiply((0.5, 1.5)), 
            "contrast": iaa.LinearContrast((0.5, 1.5)),
            "rg": iaa.AdditiveGaussianNoise(scale=(0, 0.03*255))
        }

    def random_crop_128(self):

    # All images
        for filename in os.listdir(self.carpeta):
            path = os.path.join(self.carpeta, filename)

            # Validate file in format
            if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                continue

            img = cv2.imread(path)

            if img is None:
                print(f"No se pudo leer {path}")
                continue

            h, w = img.shape[:2]

            for i in range(self.num_crops):
                # cropping size
                crop_size = random.randint(self.crop_size, min(h, w))

                # position 
                x = random.randint(0, w - self.crop_size)
                y = random.randint(0, h - self.crop_size)

                # crop
                crop = img[y:y+self.crop_size, x:x+self.crop_size]

                # 128x128
                crop_128 = cv2.resize(crop, (128, 128), interpolation=cv2.INTER_AREA)

                # name out
                out_name = f"{os.path.splitext(filename)[0]}_crop_random_{i}.png"
                out_path = os.path.join(self.carpeta, out_name)

                # save
                cv2.imwrite(out_path, crop_128)
                #print(f"Guardado: {out_path}")

    def apply_aug(self):
        
        #generate
        for archivo in os.listdir(self.carpeta):
            if not archivo.lower().endswith(('.jpg', '.png', '.jpeg')):
                continue

            ruta_img = os.path.join(self.carpeta, archivo)
            imagen = imageio.imread(ruta_img)

            for i in range(1, self.num_aug + 1):
               
               # Choose between 2 and 4 magnifications
                aug_names = random.sample(list(self.augmentations.keys()), k=random.randint(2, 4))

                # Create a sequence of increments based on the names
                seq = iaa.Sequential([self.augmentations[n] for n in aug_names])
                
                imagen_aug = seq(image=imagen)

                aug_label = "_".join(aug_names)

                 # name descriptive
                nombre_base, ext = os.path.splitext(archivo)
                nuevo_nombre = f"{nombre_base}_{aug_label}{ext}"

                ruta_nueva = os.path.join(self.carpeta, nuevo_nombre)
                imageio.imwrite(ruta_nueva, imagen_aug)           
    
    def process(self):
        print("Cropping images...")
        self.random_crop_128()
        print("Apply Data Augmentation...")
        self.apply_aug()


folder = r"C:/Users/aliso/OneDrive/Escritorio/Aumento de Datos/pirita"
aumentor = imageAument(folder,18,5,70)
aumentor.process()

