try:
    import face_recognition
except ImportError:
    face_recognition = None

import numpy as np
from PIL import Image
import json

def generar_encoding_facial(foto_archivo):
    if not face_recognition:
        raise RuntimeError("face_recognition no está instalado. Instala: pip install face_recognition face_recognition_models")
    try:
        # 1. Abrimos la imagen con PIL y la forzamos a modo RGB (8-bit por canal)
        # Esto elimina transparencias (canales Alfa) y formatos raros automáticamente
        imagen_pil = Image.open(foto_archivo).convert('RGB')

        # 2. La convertimos en un array de Numpy para que face_recognition la entienda
        imagen_np = np.array(imagen_pil)

        # 3. Buscamos los encodings
        encodings = face_recognition.face_encodings(imagen_np)
        
        if encodings:
            # Convertimos el array a una lista normal para poder guardarlo como JSON
            return json.dumps(encodings[0].tolist())
        
        return None
        
    except Exception as e:
        print(f"Error al procesar la biometría: {e}")
        return None

def comparar_rostros(encoding_guardado_json, foto_nueva_archivo):
    if not face_recognition:
        raise RuntimeError("face_recognition no está instalado. Instala: pip install face_recognition face_recognition_models")
    try:
        # Hacemos el mismo proceso de limpieza para la foto del login
        imagen_pil = Image.open(foto_nueva_archivo).convert('RGB')
        imagen_np = np.array(imagen_pil)

        encodings_nuevos = face_recognition.face_encodings(imagen_np)
        
        if not encodings_nuevos:
            return False
            
        # Reconstruir el encoding guardado desde el JSON
        encoding_guardado = np.array(json.loads(encoding_guardado_json))
        encoding_nuevo = encodings_nuevos[0]
        
        # Comparar los dos rostros
        coincide = face_recognition.compare_faces([encoding_guardado], encoding_nuevo, tolerance=0.4)
        return coincide[0]
        
    except Exception as e:
        print(f"Error al comparar rostros: {e}")
        return False