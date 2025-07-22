import cv2
import datetime
import time
import os

def grabar_partidos(duracion_bloque_min=1, cantidad_bloques=1):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("No se pudo acceder a la cámara.")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = 20.0

    # Ruta donde guardar los videos
    carpeta_salida = "C:/Users/matil/Desktop/videos"

    # Crear carpeta si no existe
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    for i in range(cantidad_bloques):
        ahora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(carpeta_salida, f"partido_{ahora}.mp4")
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(filename, fourcc, fps, (width, height))

        print(f"Grabando bloque {i+1} - archivo: {filename}")
        tiempo_final = time.time() + duracion_bloque_min * 60

        while time.time() < tiempo_final:
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)
            cv2.imshow('Grabando...', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        out.release()
        print(f"Finalizó bloque {i+1}")

    cap.release()
    cv2.destroyAllWindows()
    print("Grabación finalizada")

# Cambiá los valores para testear
grabar_partidos(duracion_bloque_min=0.5, cantidad_bloques=1)