import cv2
import datetime
import time

inicio = time.time()
def grabar_partidos(duracion_bloque_min=0.1, cantidad_bloques=1): 
    cap = cv2.VideoCapture(0) #camara por defecto 

    if not cap.isOpened():
        print("No se pudo acceder a la cámara.")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # frame para la visualizacion 
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = 20.0

    for i in range(cantidad_bloques):
        ahora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"/Users/maitegarcia/Desktop/videos/partido_{ahora}.mp4"
        fourcc = cv2.VideoWriter_fourcc(*'mp4v') #formato 
        out = cv2.VideoWriter(filename, fourcc, fps, (width, height))

        print(f"Grabando bloque {i+1} - archivo: {filename}")
        tiempo_final = time.time() + duracion_bloque_min * 60

        while time.time() < tiempo_final:
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)

            # Mostrar en pantalla la grabacion actual 
            cv2.imshow('Grabando...', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        out.release()
        print(f"Finalizó bloque {i+1}")

        duracion = time.time() - inicio 

    print("duracion video en segundos: {duracion} ")

    cap.release()
    cv2.destroyAllWindows()
    print("Grabación finalizada")

grabar_partidos()