# Youtube-To-audio

## Instalación de Dependencias

### Python y Bibliotecas Necesarias

1. Asegúrate de tener Python 3 instalado en tu sistema.

2. Instala las bibliotecas Python necesarias ejecutando el siguiente comando:
```sh
  pip install -r requirements.txt
  ```
 

 
### Instalación de ffmpeg

3. `pydub` utiliza `ffmpeg` para la conversión de archivos de audio. Asegúrate de tener `ffmpeg` instalado en tu sistema y disponible en el `PATH`.

- **En Ubuntu:**
  ```sh
  sudo apt update
  sudo apt install ffmpeg
  ```

- **En Windows:**
  - Descarga `ffmpeg` desde [ffmpeg.org](https://ffmpeg.org/download.html).
  - Añade la ruta de la carpeta `bin` de `ffmpeg` al `PATH` de tu sistema.

4. Verifica que `ffmpeg` esté instalado correctamente ejecutando:
```sh
ffmpeg -version

