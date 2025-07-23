import cv2
import datetime
import time
import os

def grabar_partidos(duracion_bloque_seg=6, cantidad_bloques=3):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("No se pudo acceder a la cámara.")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = 20.0

    # Carpeta de salida
    carpeta_salida = "C:/Users/mati1/Desktop/videos"
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    fecha_hoy = datetime.datetime.now().strftime("%Y-%m-%d")

    for bloque in range(1, cantidad_bloques + 1):
        filename = os.path.join(
            carpeta_salida,
            f"partido_{fecha_hoy}_bloque{bloque}.mp4"
        )

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(filename, fourcc, fps, (width, height))

        print(f"Grabando bloque {bloque} - archivo: {filename}")
        tiempo_final = time.time() + duracion_bloque_seg

        while time.time() < tiempo_final:
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)
            cv2.imshow('Grabando...', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        out.release()
        print(f"Finalizó bloque {bloque}")

    cap.release()
    cv2.destroyAllWindows()
    print("Grabación finalizada")

# Cambiá los valores para pruebas
grabar_partidos(duracion_bloque_seg=6, cantidad_bloques=3)